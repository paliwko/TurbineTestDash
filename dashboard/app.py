from typing import List, Tuple

import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from dash import Dash, Input, Output, dcc, html
from plotly.subplots import make_subplots

from components.core import header
from components.filtering import amp_range, sequence_y_dropdown
from data.external import set_df_f
from graphs.templates import scatter_1, scatter_2, scatter_top

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

test_logo = "https://cdn-icons-png.flaticon.com/512/1875/1875654.png"


app.layout = dbc.Container(
    children=[
        header,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.H6("Select Amplitude [micro in/in] range:"), width=2),
                dbc.Col(amp_range(), width=5),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.H6("Select Sequence Y:"), width=2),
                dbc.Col(sequence_y_dropdown(), width=5),
            ]
        ),
        dbc.Row(dbc.Col(id="scatter-top-col", children=scatter_top())),
        dbc.Row(
            [
                dbc.Col(id="scatter-1-col", children=scatter_1()),
                dbc.Col(id="scatter-2-col", children=scatter_2()),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("scatter-top-col", "children"),
    Output("scatter-1-col", "children"),
    Output("scatter-2-col", "children"),
    Input("amp-slider", "value"),
    # Input("sequence_y_dropdown", "value"),
    prevent_initial_call=True,
)
def adjust_graphs(
    amp_range_f: List[float],
) -> Tuple[dcc.Graph, dcc.Graph, dcc.Graph]:
    return (
        scatter_top(amp_range_f),
        scatter_1(amp_range_f),
        scatter_2(amp_range_f),
    )


if __name__ == "__main__":
    app.run_server(
        port=8066,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
