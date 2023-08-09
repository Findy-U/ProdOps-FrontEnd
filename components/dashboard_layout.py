import dash_bootstrap_components as dbc
from .main_div_children import main_div_chidren
from .navbar import navbar
from .footer import footer

body = dbc.Container(
    fluid=True,
    children=main_div_chidren,
    className="header",
    style={
        'width': '100%',
    }
)

screen = [
    navbar,
    body,
    footer
]


layout = dbc.Container(
    fluid=True,
    children=screen,
    style={
        'font-family': 'Arial',
        'padding': '0',
    }
)
