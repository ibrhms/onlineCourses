import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/mpg.csv')

data = [
    go.Histogram(
        x=df['mpg'],
        xbins=dict(start=8, end=50, size=6))
]

layout = go.Layout(
    title="<b> Miles per Gallon over <br>\
        1970's Era Vehicles</b>")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)