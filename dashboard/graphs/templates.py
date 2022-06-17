from typing import List

import plotly.express as px
import plotly.graph_objects as go
from dash import dcc
from data.external import set_df_f
from plotly.subplots import make_subplots


def scatter_top(amp_range_f: List[float] = None, seq_y_vals: List[int] = None):
    _df = set_df_f()
    if amp_range_f is not None:
        _df = _df.loc[_df.dda50Amplitude.between(*amp_range_f)]
    if seq_y_vals is not None:
        _df = _df.loc[_df.Testpointsequencenumber_y.isin(seq_y_vals)]

    scatter_fig = px.scatter(
            _df,
            x="r12_load_MW",
            y="dda50FrequencyHz",
            title="test",
            # colorscale="Inferno",
            # showscale=True
            hover_data=[
                "Tex_F",
                "r12_load_MW",
                "dda50Amplitude",
            ],
            height=700,
            color="dda50Amplitude",
            color_continuous_scale="Bluered",  # set color equal to a variable
        )
    scatter_fig.update_traces(marker={'size': 15})
    return dcc.Graph(
        id="scatter-top",
        figure=scatter_fig,
    )


def scatter_1(amp_range_f: List[float] = None, seq_y_vals: List[int] = None):
    _df = set_df_f()
    if amp_range_f is not None:
        _df = _df.loc[_df.dda50Amplitude.between(*amp_range_f)]
    if seq_y_vals is not None:
        _df = _df.loc[_df.Testpointsequencenumber_y.isin(seq_y_vals)]
    # Create figure with secondary y-axis

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=_df["TimeUTC"], y=_df["Speed1[Rpm]"], name="Speed"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=_df["TimeUTC"], y=_df["dda50Amplitude"], name="Amplitude"),
        secondary_y=True,
    )
    fig.update_layout(
        title_text="Dual axis scatter"
    )
    fig.update_xaxes(title_text="Time")
    fig.update_yaxes(title_text="Speed", secondary_y=False)
    fig.update_yaxes(title_text="Amplitude", secondary_y=True)
    fig.update_traces(dict(mode="markers"))


    return dcc.Graph(
        id="scatter-1",
        figure=fig
        # figure=px.scatter(
        #     _df,
        #     x="TimeUTC",
        #     y="r12_load_MW",
        #     color="dda50Amplitude",
        #     title="test",
        #     # colorscale="Inferno",
        #     color_continuous_scale="Bluered",
        #     # showscale=True
        #     hover_data=[
        #         "Tex_F",
        #         "r12_load_MW",
        #         "dda50Amplitude",
        #     ],
        # ),
    )


def scatter_2(amp_range_f: List[float] = None, seq_y_vals: List[int] = None):
    _df = set_df_f()
    if amp_range_f is not None:
        _df = _df.loc[_df.dda50Amplitude.between(*amp_range_f)]
    if seq_y_vals is not None:
        _df = _df.loc[_df.Testpointsequencenumber_y.isin(seq_y_vals)]
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
