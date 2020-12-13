import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../Data/mpg.csv')

app = dash.Dash()

app.layout = html.Div([
    html.Div(dcc.Dropdown(id='xaxis', options=[{'label': i, 'value': i} for i in df.columns], value='mpg'),
             style={'width': '48%', 'display': 'inline-block'}),
    html.Div(dcc.Dropdown(id='yaxis', options=[{'label': i, 'value': i} for i in df.columns], value='mpg'),
             style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='plot')]
)


@app.callback(Output('plot', 'figure'), [Input('xaxis', 'value'), Input('yaxis', 'value')])
def update_fig(xaxis, yaxis):

    data = [go.Scatter(x=df[xaxis], y=df[yaxis], text=df['name'], mode='markers', name='scatter',
                       marker={'size': 15, 'opacity': 0.5, 'line': {'width': 0.3, 'color': 'red'}})]
    layout = go.Layout(title='Scatter', title_x=0.5, xaxis={
                       'title': xaxis}, yaxis={'title': yaxis})
    fig = go.Figure(data=data, layout=layout)
    return fig


if __name__ == '__main__':
    app.run_server()
