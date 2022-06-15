import dash_bootstrap_components as dbc
from dash import html

test_logo = "https://cdn-icons-png.flaticon.com/512/1875/1875654.png"
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=test_logo, height="100")),
                    dbc.Col(
                        dbc.NavbarBrand("Turbine Test Data Reviewer", className="ms-2")
                    ),
                ],
                align="center",
                className="g-0",
            ),
        ]
    ),
    color="light",
    dark=False,
)
