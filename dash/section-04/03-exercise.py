import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 

import pandas as pd 
import os

app = dash.Dash()

csv_file = '../Data/OldFaithful.csv'
cur_dir = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(os.path.join(cur_dir, csv_file))

app.layout = html.Div([
    html.H1(
        children = 'Old Faithful',
        style = {'textAlign':'center'}
    ),

    dcc.Graph(
        id='Old Faithful',
        figure={
            'data':[
                go.Scatter(
                    x=df['X'],
                    y=df['Y'],
                    mode='markers',
                    marker={
                        'size':12,
                        'symbol':'rgb(51,124,10)'
                    }
                )
            ],
            'layout':go.Layout(
                title='Old Faithful Scatterplot',
                xaxis={'title':'Duration'},
                yaxis={'title':'Waiting Time'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()