import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='all', #adding all original data points
        jitter=0.1, #density of data points
        pointpos=1.5
    ),
    go.Box(
        y=y,
        boxpoints='outliers'
    )
]

layout = go.Layout(title = 'outliers plot')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)