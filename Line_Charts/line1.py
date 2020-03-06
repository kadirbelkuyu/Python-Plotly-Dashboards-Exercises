# -*- coding: utf-8 -*-

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(56)
x_values = np.linspace(0,1,100)
y_values = np.random(100)

trace1 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'markers',
    name = 'markers'
)
trace2 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'line+markers',
    name = 'line+markers'
)
trace3 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'lines',
    name = 'lines'
)

data = [trace1,trace2,trace3]
layout = go.Layout(
    title = 'Üç farklı modu gösteren çizgi grafiği'
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line1.html')

