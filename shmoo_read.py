import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, ClientsideFunction

import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib
import plotly.graph_objects as go

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Shmoo Analytics Dashboard"

server = app.server
app.config.suppress_callback_exceptions = True

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

# # Read data
df = pd.read_csv(DATA_PATH.joinpath("clinical_analytics.csv.gz"))

clinic_list = df["Clinic Name"].unique()
# df["Admit Source"] = df["Admit Source"].fillna("Not Identified")
admit_list = df["Admit Source"].unique().tolist()


data =  [[.1, .3, .5, .7, .9],
     [1, .8, .6, .4, .2],
     [.2, 0, .5, .7, .9],
     [.9, .8, .4, .2, 0],
     [.3, .4, .5, .7, 1]]

def description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Shmoo Reader"),
            html.H3("Welcome to the Shmoo Reader Dashboard"),
            html.Div(
                id="intro",
                children="Explore different Shmoo Files to Visulize and Generate Shmoo Plot",
            ),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.P("Select Product"),
            dcc.Dropdown(
                id="product-select",
                options=[{"label": i, "value": i} for i in ["Waikiki", "Hamilton", "Magnus"]],
                value="Waikiki",
            ),
            html.Br(),
            html.P("Select Shmoo Test Type"),
            dcc.Dropdown(
                id="admit-select",
                options=[{"label": i, "value": i} for i in ["TDF", "ATPG", "MBIST"]],
                value="TDF",
                multi=True,
            ),
            html.Br(),
            html.P("Upload CSV"),
            dcc.Upload(
                id="upload-data",
                children=html.Div(["Drag and drop or click to select a file to upload."]),
            style={
                "width": "100%",
                "height": "80px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=True,
                ),
            html.Br(),
            html.Div(
                id="reset-btn-outer",
                children=[
                    html.Button(id="plot-btn", children="Plot", n_clicks=0),
                    html.Button(id="download-btn", children="Download", n_clicks=0),
                    html.Button(id="reset-btn", children="Reset", n_clicks=0),
                ],
                style={"display": "flex", "justify-content": "space-between"},
            ),
        ],
    )

app.layout = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("plotly_logo.png"))],
        ),
        # Left column
        html.Div(
            id="left-column",
            className="four columns",
            children=[description_card(), generate_control_card()]
            + [
                html.Div(
                    ["initial child"], id="output-clientside", style={"display": "none"}
                )
            ],
        ),
        # Right column
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                # Patient Volume Heatmap
                html.Div(
                    id="shmoo_plot_card",
                    children=[
                        html.B("Shmoo Plot"),
                        html.Hr(),
                        dcc.Graph(id="patient_volume_hm"),
                    ],
                ),
                # Patient Wait time by Department
                html.Div(
                    id="wait_time_card",
                    children=[
                        html.B("Select Test Program and Die Size"),
                        html.Hr(),
                        # html.Div(id="wait_time_table", children=initialize_table()),
                    ],
                ),
            ],
        ),
    ],
)

# @app.callback(
#     Output("patient_volume_hm", "figure"),
#     [Input("plot-btn", "n_clicks"), Input("reset-btn", "n_clicks")]
# )
# def update_plots(plot_clicks, reset_clicks):
#     ctx = dash.callback_context
#     if ctx.triggered:
#         button_id = ctx.triggered[0]["prop_id"].split(".")[0]
#         if button_id == "plot-btn":
#             # Generate heatmap data
#             data = [[0.1, 0.3, 0.5, 0.7, 0.9],
#                     [1, 0.8, 0.6, 0.4, 0.2],
#                     [0.2, 0, 0.5, 0.7, 0.9],
#                     [0.9, 0.8, 0.4, 0.2, 0],
#                     [0.3, 0.4, 0.5, 0.7, 1]]

#             fig = go.Figure(data=go.Heatmap(z=data))
#             fig.update_layout(title="Patient Volume Heatmap")
#         elif button_id == "reset-btn":
#             # Return an empty figure to clear the plot
#             return go.Figure()

#     # Return the current figure if no button was clicked
#     return dash.no_update


@app.callback(
    Output("patient_volume_hm", "figure"),
    [Input("plot-btn", "n_clicks")],
    allow_duplicate=True
)
def generate_heatmap(n_clicks):
    if n_clicks:
        # Generate heatmap data
        data = [[0.1, 0.3, 0.5, 0.7, 0.9],
                [1, 0.8, 0.6, 0.4, 0.2],
                [0.2, 0, 0.5, 0.7, 0.9],
                [0.9, 0.8, 0.4, 0.2, 0],
                [0.3, 0.4, 0.5, 0.7, 1]]

        fig = go.Figure(data=go.Heatmap(z=data))
        fig.update_layout(title="Shmoo Heatmap")

        return fig

    # Return an empty figure if the button has not been clicked
    return go.Figure()


# @app.callback(
#     Output("patient_volume_hm", "figure"),
#     [Input("reset-btn", "n_clicks")],
#     allow_duplicate=True
# )
# def reset_plots(reset_clicks):
#     if reset_clicks:
#         # Return an empty figure to clear the plot
#         return go.Figure()

#     # Return the current figure if the button has not been clicked
#     return dash.no_update

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
