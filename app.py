import os
from dash import Dash
import dash_bootstrap_components as dbc
from components.layouts.dashboard_layout import layout

# Obtém o caminho completo para o arquivo styles.css
css_path = os.path.join(os.path.dirname(__file__), 'assets/css/styles.css')

# Criação do aplicativo Dash
app = Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP, css_path])

# Layout do dashboard
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
