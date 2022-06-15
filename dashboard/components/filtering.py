from dash import dcc
from data.external import set_df_f


def amp_range() -> dcc.RangeSlider:
    df = set_df_f()
    min_, max_ = df.dda50Amplitude.min(), df.dda50Amplitude.max()
    # mean_, std_ = df.dda50Amplitude.mean(), df.dda50Amplitude.std()
    return dcc.RangeSlider(min=0, max=max_, step=1, value=[min_, max_], id="amp-slider")


def sequence_y_dropdown() -> dcc.Dropdown:
    df = set_df_f()
    return dcc.Dropdown(
        df.Testpointsequencenumber_y.unique(),
        id="sequence_y_dropdown",
        placeholder="Select a Sequence Y",
        multi=True,
        searchable=False,
    )
