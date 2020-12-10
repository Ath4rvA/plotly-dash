import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

x = np.linspace(0, 1, 100)
y = np.random.randn(100)

trace = go.Scatter(x=x, y=y, mode='markers', name='markers')
trace2 = go.Scatter(x=x, y=y - 5, mode='lines', name='linesonly')
trace3 = go.Scatter(x=x, y=y + 5, mode='lines+markers',
                    name='lines and markers')

data = [trace, trace2, trace3]

layout = go.Layout(title='lines chart')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, 'lines.html')
