import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from test_shmoo_data import test_shmoo_data
def addSquare(fig, x0, y0, x1, y1, voltage, freq, fill_color, result):

    lineCol = "black"
    if result == 0:
        pass_fail = "Pass"
    else:
        pass_fail = "Fail"
    fig.add_trace(
        go.Scatter(
            x=[x0,x0,x1,x1,x0], 
            y=[y0,y1,y1,y0,y0], 
            fill="toself",
            fillcolor=fill_color,
            mode='lines',
            name='',
            text=f'Vdd {voltage}<br>Freq: {freq}<br>{pass_fail}',
            line_color=lineCol,
            opacity=1,
            showlegend=False
        )
    )


def create_shmoo_plot(shmoo_data, hoverlabel_color="black"):
    """
    shmoo_data = [
        ["100", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
        ["90", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
        ["80", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
        ["70", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
        ["60", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
        ["50", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
        ["40", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
        ["30", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
        ["20", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
        ["10", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
        ["0", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
        ["ATPG", "0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75","80", "85","90", "95","100"]
    ]



    """

    # Convert "F" to 0 and "P" to 1
    new_shmoo_data = []
    for row in shmoo_data:
        new_row = [row[0]]
        for i in range(1, len(row)):
            if row[i] == "F" or row[i]==".":
                new_row.append(0)
            elif row[i] == "P" or row[i]=="#":
                new_row.append(1)
            else:
                new_row.append(row[i])
        new_shmoo_data.append(new_row)
    
    # Create freq list (last row except first element)
    freq = [float(element) for index, element in enumerate(new_shmoo_data[-1][1:])]
    # Create voltage list (first element of each list except the last list)
    voltage = [row[0] for row in new_shmoo_data[:-1]]

    reverse_voltage_label = voltage[::-1]
    # reverse the data list, so that the plot poistion and value can match 
    data = [row[1:] for row in new_shmoo_data[:-1]]
    data = data[::-1]

    fig = go.Figure()
    for col_index in range(len(freq)):
        for row_index in range(len(voltage)):
            if data[row_index][col_index] == 0:
                shape_color = "red"
            elif data[row_index][col_index] == 1:
                shape_color = "green"
            addSquare(fig=fig, x0=col_index, y0=row_index, x1=col_index+1, y1=row_index+1, fill_color=shape_color, voltage=reverse_voltage_label[row_index], freq=freq[col_index], result=data[row_index][col_index])

    
    fig.update_layout(
        xaxis=dict(
            range=[0, len(freq)+1],
            tickmode='array',
            tickvals=[x + 0.5 for x in range(len(freq))],
            ticktext=freq,
            title="Freq"
        ),
        yaxis=dict(
            range=[0, len(reverse_voltage_label)+1],
            tickmode='array',
            tickvals=[x + 0.5 for x in range(len(reverse_voltage_label))],
            ticktext=reverse_voltage_label,
            title="Voltage"
        ),
        hovermode='closest',
        hoverlabel=dict(bgcolor="black"),
        # plot_bgcolor='rgba(0, 0, 0, 0)',
        # paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig 


def read_shmoo_data(lines, die="Die1"):
    """Summary
    analyze the lines data and retrurn a dictionary

    Args:
        lines (TYPE): list of lists

        ["SHmmo TesT Program", "Test Site: 0", "AdjusTESTRange:Fasle", "ResultMode is Results", "CurrentPatternName:test_program_name1", "PatternCycleCount:11111", "Current_V_Spec:VDDCX=0.1V", 
        "Current_T_Spec:ATPG_Shift_100MHz", "VcoefLL_ADJ:0.6V", "ATPG_Shift_700MHZ", "CurrentPatternName:test_program_name1",
            '100.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '95.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '90.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '85.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '80.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '75.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '70.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '65.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '60.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '55.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '50.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '45.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '40.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '35.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            '30.00\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t',
            'X-Aixs\t0.60\t0.61\t0.62\t0.63\t0.64\t0.65\t0.66\t0.67\t0.68\t0.69\t0.70\t0.71\t0.72\t0.73\t0.74\t0.75\t0.76\t0.77\t0.78\t0.79\t0.80\t0.81\t0.82\t0.83\t0.84\t0.85\t0.86\t0.87\t0.88\t0.89\t0.90\t0.91\t0.92\t0.93\t0.94\t0.95\t0.96\t0.97\t0.98\t0.99\t:VDDCX (v)',
    """

    restult_dict = {die:{}}

    is_shmoo_data = False

    is_test_info = True 

    shmoo_data_lines = []
    test_info = ""
    count_shmoo = 0
    current_test_program = ""
    for index, line in enumerate(lines):
        # print(index)
        # print(line)
        if is_test_info:
            test_info = test_info + line +"\n"

        if is_shmoo_data:
            if "X-Aixs" in line:
                # remove the "X-Aixs" and last elemnet and add new elemetn 
                line_list = line.split("\t")
                modified_line = ['ATPG'] + line_list[1:-1]
                shmoo_data_lines.append(modified_line)
            else:
                shmoo_data_lines.append(line.split("\t"))

        if "CurrentPatternName" in line and "\t" in lines[index+1]:
            # print("pass")
            is_shmoo_data = True 
            is_test_info = False
            current_test_program = line


        if "X-Aixs" in line:
            is_test_info = True 
            is_shmoo_data = False 
            count_shmoo = count_shmoo+1
            restult_dict[die].update(
                   {current_test_program:
                        {
                            "shmoo_data":shmoo_data_lines,
                             "test_info":test_info
                        }
                    }
            )
            shmoo_data_lines = []
            test_info = ""

    return restult_dict


# shmoo_data = [
#     ["100", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
#     ["90", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
#     ["80", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
#     ["70", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
#     ["60", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
#     ["50", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P","P", "P","P", "P", "P"],
#     ["40", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
#     ["30", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
#     ["20", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
#     ["10", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
#     ["0", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F","F", "F","F", "F", "P"],
#     ["ATPG", "0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75","80", "85","90", "95","100"]
# ]

# fig = create_shmoo_plot(shmoo_data=shmoo_data)
# fig.show()