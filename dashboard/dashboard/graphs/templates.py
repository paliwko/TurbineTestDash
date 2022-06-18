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
        color_continuous_scale="Turbo",  # set color equal to a variable
    )
    scatter_fig.update_traces(marker={"size": 20})
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
    fig.add_trace(
        go.Scatter(x=_df["TimeUTC"], y=_df["r12_load_MW"], name="Load"),
        secondary_y=False,
    )

    fig.update_layout(title_text="Dual axis scatter")
    fig.update_xaxes(title_text="Time")
    fig.update_yaxes(title_text="Speed", secondary_y=False)
    fig.update_yaxes(title_text="Amplitude", secondary_y=True)
    fig.update_traces(dict(mode="markers"))
    fig.update_layout(height=700)
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99))

    return dcc.Graph(
        id="scatter-1",
        figure=fig

    )


def scatter_2(amp_range_f: List[float] = None, seq_y_vals: List[int] = None):
    _df = set_df_f()
    if amp_range_f is not None:
        _df = _df.loc[_df.dda50Amplitude.between(*amp_range_f)]
    if seq_y_vals is not None:
        _df = _df.loc[_df.Testpointsequencenumber_y.isin(seq_y_vals)]
    # Create figure with secondary y-axis

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=_df["TimeUTC"], y=_df["r12_load_MW"], name="Speed"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=_df["TimeUTC"], y=_df["dda50Amplitude"], name="Amplitude"),
        secondary_y=True,
    )
    fig.update_layout(title_text="Dual axis scatter")
    fig.update_xaxes(title_text="Time")
    fig.update_yaxes(title_text="Load", secondary_y=False)
    fig.update_yaxes(title_text="Amplitude", secondary_y=True)
    fig.update_traces(dict(mode="markers"))

    return dcc.Graph(id="scatter-2", figure=fig)


