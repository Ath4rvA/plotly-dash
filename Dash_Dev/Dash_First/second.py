import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

np.random.seed(42)

x = np.random.randint(1, 101, 100)
y = np.random.randint(1, 101, 100)

scatter_1 = go.Scatter(x=x, y=y, mode='markers', name='Scatter_1', marker={
    'size': 12,
    'symbol': 'pentagon',
    'line': {'width': 2}}
)


scatter_2 = go.Scatter(x=x, y=y, mode='markers', name='Scatter_2', marker={
    'size': 12,
    'symbol': 'circle',
    'line': {'width': 2},
    'color': '#ffb7cd'}
)

layout_1 = go.Layout(title='Scatter Plot 1',
                     title_x=0.5, plot_bgcolor='#24ecad')
fig_1 = go.Figure(data=[scatter_1], layout=layout_1)

layout_2 = go.Layout(title='Scatter Plot 2',
                     title_x=0.5, plot_bgcolor='#f9f7f3')
fig_2 = go.Figure(data=[scatter_2], layout=layout_2)


app = dash.Dash()
app.layout = html.Div([dcc.Graph(id='scatter_1', figure=fig_1),
                       dcc.Graph(id='scatter_2', figure=fig_2)])
app.run_server()
