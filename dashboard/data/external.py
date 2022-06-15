import glob

import pandas as pd
import plotly.express as px

# --
import plotly.graph_objects as go
import seaborn as sns
from dash import Dash, Input, Output, dcc, html

# --

# file1_ = open("sensor_1.csv", "r")
# lines = file1_.readlines()
# cnt = 0
# for i in range(0, len(lines)):
#     if lines[i].find("Scan Number") != -1:
#         cnt = i
#         break

# df1 = pd.read_csv("sensor_1.csv", sep=",", header=cnt)

# df1.columns = df1.columns.str.replace(" ", "")

# file2_ = open("run_data.csv", "r")
# lines = file2_.readlines()
# cnt2 = 0
# for i in range(0, len(lines)):
#     if lines[i].find("Date") != -1:
#         cnt2 = i
#         break

# df2 = pd.read_csv("run_data.csv", sep=",", header=cnt2 - 1)
# print(df2.columns)

# df2.columns = df2.columns.str.replace(" ", "", "  ", "")

# df1.rename(columns={"Testmantime(UTC)": "TimeUTC"}, inplace=True)
# df2.rename(columns={"Time(UTC)": "TimeUTC"}, inplace=True)

# set_df = pd.merge_asof(df1, df2, on="TimeUTC")
# set_df.sort_values("dda_50Amplitude", ascending=True, inplace=True)

# # data exploration
# -----------------------------------------------------------------
# print(set_df[:5])
# print(sorted(set_df.Testpointidentification_y.unique()))
# print(set_df.columns)
# data Viz

# fig_scatter = px.scatter(
#    data_frame=set_df, x="TimeUTC", y="dda_50Frequency[Hz]", color="dda_50Amplitude"
# )
# fig_scatter.show()


df1 = pd.read_csv(
    r"E:/Pauli/Podyplom/IWD/turbine_test_dash/dashboard/data/data_raw.csv",
    encoding="latin-1",
)
df1.columns = df1.columns.str.replace(" ", "")
set_df = df1
set_df.sort_values("dda50Amplitude", ascending=True, inplace=True)

# set_df.reset_index(drop=True['TimeUTC'] = pd.to_datetime(set_df.reset_index(drop=True['TimeUTC'], unit='s', errors='coerce')))


def set_df_f() -> pd.DataFrame:
    return set_df


# print(set_df.dtypes)
