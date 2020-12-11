# Compare petal length distribution of each class

import plotly.graph_objs as go
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

df = pd.read_csv('iris.csv')
setosa = df['petal_length'][df['class'] == 'Iris-setosa']
versicolor = df['petal_length'][df['class'] == 'Iris-versicolor']
virginica = df['petal_length'][df['class'] == 'Iris-virginica']
classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
fig = ff.create_distplot([setosa, versicolor, virginica],
                         classes, bin_size=[.2, .2, .2])
pyo.plot(fig, filename='exercise.html')
