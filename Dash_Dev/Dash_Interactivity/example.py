import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../Data/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

app.layout = html.Div([dcc.Graph(id='graph'),
                       dcc.Dropdown(id='year-picker', options=year_options, value=df['year'].min())])


@app.callback(Output('graph', 'figure'), [Input('year-picker', 'value')]) # dcc.Graph has figure as argument where we pass the figure object. Hence the name here.
def update_fig(selected_year): # If any other word instead of figure then it wont work. Basically output of this function will be passed to html element having 'graph' as id

    # Dropdown option will be passed as argument to this function. It is selected by the Input part
    # as mentioned in callback decorator. Extract Html element which has id='year-picker' and get it's 'value' field

    filtered_df = df[df['year'] == selected_year]

    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']
                                      == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'], y=df_by_continent['lifeExp'],
            mode='markers', opacity=0.7, marker={'size': 15}, text=df_by_continent['country'], name=continent_name))

    layout = go.Layout(title='My Plot', title_x=0.5, xaxis={'title': 'GDP Per Cap', 'type': 'log'},  # Set logarithmic scale
                       yaxis={'title': 'Life Expectancy'})
    fig = go.Figure(data=traces, layout=layout)
    return fig


if __name__ == '__main__':
    app.run_server()
