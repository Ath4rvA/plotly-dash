import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('mpg.csv')

# obj = go.Histogram(x=df['mpg'])  # default
obj = go.Histogram(x=df['mpg'], xbins=dict(
    start=0, end=50, size=4))  # start and end specify certain range of data you want. Size is size of bins
layout = go.Layout(title='mpg histogram', title_x=0.5)
fig = go.Figure(data=[obj], layout=layout)
pyo.plot(fig, filename='hist.html')
