from typing import List, Tuple

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from dash import Dash, Input, Output, dash_table, dcc, html
from plotly.subplots import make_subplots

from components.core import header
from components.filtering import amp_range, sequence_y_dropdown
from data.external import filter_data, set_df_f
from graphs.templates import scatter_1, scatter_top

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

test_logo = "https://cdn-icons-png.flaticon.com/512/1875/1875654.png"


app.layout = dbc.Container(
    children=[
        header,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.H5("Select Amplitude [micro in/in] range:"), width=2),
                dbc.Col(amp_range(), width=5),
                dbc.Col(width=3),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.H5("Select Sequence Y:"), width=2),
                dbc.Col(sequence_y_dropdown(), width=5),
                dbc.Col(width=2),
                dbc.Col(
                    dbc.Button(
                        "Reset selection",
                        color="warning",
                        className="me-1",
                        href="/",
                        external_link=True,
                        id="reset-selection",
                    ),
                    width=3,
                    align="right",
                ),
            ]
        ),
        dbc.Row(dbc.Col(id="scatter-top-col", children=scatter_top())),
        dbc.Row(
            [
                dbc.Col(id="scatter-1-col", children=scatter_1()),
                # dbc.Col(id="scatter-2-col", children=scatter_2()),
            ]
        ),
        dbc.Row(
            dbc.Col(
                dash_table.DataTable(
                    data=set_df_f().to_dict("records"),
                    columns=[{"name": i, "id": i} for i in set_df_f().columns],
                    page_action="native",
                    page_current=0,
                    page_size=10,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    id="text-data",
                )
            )
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("scatter-top-col", "children"),
    Output("scatter-1-col", "children"),
    # Output("scatter-2-col", "children"),
    Input("amp-slider", "value"),
    Input("sequence-y-dropdown", "value"),
    prevent_initial_call=True,
)
def adjust_graphs(
    amp_range_f: List[float], seq_y_vals: List[int]
) -> Tuple[dcc.Graph, dcc.Graph, dcc.Graph]:
    print(seq_y_vals)
    return (
        scatter_top(amp_range_f, seq_y_vals),
        scatter_1(amp_range_f, seq_y_vals),
        # scatter_2(amp_range_f, seq_y_vals),
    )


@app.callback(
    Output("text-data", "data"),
    Input("sequence-y-dropdown", "value"),
    prevent_initial_call=True,
)
def adjust_table(amp_range_f: List[float], seq_y_vals: List[int]) -> str:
    df = set_df_f()
    df = filter_data(df, amp_range_f, seq_y_vals)
    return df.to_dict("records")


# @app.callback(
#    Output("sequence-y-dropdown", "value"),
#    Input("sequence-y-dropdown", "options"),
#    prevent_initial_call=True,
# )
# def callback(value):
#    return ""


# @app.callback(
#    Output("sequence-y-dropdown", "value"), Input("reset-selection", "n_clicks")
# )
# def dropdown_callback(n_clicks):
#    return n_clicks["none"]


if __name__ == "__main__":
    app.run_server(
        port=8067,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
