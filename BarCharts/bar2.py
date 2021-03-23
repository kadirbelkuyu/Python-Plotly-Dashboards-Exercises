import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/2018WinterOlympics.csv')

trace1 = go.Bar(
    x=df['NOC'],  
    y=df['Gold'],
    name = 'Gold',
    marker=dict(color='#FFD700')
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker=dict(color='#9EA0A1') 
)
trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker=dict(color='#CD7F32') 
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar2.html')
