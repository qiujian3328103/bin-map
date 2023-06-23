import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
# Show the figure
import streamlit as st 
pio.templates.default = "plotly"

def addSquare(fig, x0, y0, x1, y1, die_x, die_y):

    lineCol = "black"

    fig.add_trace(
        go.Scatter(
            x=[x0,x0,x1,x1,x0], 
            y=[y0,y1,y1,y0,y0], 
            fill="toself",
            fillcolor='LightGreen',
            mode='lines',
            name='',
            text=f'die {die_x} {die_x}<br>bin_value:',
            line_color=lineCol,
            opacity=1,
            showlegend=False
        )
    )



df_raw = pd.read_csv('KAMORTA.csv', index_col=False)
print(df_raw["sort_test_flag"].unique().tolist())
# print(df_raw.columns)
# print(df_raw)

x_list = sorted(df_raw["ucs_die_origin_x"].unique().tolist())
y_list = sorted(df_raw["ucs_die_origin_y"].unique().tolist())
size_x = abs(x_list[0]) - abs(x_list[1])
size_y = abs(y_list[0]) - abs(y_list[1])


df_raw['X_BottomLeft'] = df_raw["ucs_die_origin_x"] - size_x/2
df_raw['X_TopRight'] = df_raw["ucs_die_origin_x"] + size_x/2
df_raw['Y_BottomLeft'] = df_raw["ucs_die_origin_y"] - size_y/2
df_raw['Y_TopRight'] = df_raw["ucs_die_origin_y"] + size_y/2

# df_raw['X_BottomLeft'] = df_raw["ucs_die_origin_x"] - die_size["KAMORTA"]["Die_Size_X"]/2
# df_raw['X_TopRight'] = df_raw["ucs_die_origin_x"] + die_size["KAMORTA"]["Die_Size_X"]/2
# df_raw['Y_BottomLeft'] = df_raw["ucs_die_origin_y"] - die_size["KAMORTA"]["Die_Size_Y"]/2
# df_raw['Y_TopRight'] = df_raw["ucs_die_origin_y"] + die_size["KAMORTA"]["Die_Size_Y"]/2

df = df_raw[df_raw["sort_test_flag"]=="T"]

fig = go.Figure(layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    ))

# Add circle shape
fig.add_shape(
    type="circle",
    xref="x",
    yref="y",
    x0=-150,
    y0=-150,
    x1=150,
    y1=150,
    line_color="LightSeaGreen",
)

# Iterate through each die and draw rectangles
for index, row in df.iterrows():
    x_bottom_left = row['X_BottomLeft'] * 0.001
    y_bottom_left = row['Y_BottomLeft'] * 0.001
    x_top_right = row['X_TopRight'] * 0.001
    y_top_right = row['Y_TopRight'] * 0.001
    die_x = row["sort_die_x"]
    die_y = row["sort_die_y"]
    bin_data = row["component_id"]
    x = [x_bottom_left, x_bottom_left, x_top_right, x_top_right, x_bottom_left]
    y = [y_bottom_left, y_top_right, y_top_right, y_bottom_left, y_bottom_left]

    addSquare(fig, x0=x_bottom_left, y0=y_bottom_left, x1=x_top_right, y1=y_top_right, die_x=die_x, die_y=die_y)


fig.update_layout(
    xaxis=dict(range=[-150, 150]),  # Adjust the x-axis range if necessary
    yaxis=dict(range=[-150, 150]),  # Adjust the y-axis range if necessary
    hovermode='closest',
    showlegend=False,  # Remove the legend
    scene=dict(
        aspectratio=dict(x=1, y=1, z=1)  # Set equal aspect ratio for x, y, and z
    ),
    hoverlabel=dict(
        bgcolor="black",
    ), 
    height=800, 
    coloraxis_colorbar=dict(
    title="Species",
    tickvals=[1,2,3],
    ticktext=["setosa","versicolor","virginica"],
    lenmode="pixels", len=100,)
    )

# fig.show()

st.plotly_chart(fig, height=800)
