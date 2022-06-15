from typing import List

import plotly.express as px
from dash import dcc
from data.external import set_df_f
from plotly.subplots import make_subplots


def scatter_top() -> dcc.Graph:
    return dcc.Graph(
        id="scatter-top",
        figure=px.scatter(
            set_df_f(),
            x="r12_load_MW",
            y="dda50FrequencyHz",
            color="dda50Amplitude",
            title="test",
            # colorscale="Inferno",
            color_continuous_scale="Bluered",
            # showscale=True
            hover_data=[
                "Tex_F",
                "r12_load_MW",
                "dda50Amplitude",
            ],
        ),
    )


def scatter_1() -> dcc.Graph:
    return dcc.Graph(
        id="scatter-1",
        figure=px.scatter(
            set_df_f(),
            x="TimeUTC",
            y="r12_load_MW",
            color="dda50Amplitude",
            title="test",
            # colorscale="Inferno",
            color_continuous_scale="Bluered",
            # showscale=True
            hover_data=[
                "Tex_F",
                "r12_load_MW",
                "dda50Amplitude",
            ],
        ),
    )


def scatter_2() -> dcc.Graph:
    return dcc.Graph(
        id="scatter-2",
        figure=px.scatter(
            set_df_f(),
            x="TimeUTC",
            y="Speed1[Rpm]",
            color="dda50Amplitude",
            title="test",
            # colorscale="Inferno",
            color_continuous_scale="Bluered",
            # showscale=True
            hover_data=[
                "Tex_F",
                "r12_load_MW",
                "dda50Amplitude",
            ],
        ),
    )
