from .checklist import checklist_filter
from helper_functions import helper_functions as hf
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd


# Cabeçalho
class_h3 = "text-center"

# Label
class_label1 = "label1"

# Card
class_card = "card"

# Divs e Cols
class_row = "row-highlight"
class_col = "col-highlight"

# Graph
class_graph = "graph-container"

# Dropdown
class_dropdown = "dropdown"

# Dados de exemplo
# df = pd.read_csv('ProdOps\database\Data.csv')
df = hf.extract_data()
print(df.head())

# Tratamento de Dados #

DF_main = hf.transform_data(df)

DF_ind = DF_main.copy()

DF_ind = hf.df_ind(DF_ind)

# Criação de Indicadores

DF_ind_pessoal = hf.df_ind_pessoal()

dropdown_filter = dbc.Card(
    [
        dbc.CardHeader(
            html.H3("Categorias"),
            style={"border-radius": "5px"}
        ),
        dbc.CardBody(
            [
                html.Label("Categoria 1",
                           className=class_label1,
                           ),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-cat1",
                        clearable=False,
                        className=class_dropdown,
                        persistence=True,
                        persistence_type="session",
                        multi=True,
                    )
                ),
                html.Label("Categoria 2",
                           className=class_label1),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-cat2",
                        clearable=False,
                        className=class_dropdown,
                        persistence=True,
                        persistence_type="session",
                        multi=True,
                    )
                )
            ]
        )
    ],
    className=class_card,
)

period_filter = dbc.Card(
    [
        dbc.CardHeader(
            html.H3("Período",
                    className=class_h3,
                    )
        ),
        dbc.CardBody(
            dcc.DatePickerRange(
                start_date="2023-01-01",
                end_date="2023-12-31",
                className="form-control",

            )
        )
    ],
    className=class_card,

)

indicators = dbc.Col(
    [
        # Cabeçalho #
        dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        "Desempenho",
                        className="text-center h1",
                    ),
                    width=10
                ),
                dbc.Col(
                    html.P(f"Última atualização: {pd.to_datetime('today').strftime('%Y-%m-%d')}",
                           className="text-p",
                           ),
                    width=2
                )
            ]

        ),

        # Valores únicos #
        dbc.Row(
            [
                dbc.Col(
                    hf.create_card(
                        "Productivity", hf.productivity(DF_ind_pessoal), ""),
                    width=3
                ),
                dbc.Col(
                    hf.create_card(
                        "Batata", hf.productivity(DF_ind_pessoal), ""),
                    width=3
                ),
                dbc.Col(
                    hf.create_card(
                        "WIP (Work in Progress)", hf.wip(DF_ind), ""),
                    width=3
                ),
                dbc.Col(
                    hf.create_card(
                        "Stale Work", hf.stale_work(DF_ind), ""),
                    width=3
                )
            ],
            className="information-row",
            justify="center",
            align="center",
        ),

        # Gráficos Superiores #
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(figure=hf.plot_histogram_status(DF_main),
                                  className=class_graph,
                                  )
                    ],
                    width=6
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure=hf.plot_histogram_status(DF_main),
                                  className=class_graph,
                                  )
                    ],
                    width=6,
                )
            ]
        ),

        # Gráficos Inferiores #
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(
                            figure=hf.plot_histogram_blocked_vs_unblocked(
                                DF_main),
                            className=class_graph,
                        )
                    ],
                    width=6
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            figure=hf.plot_histogram_blocked_vs_unblocked(
                                DF_main),
                            className=class_graph,
                        )
                    ],
                    width=6
                )
            ]
        )

    ],
    className=class_col,
    width=10
)

main_div_chidren = [
    dbc.Row(
        [
            # Sidebar #
            dbc.Col(
                [
                    dbc.Button(
                        "Atualizar",
                        id="Atualizar",
                        className="button",
                    ),
                    dropdown_filter,
                    checklist_filter,
                    period_filter
                ],
                className=class_col,
                width=2
            ),
            indicators
        ],
        className=class_row
    )
]
