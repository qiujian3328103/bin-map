js code 

theme_callback = CustomJS(args=dict(source=source, color_theme=color_theme), code="""
    // Get the selected color theme
    var theme = color_theme.value;

    // Define the color palettes for different themes
    var colorPaletteTheme1 = %s;
    var colorPaletteTheme2 = %s;

    // Function to get colors based on the selected theme
    function getColorsFromTheme(theme) {
        if (theme === "Theme 1") {
            return source.data['bin_value'].map(function(value) {
                var index = Math.round(value);
                return colorPaletteTheme1[index];
            });
        } else if (theme === "Theme 2") {
            return source.data['bin_value'].map(function(value) {
                var index = Math.round(value);
                return colorPaletteTheme2[index];
            });
        } else {
            return Array(source.get_length()).fill("green");
        }
    }

    // Update the color column in the source with colors based on the selected theme
    source.data['color'] = getColorsFromTheme(theme);

    // Trigger the update of the plot
    source.change.emit();
""" % (color_palette_theme1, color_palette_theme2))
