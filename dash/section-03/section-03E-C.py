import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/mpg.csv')

print(df.columns)

data = [go.Scatter(
    x = df['cylinders'],
    y = df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(
        size=df['weight']/400, 
        color=df['horsepower'],
        showscale=True)
     )]

layout = go.Layout(title='my Bubble', hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)