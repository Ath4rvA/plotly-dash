import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

df1 = pd.read_csv('2010SitkaAK.csv')
df2 = pd.read_csv('2010SantaBarbaraCA.csv')
df3 = pd.read_csv('2010YumaAZ.csv')

trace_1 = go.Heatmap(x=df1['DAY'], y=df1['LST_TIME'], z=df1['T_HR_AVG'],
                     zmin=5, zmax=40)

trace_2 = go.Heatmap(x=df2['DAY'], y=df2['LST_TIME'], z=df2['T_HR_AVG'],
                     zmin=5, zmax=40)

trace_3 = go.Heatmap(x=df3['DAY'], y=df3['LST_TIME'], z=df3['T_HR_AVG'],
                     zmin=5, zmax=40)

fig = tools.make_subplots(rows=1, cols=3, subplot_titles=(
    'Sitka AK', 'SB Cali', 'Yuma AZ'), shared_yaxes=True)

fig.append_trace(trace_1, 1, 1)  # trace, row, col. We have 1 row 3 cols
fig.append_trace(trace_2, 1, 2)
fig.append_trace(trace_3, 1, 3)

fig['layout'].update(title='Compare Heat Maps')

pyo.plot(fig, filename='multiple_heat.html')
