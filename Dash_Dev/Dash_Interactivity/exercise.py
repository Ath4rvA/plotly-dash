import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(
        id='my_slider',
        marks={i: i for i in range(-6, 7)},
        min=-6,
        max=6,
        value=[-1, 1]),
    html.Hr(),
    html.Div(id='result', children='value', style={'font-size': 25, 'text-align': 'center'})])


@app.callback(Output('result', 'children'), [Input('my_slider', 'value')])
def multiply(nums):
    return nums[0] * nums[1]


if __name__ == '__main__':
    app.run_server()
