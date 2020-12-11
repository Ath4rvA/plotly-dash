import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('abalone.csv')

sample_1 = np.random.choice(df.rings, 100, replace=False)
sample_2 = np.random.choice(df.rings, 150, replace=False)

box_obj_1 = go.Box(y=sample_1, name='sample_1', boxpoints='outliers')
box_obj_2 = go.Box(y=sample_2, name='sample_2', boxpoints='outliers')

data = [box_obj_1, box_obj_2]

layout = go.Layout(title="comparison", title_x=0.5)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='box.html')
