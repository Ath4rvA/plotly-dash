import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('mocksurvey.csv')


# Vertical

data_vertical = []

for col in df.columns[1:]:
    data_vertical.append(go.Bar(x=df['Unnamed: 0'], y=df[col], name=col))

layout = go.Layout(title="Mock Survey Results", title_x=0.5, barmode='stack')
fig = go.Figure(data=data_vertical, layout=layout)
pyo.plot(fig)

# Horizontal

data_horizontal = []

for col in df.columns[1:]:
    data_horizontal.append(
        go.Bar(y=df['Unnamed: 0'], x=df[col], name=col, orientation='h'))

layout = go.Layout(title="Mock Survey Results", title_x=0.5, barmode='stack')
fig = go.Figure(data=data_horizontal, layout=layout)
pyo.plot(fig)
