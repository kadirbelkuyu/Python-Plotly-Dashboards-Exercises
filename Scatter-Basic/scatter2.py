
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]
layout = go.Layout(
    title = 'Random Data Scatterplot', 
    xaxis = dict(title = 'Some random x-values'), 
    yaxis = dict(title = 'Some random y-values'), 
    hovermode ='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter2.html')
