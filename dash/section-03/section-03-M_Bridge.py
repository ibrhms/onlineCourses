import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/FremontBridgeBicycles.csv')
df['Date'] = pd.to_datetime(df['Date'])

df['Hour'] = df['Date'].dt.time

df2 = df.groupby('Hour').sum()

trace1 = go.Bar (
    x=df2.index,
    y=df2['Fremont Bridge West Sidewalk'],
    name='Southbound',
    width=1
)

trace2 = go.Bar(
    x=df2.index,
    y=df2['Fremont Bridge East Sidewalk'],
    name='Northbound',
    width=1
)

data = [trace1, trace2]

layout = go.Layout (
    title='Fremont Bridge Bycycle Traffic by Hour',
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)