import itertools

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.models import HoverTool
import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, LinearAxis
import streamlit as st 



df_raw = pd.read_csv('sample.csv', index_col=False)
df = df_raw
df = df_raw[df_raw["sort_test_flag"]=="T"]
width = die_size["ZB10820-1F"]["Die_Size_X"]
height = die_size["ZB10820-1F"]["Die_Size_Y"]

# calcualte the bottom and top coordinate for each die 
df['left'] = df['ucs_die_origin_x']*0.001 - 0.001*height/2
df['right'] = df['ucs_die_origin_x']*0.001 + 0.001*height/2
df['bottom'] = df['ucs_die_origin_y'] *0.001- 0.001*width/2
df['top'] = df['ucs_die_origin_y']*0.001 + 0.001*width/2
df["color"]="green"

# columnd data source of dataframe 
source = ColumnDataSource(df)


fig_size = (500, 500)

plot = figure(plot_width=fig_size[0], plot_height=fig_size[1], 
              x_range=(-160, 160),
              y_range=(-160, 160),
              aspect_scale=1)


cell = plot.quad(source=source, left='left', right='right', 
       bottom='bottom', top='top', color="color",
       fill_alpha=1, line_color='black')
# Add the annulus glyph for the wafer layout
# wafer = plot.annulus(x=0, y=0, inner_radius=150,
#              fill_color='white', fill_alpha=1, line_color='black', level='underlay')
# Draw the circle
circle = plot.circle(x=0, y=0, radius=150, fill_color='white', line_color='black', level='underlay')

hover = HoverTool(renderers=[cell], tooltips=[('Sort Die X', '@sort_die_x'),
                                              ('Sort Die Y', '@sort_die_y')])

plot.add_tools(hover)

# Create additional axes
plot.extra_x_ranges = {"top_range": plot.x_range}
plot.extra_y_ranges = {"right_range": plot.y_range}

# Add additional x-axis and y-axis on the top and right side
plot.add_layout(LinearAxis(x_range_name="top_range"), 'above')
plot.add_layout(LinearAxis(y_range_name="right_range"), 'right')


# show(plot)
st.bokeh_chart(plot)
