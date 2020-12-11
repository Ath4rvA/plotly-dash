import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('mpg.csv')

obj = go.Scatter(x=df.displacement, y=df.acceleration, text=df.name, mode='markers', marker=dict(
    size=(df.weight) / 100,
    color=df.cylinders,
    showscale=True
))

layout = go.Layout(title="displacement vs acceleration", title_x=0.5, xaxis=dict(title='Displacement'),
                   yaxis=dict(title='Acceleration'))
fig = go.Figure(data=[obj], layout=layout)

pyo.plot(fig, filename='bubble.html')
