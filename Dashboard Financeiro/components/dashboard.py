import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.dash_table.Format import Group
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd



#============ Layout ============#
layout = dbc.Col([
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([

                    ]),
                
                ])
            ])
        ])
])
