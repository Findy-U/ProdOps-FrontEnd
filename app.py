import os
from dash import Dash
import dash_bootstrap_components as dbc
from components.layouts.dashboard_layout import layout


css_path = os.path.join(os.path.dirname(__file__), 'assets/css/styles.css')

app = Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP, css_path])

app.layout = layout


if __name__ == '__main__':
    app.run_server(debug=True)
