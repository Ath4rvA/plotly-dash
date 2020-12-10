import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(100)

x = np.random.randint(0, 101, 50)
y = np.random.randint(0, 101, 50)

obj = go.Scatter(x=x, y=y, mode='markers', marker=dict(
    size=12,
    color='rgb(51,204,153)',
    symbol='circle'), line=dict(width=2))

data = [obj]

layout = go.Layout(title='x vs y scatter', xaxis=dict(
    title='x-axis'), yaxis=dict(title='y-axis'), hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, 'scatter.html')
