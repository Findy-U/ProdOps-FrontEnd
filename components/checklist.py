import dash_bootstrap_components as dbc
from dash import html

checklist_filter = dbc.Card(
    [
        dbc.CardHeader(
            html.H3("Opções",
                    className="text-center",
                    )
        ),
        dbc.CardBody(
            dbc.RadioItems(
                options=[
                    {"label": "Opção 1",
                     "value": "opcao1"},
                    {"label": "Opção 2",
                     "value": "opcao2"},
                    {"label": "Opção 3",
                     "value": "opcao3"}
                ],
                value="opcao1"
            )
        )
    ],
    className="card",
)
