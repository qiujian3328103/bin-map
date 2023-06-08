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
