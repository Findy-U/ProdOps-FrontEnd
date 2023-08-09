import dash_bootstrap_components as dbc
from dash import html, get_asset_url

img = html.Img(src='assets/logo.svg')

text = html.P()

navbar = dbc.Navbar([
    img,
],
    style={
        "background-color": "#333333",
        "height": "50px"
}
)
