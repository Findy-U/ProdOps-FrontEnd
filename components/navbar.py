import dash_bootstrap_components as dbc
from dash import html

img = html.Img(
    src='assets/logo.svg',
    style={
        "width": "15vw",
        "padding-left": "19px"
    })

text = html.P(
    children="Dashboard",
    style={
        "color": "white",
        "align-self": "center",
        "margin": "auto",
        "font-size": "2.9vw"
    })

navbar = dbc.Navbar([
    img,
    text
],
    color="#1e1e1e",
    dark=True,
    style={
        "border-bottom": "4px solid #03887d",
        "padding": "9px"}
)
