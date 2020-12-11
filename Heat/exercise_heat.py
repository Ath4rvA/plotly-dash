# heat map of year and month passenger count

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('flights.csv')

obj = go.Heatmap(x=df['year'], y=df['month'],
                 z=df['passengers'], colorscale='jet')

layout = go.Layout(title='Monthly passengers by year', title_x=0.5)

fig = go.Figure(data=[obj], layout=layout)
pyo.plot(fig, filename='exercise_heat.html')
