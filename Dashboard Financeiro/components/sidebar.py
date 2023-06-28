import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


#============ Layout ============#

layout = dbc.Col([
            html.H1("My Budget", className="primary-text"),
            html.P("By Eric", className="info-text"),
            html.Hr(),

#====== Selecao de perfil ======#
            dbc.Button(id='button-avatar',
                children=[html.Img(src='/assets/img_hom.png',id='avatar_change', alt='Avatar', className='perfil_avatar',),
            ], style={'background-color':'transparent', 'border-color':'transparent'}),




#====== Seção Novo ======#

            dbc.Row([
                dbc.Col([
                    dbc.Button(color="success", id="open-novo-receita",
                            children=["+ Receita"]),
                ], width=6),

                dbc.Col([
                    dbc.Button(color="danger", id="open-novo-despesa",
                            children=["+ Despesa"]),
                ], width=6)
            ]),
#====== Modal Receita ======#
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                           dbc.Label('Descrição'),
                           dbc.Input(placeholder="Ex.: divedendos da bolsa, herança...", id="txt-receita"),

                        ], width=6),
                        dbc.Col([
                            dbc.Label("Valor: "),
                            dbc.Input(placeholder="R$100.00", id="valor_receita", value="")
                        ], width=6)
                    ]),
                    dbc.Col([
                        dbc.Label('Data: '),
                        dcc.DatePickerSingle(id='date-receitas',
                            min_date_allowed=date(2023,1,1),
                            max_date_allowed=date(2030,12,31),
                            date=datetime.today(),
                            style={"width": "100%"})
                    ], width=4),

                    dbc.Col([
                        dbc.Label("Extras"),
                        dbc.Checklist(
                            options=[],
                            value=[],
                            id='swiches-input-receitas',
                            switch=True
                        )
                    ],width=4),

                    dbc.Col([
                        html.Label('Categoria da Receita'),
                        dbc.Select(id='select_receita', options=[],value=[])
                    ],width=4)
                ],style={"margin-top": "25px"}),

                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend("Adicionar categoria", style={'color': 'green'}),
                                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                                    html.Br(),
                                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                                    html.Br(),
                                                    html.Div(id="category-div-add-receita", style={}),
                                ],width=6),
                                dbc.Col([
                                    html.Legend("Excluir categorias", style={'color': 'red'}),
                                    dbc.Checklist(
                                        id='checklist-receita',
                                        options=[],
                                        value=[],
                                        label_checked_style={'color': 'red'},
                                        input_checked_style={'color': 'blue', 'borderColor': 'orange'}
                                    ),
                                    dbc.Button("Remover", color='warning', id='remover-caregoria-receita', style={'margin-top': '20px'}),
                                ],width=6)
                            ])
                        ], title='Adicionar/Remover Categorias')
                    ], flush=True, start_collapsed=True, id='accordion-receita')
                ])

            ], id='modal-novo-receita'),


#====== Modal Despesa ======#
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
                dbc.ModalBody([

                ])
            ],id='modal-novo-despesa'),


#====== Seção Nav ======#
            html.Hr(),
            dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
                dbc.NavLink("Extratos", href="/extratos", active="exact"),
            ], vertical=True,pills=True, id='nav_buttons',style={"margin-botton" : "50px"}),


],id="sidebar_completa")





#======  Callbacks  ======#
#PopUp Receitas
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

#PopUp Despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open