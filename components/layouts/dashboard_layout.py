import dash_bootstrap_components as dbc
from .main_div_children import main_div_chidren


main_div = [
    # Dashboard #
    dbc.Container(
        fluid=True,
        children=main_div_chidren,
        className="header",
    ),
]


layout = dbc.Container(
    fluid=True,
    children=main_div,
    style={'font-family': 'Arial'}
)
