import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('../../Data/OldFaithful.csv')

scatter_obj = go.Scatter(x=df.X, y=df.Y, mode='markers',
                         name='OldFaithful', marker={'size': 6})

layout = go.Layout(title='Old Faithful Eruption Intervals vs Durations', title_x=0.5,
                   xaxis={'title': 'Duration of Eruption (minutes)'}, yaxis={'title': 'Interval to next Eruption (minutes)'})

fig = go.Figure(data=[scatter_obj], layout=layout)

app = dash.Dash()

app.layout = html.Div(dcc.Graph(id='Old Faithful', figure=fig))

app.run_server()
