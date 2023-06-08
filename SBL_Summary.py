import pandas as pd  # pip install pandas openpyxl
# import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit


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



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SBL Daily Monitor", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=2,
        nrows=1000,
    )
    # df = pd.read_excel("supermarkt_sales.xlsx", index_col=False, skiprows=3)
    # Add 'hour' column to dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)

# ---- MAINPAGE ----
st.title(":bar_chart: SBL Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total SBL Hold Lots:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Total SBL Hold Wafers:")
    st.subheader(f"{average_rating}")
with right_column:
    st.subheader("SBL Hold Rates:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)
# st.echo()
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


# create 8 products cards
# card_col1, card_col2, card_col3, card_col4 = st.columns(4)

card_col1, card_col2, card_col3, card_col4 = st.columns(4)
title = "N2XM"
content = "42"
color = "#DAF7A6"  # Change the color to your preferred value (e.g., #ff0000 for red)

with card_col1:
    card_component(title, content, color)
    card_component(title, content, color)
with card_col2:
    card_component(title, content, color)
    card_component(title, content, color)
with card_col3:
    card_component(title, content, color)
    card_component(title, content, color)
with card_col4:
    card_component(title, content, color)
    card_component(title, content, color)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# https://github.com/Sven-Bo/streamlit-sales-dashboard
# F0F6F3
