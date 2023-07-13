import itertools

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.models import HoverTool
import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet, LinearAxis, Select, LinearColorMapper, Slider, CustomJS
from bokeh.models import HoverTool
from bokeh.layouts import column, row 
import streamlit as st 
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256, Inferno256, Magma256, Plasma256, Viridis256, Cividis256, Turbo256
import numpy as np 
import json

die_size = {
  "ZB10717-1F":{
    "Die_Size_X":6223,
    "Die_Size_Y":5098
  },
  "ZB10717-2F":{
    "Die_Size_X":6223,
    "Die_Size_Y":5098
  },
  "ZB10820-1F":{
    "Die_Size_X":3713.6,
    "Die_Size_Y":4153.6
  },
  "ZB10897-1F":{
    "Die_Size_X":6867.984,
    "Die_Size_Y":4247.68
  },
  "10VEGA1":{
    "Die_Size_X":19555.472,
    "Die_Size_Y":26121.872
  },
  "KAMORTA":{
    "Die_Size_X":7270.96,
    "Die_Size_Y":6559.46
  }
}

df_raw = pd.read_csv('KAMORTA.csv', index_col=False)
df = df_raw
df = df_raw[df_raw["sort_test_flag"]=="T"]

x_list = sorted(df_raw["ucs_die_origin_x"].unique().tolist())
y_list = sorted(df_raw["ucs_die_origin_y"].unique().tolist())

size_x = abs(x_list[0]) - abs(x_list[1])
size_y = abs(y_list[0]) - abs(y_list[1])

print(size_x, size_y)

df['left'] = df_raw["ucs_die_origin_x"]*0.001 - 0.001*size_x/2
df['right'] = df_raw["ucs_die_origin_x"]*0.001 + 0.001*size_x/2
df['bottom'] = df_raw["ucs_die_origin_y"]*0.001 - 0.001*size_y/2
df['top'] = df_raw["ucs_die_origin_y"]*0.001 + 0.001*size_y/2

# Create a sample dataframe
df['bin_value'] = np.random.randint(0, 51, size=len(df))
print(df)
# Create a color palette
# Define the color palette
color_palette = Viridis256


# Define a mapping function to assign colors based on bin values
def assign_color(bin_value):
    index = int((bin_value / df['bin_value'].max()) * (len(color_palette) - 1))
    return color_palette[index]

# Create a new column 'color' based on the bin_value
df['color'] = df['bin_value'].apply(assign_color)


# Assign colors based on the normalized 'bin_value'
# df['color'] = df['norm_bin_value'].apply(lambda x: color_palette[int(x * (len(color_palette) - 1))])

print(df["color"])

# width = die_size["ZB10820-1F"]["Die_Size_X"]
# height = die_size["ZB10820-1F"]["Die_Size_Y"]

# # calcualte the bottom and top coordinate for each die 
# df['left'] = df['ucs_die_origin_x']*0.001 - 0.001*height/2
# df['right'] = df['ucs_die_origin_x']*0.001 + 0.001*height/2
# df['bottom'] = df['ucs_die_origin_y'] *0.001- 0.001*width/2
# df['top'] = df['ucs_die_origin_y']*0.001 + 0.001*width/2
# df["color"]="green"

print(df.columns)

# columnd data source of dataframe 
source = ColumnDataSource(df)


fig_size = (500, 500)

plot = figure(plot_width=fig_size[0], plot_height=fig_size[1], 
              x_range=(-180, 180),
              y_range=(-180, 180),
              aspect_scale=1)


cell = plot.quad(source=source, left='left', right='right', 
       bottom='bottom', top='top', color="color",
       fill_alpha=1, line_color='black')

# Add the annulus glyph for the wafer layout
# wafer = plot.annulus(x=0, y=0, inner_radius=150,
#              fill_color='white', fill_alpha=1, line_color='black', level='underlay')
# Draw the circle
circle = plot.circle(x=0, y=0, radius=155, fill_color='white', line_color='black', level='underlay')

hover = HoverTool(renderers=[cell], tooltips=[('Sort Die X', '@sort_die_x'),
                                              ('Sort Die Y', '@sort_die_y'), 
                                              ('Bin Value', '@bin_value')])

plot.add_tools(hover)

# Create additional axes
plot.extra_x_ranges = {"top_range": plot.x_range}
plot.extra_y_ranges = {"right_range": plot.y_range}

# Add additional x-axis and y-axis on the top and right side
plot.add_layout(LinearAxis(x_range_name="top_range"), 'above')
plot.add_layout(LinearAxis(y_range_name="right_range"), 'right')







# Create a Select widget for color selection
bin_value_slider = Slider(start=0, end=100, value=5, step=1, title="Stuff")
# Create a Select widget for color theme selection
color_theme_select = Select(title="Color Theme:", options=["Viridis256", "Inferno256", "Magma256", "Plasma256", "Turbo256"], value="Turbo256")

print(Viridis256)


################################################################################################################################################

# Define the JavaScript code for the CustomJS callback
# Define the JavaScript code for the CustomJS callback
custom_js_code = """
    // Get the selected color theme
    var colorTheme = color_theme_select.value;
    
    // Get the selected bin value
    var binValue = bin_value_slider.value;
    
    // Get the selected color theme data
    var colorTheme1 = JSON.parse(color_them_1);
    var colorTheme2 = JSON.parse(color_them_2);
    var colorTheme3 = JSON.parse(color_them_3);
    var colorTheme4 = JSON.parse(color_them_4);
    var colorTheme5 = JSON.parse(color_them_5);
    
    // Define the color palette based on the color theme
    var colorPalette;
    if (colorTheme === "Viridis256") {
        colorPalette = colorTheme1;
    } else if (colorTheme === "Inferno256") {
        colorPalette = colorTheme2;
    } else if (colorTheme === "Magma256") {
        colorPalette = colorTheme3;
    } else if (colorTheme === "Plasma256") {
        colorPalette = colorTheme4;
    } else if (colorTheme === "Turbo256") {
        colorPalette = colorTheme5;
    }
    
    // Calculate the color interval based on the number of colors and the bin value
    var maxBinValue = Math.max.apply(Math, source.data['bin_value']);
    var colorInterval = Math.floor(colorPalette.length / binValue);
    
    // Create a new color list with the desired color interval
    var newColorList = [];
    for (var i = 0; i < colorPalette.length; i += colorInterval) {
        newColorList.push(colorPalette[i]);
    }
    
    // Update the color column based on the bin value and new color list
    source.data['color'] = source.data['bin_value'].map(function (value) {
        var colorIndex = Math.floor((value / maxBinValue) * (newColorList.length - 1));
        return newColorList[colorIndex];
    });
    source.change.emit();
"""

# Create the CustomJS callback
custom_js_callback = CustomJS(args=dict(source=cell.data_source, 
                                        color_theme_select=color_theme_select, 
                                        bin_value_slider=bin_value_slider, 
                                        color_them_1=json.dumps(Viridis256), 
                                        color_them_2=json.dumps(Inferno256), 
                                        color_them_3=json.dumps(Magma256), 
                                        color_them_4=json.dumps(Plasma256), 
                                        color_them_5=json.dumps(Turbo256)), 
                              code=custom_js_code)


# Assign the CustomJS callback to the color theme select and bin value slider
color_theme_select.js_on_change('value', custom_js_callback)
bin_value_slider.js_on_change('value', custom_js_callback)






bk_col = column(color_theme_select, bin_value_slider)

bk_row = row(bk_col, plot)

st.sidebar.selectbox("Select Data: ", options=["Select A", "Select B"], index=0)
# show(plot)
st.bokeh_chart(bk_row, use_container_width=False)


