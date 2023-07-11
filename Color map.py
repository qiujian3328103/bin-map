# Define the start and end colors
start_color = (0, 255, 0)  # Green
end_color = (255, 0, 0)    # Red

# Define the list of values
lst = [1, 0, 10, 20, 8, 9, 12, 14, 20]

# Define the number of intervals
num_intervals = 20

# Create the color map
color_map = create_color_map(start_color, end_color, num_intervals)

# Get the color for each value in the list
color_list = [get_color_from_value(value, lst, color_map) for value in lst]

# Display the resulting colors
for value, color in zip(lst, color_list):
    print(f"Value: {value}, Color: {color}")
