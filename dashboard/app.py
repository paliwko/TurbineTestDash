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
                dbc.Col(html.H5("Select Amplitude [micro in/in] range:")),
                dbc.Col(amp_range()),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.H5("Select Sequence Y:")),
                dbc.Col(sequence_y_dropdown()),
            ]
        ),
        dbc.Row(dbc.Col(scatter_top())),
        dbc.Row([dbc.Col(scatter_1()), dbc.Col(scatter_2())]),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(
        port=8066,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
