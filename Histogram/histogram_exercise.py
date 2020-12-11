import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('abalone.csv')

hist_obj = go.Histogram(x=df.length, xbins=dict(start=0, end=1, size=0.02))

layout = go.Layout(title='Histogram of lengths.', title_x=0.5)

fig = go.Figure(data=[hist_obj], layout=layout)

pyo.plot(fig, filename='exercise.html')
