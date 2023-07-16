import plotly.express as px
import numpy as np
import plotly.graph_objects as go

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
            if row[i] == "F":
                new_row.append(0)
            elif row[i] == "P":
                new_row.append(1)
            else:
                new_row.append(row[i])
        new_shmoo_data.append(new_row)
    
    # Create freq list (last row except first element)
    freq = [int(element) for index, element in enumerate(new_shmoo_data[-1][1:])]
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
