def interpolate_color(start_color, end_color, fraction):
    # Convert RGB colors to separate components
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color
    
    # Interpolate the RGB components
    interpolated_r = int(start_r + fraction * (end_r - start_r))
    interpolated_g = int(start_g + fraction * (end_g - start_g))
    interpolated_b = int(start_b + fraction * (end_b - start_b))
    
    # Return the interpolated color as a tuple
    return (interpolated_r, interpolated_g, interpolated_b)

def create_color_map(start_color, end_color, num_intervals):
    color_map = []
    
    # Calculate the fraction step size
    step = 1.0 / (num_intervals - 1)
    
    # Generate the color map by interpolating colors
    for i in range(num_intervals):
        fraction = i * step
        color = interpolate_color(start_color, end_color, fraction)
        color_map.append(color)
    
    return color_map

def get_color_from_value(value, lst, color_map):
    num_intervals = len(color_map)
    
    # Calculate the interval size
    interval_size = max(lst) / (num_intervals - 1)
    
    # Calculate the interval index for the given value
    interval_index = int(value / interval_size)
    
    # Handle values exceeding the maximum
    if interval_index >= num_intervals - 1:
        interval_index = num_intervals - 2
    
    # Interpolate the color based on the value
    start_color = color_map[interval_index]
    end_color = color_map[interval_index + 1]
    fraction = (value - interval_index * interval_size) / interval_size
    interpolated_color = interpolate_color(start_color, end_color, fraction)
    
    return interpolated_color
    


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
