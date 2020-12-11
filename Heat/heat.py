# Single heat map

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('2010SantaBarbaraCA.csv')

data = [go.Heatmap(x=df['DAY'], y=df['LST_TIME'],
                   z=df['T_HR_AVG'],
                   colorscale='temps')]
layout = go.Layout(title='Santa Barbara California Temps', title_x=0.5)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heat.html')
