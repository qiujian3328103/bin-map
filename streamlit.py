import streamlit as st

def card_component(title, content, color):
    """
    Function to create a card component with a specific color using Streamlit.
    """
    st.markdown(
        f"""
        <div style='background-color: {color}; padding: 20px; border-radius: 10px; width: 150px;'>
            <h3 style='text-align: center; color: black; font-size: 20px;'>{title}</h3>
            <p style='color: black; margin-bottom: 0;'>Hold Lots: {content}</p>
            <p style='color: black; margin-top: 0;'>Hold Wafers: {content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Example usage
title = "N2XM"
content = "42"
color = "#DAF7A6"  # Change the color to your preferred value (e.g., #ff0000 for red)

st.write("# Streamlit Card Component Example")
card_component(title, content, color)

# --------------------------------------------------------------------------------------# 

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
# st.echo()



# df = pd.read_csv(r"C:\Users\Jian Qiu\Dropbox\StSBLDashboard\fake_dataset.csv", index_col=False)
#
# # Convert the "date" column to datetime type
# df['date'] = pd.to_datetime(df['date'])
#
# # Extract the day, month, week, and year from the "date" column
# df['Day'] = df['date'].dt.strftime("%d")
# df['Month'] = df['date'].dt.strftime("%m")
# df['Week'] = df['date'].dt.strftime("%U")
# df['Year'] = df['date'].dt.strftime("%Y")
# df['Month'] = df['date'].dt.strftime("%B")
# # Set the "Month" column as categorical with the desired order
# month_order = ['January', 'February', 'March', 'April', 'May', 'June',
#                'July', 'August', 'September', 'October', 'November', 'December']
# df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
# df = df.sort_values('Month')
# fig = px.bar(
#     df,
#     x="Month",
#     y="wafer_id",
#     # orientation="h",
#     color="hold",
#     title="<b>Sales by Product Line</b>",
#     color_discrete_sequence=px.colors.qualitative.Dark24,
#     # template="plotly_white",
# )
#
# fig.update_layout(
#     title="Plot Title",
#     xaxis_title="X Axis Title",
#     yaxis_title="Y Axis Title",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=14,
#         color="RebeccaPurple"
#     )
# )
#
# st.plotly_chart(fig, use_container_width=True)

import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv(r"C:\Users\Jian Qiu\Dropbox\StSBLDashboard\fake_dataset.csv", index_col=False)

# Convert the "date" column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Extract the month from the "date" column
df['Month'] = df['date'].dt.strftime("%B")

# Sort the DataFrame by the "Month" column
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
df = df.sort_values('Month')

# Group by "Month" and "hold", and calculate the count
df_grouped = df.groupby(['Month', 'hold']).size().unstack()

# Calculate the percentage of "PE" hold for each month
df_percent = df_grouped['PE HOLD'] / df_grouped.sum(axis=1)

# Create subplots with shared x-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add stacked bar chart for hold groups
for column in df_grouped.columns:
    fig.add_trace(
        go.Bar(x=df_grouped.index, y=df_grouped[column], name=column),
        secondary_y=False,
    )

# Add line chart for "PE" hold percentage
fig.add_trace(
    go.Scatter(x=df_percent.index, y=df_percent, mode='lines+markers', name='PE Hold Percentage'),
    secondary_y=True,
)

# Add percentage annotations on each line point
for i in range(len(df_percent)):
    fig.add_annotation(
        x=df_percent.index[i],
        y=df_percent.iloc[i],
        text=f"{df_percent.iloc[i]*100:.2f}%",  # Display as percentage
        showarrow=True,
        arrowhead=1,
        arrowcolor='black',
        ax=0,
        ay=-30,
        font=dict(color="white")  # Set the font color to white
    )

fig.update_layout(
    barmode='stack',
    title="Sales by Product Line",
    xaxis_title="Month",
    yaxis_title="Wafer ID",
    yaxis2_title="PE Hold Percentage",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    ),
    width=1000,
)

# Set the second y-axis range from 0 to 1
fig.update_yaxes(range=[0, 1], secondary_y=True)

st.plotly_chart(fig, use_container_width=True, width=1000)




###################################################################################################
# Filter the dataframe for "PE HOLD"
df_pe_hold = df[df['hold'] == 'PE HOLD']

# Group by "product_id" and calculate the count
df_count = df_pe_hold.groupby('product_id').size().reset_index(name='count')


# Determine the number of columns and rows for the grid layout
num_cols = 4
num_rows = -(-len(df_count) // num_cols)  # Round up division

# Create a grid layout for the card widgets
grid = st.container()
with grid:
    st.markdown("---")
    st.markdown('<h2 style="text-align: center;">Product ID and PE HOLD Counts</h2>', unsafe_allow_html=True)
    for i in range(num_rows):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            index = i * num_cols + j
            if index < len(df_count):
                product_id = df_count.iloc[index]['product_id']
                count = df_count.iloc[index]['count']
                card_title = f"<h3 style='text-align: center;'>Product ID: {product_id}</h3>"
                card_text = f"<p style='text-align: center;'>Number of PE HOLD: {count}</p>"
                cols[j].markdown(f'<div style="background-color: #F0E68C; padding: 10px; border-radius: 5px; margin-bottom: 10px;">{card_title}{card_text}</div>', unsafe_allow_html=True)
                
                
