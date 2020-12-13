import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': '#f7ee82', 'text': '#7FDBFF', 'plot_bg': '#2fe8a8', 'paper': '#cbeae2',
          'plot_font_color': '#194dce'}

app.layout = html.Div(children=[html.H1("Hello, Dash!", style={'textAlign': 'center',
                                                               'color': colors['text']}),  # Header settings
                                html.Div('Dash: Web Dashboards with Python!'),
                                dcc.Graph(id='example', figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y':[4, 1, 2],
                                            'type':'bar', 'name':'SF'},
                                        {'x': [1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'NYC'}],
                                    'layout':{'title': 'Bar Plots!',
                                              # area on which chart is there
                                              'plot_bgcolor': colors['plot_bg'],
                                              # area outside chart but part of dboard
                                              'paper_bgcolor': colors['paper'],
                                              'font':{'color': colors['plot_font_color'],
                                                      'size': 24}}  # font color and size of text present in chart
                                })], style={'backgroundColor': colors['background']})  # Rest of div settings where dboard doesn't occupy

if __name__ == '__main__':
    app.run_server()
