import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Read data

df = pd.read_csv('2010YumaAZ.csv')
df.set_index('DAY', inplace=True)

data = []
# data.append([go.Scatter(x=df['LST_TIME'], y=df.loc[name, 'T_HR_AVG'],
#                         mode='lines', name=name) for name in df.index])

for day in df.index.unique():
    trace = go.Scatter(x=df.loc[day, 'LST_TIME'], y=df.loc[day,
                                                           'T_HR_AVG'], mode='lines+markers', name=day)

    data.append(trace)

print(data[0])

layout = go.Layout(
    title="Daily temperatures from June 1-7, 2010 in Yuma, Arizona", title_x=0.5)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, 'exercise.html')
