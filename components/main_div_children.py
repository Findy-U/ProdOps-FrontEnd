from .checklist import checklist_filter
from helper_functions import helper_functions as hf
from dash import dcc, html
import dash_bootstrap_components as dbc


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
                           className="label1",
                           ),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-cat1",
                        clearable=False,
                        className="dropdown",
                        persistence=True,
                        persistence_type="session",
                        multi=True,
                    )
                ),
                html.Label("Categoria 2",
                           className="label1"),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-cat2",
                        clearable=False,
                        className="dropdown",
                        persistence=True,
                        persistence_type="session",
                        multi=True,
                    )
                )
            ]
        )
    ],
    className="card",
)

period_filter = dbc.Card(
    [
        dbc.CardHeader(
            html.H3("Período",
                    className="text-center",
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
    className="card",

)

# Graph
class_graph = "graph-container"

indicators = dbc.Col(
    [
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
                        "Work in Progress", hf.wip(DF_ind), ""),
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
    className="col-highlight-right",
    width=10
)

# Sidebar #
left_column = dbc.Col(
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
    className="col-highlight-left",
    width=2
)

main_div_chidren = dbc.Row(
    [left_column, indicators],
    className="row-highlight"
)
