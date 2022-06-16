from typing import List

from dash import dcc
from data.external import set_df_f


def amp_range() -> dcc.RangeSlider:
    df = set_df_f()
    min_, max_ = df.dda50Amplitude.min(), df.dda50Amplitude.max()
    # mean_, std_ = df.dda50Amplitude.mean(), df.dda50Amplitude.std()
    return dcc.RangeSlider(
        min=0,
        max=max_,
        value=[min_, max_],
        id="amp-slider",
        allowCross=False,
        tooltip={"placement": "top", "always_visible": True},
    )


def sequence_y_dropdown() -> dcc.Dropdown:
    df = set_df_f()
    return dcc.Dropdown(
        df.Testpointsequencenumber_y.unique(),
        id="sequence-y-dropdown",
        placeholder="Select a Sequence Y",
        multi=True,
        searchable=False,
    )
