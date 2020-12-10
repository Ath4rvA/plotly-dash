import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('nst-est2017-alldata.csv')

df2 = df[df.DIVISION == '1']
df2.set_index('NAME', inplace=True)

population_columns = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[population_columns]

data = [go.Scatter(x=df2.columns, y=df2.loc[name],
                   mode='lines+markers', name=name) for name in df2.index]

layout = go.Layout(title="Population Trend", xaxis=dict(
    title='Year'), yaxis=dict(title='Count'))

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, 'population.html')
