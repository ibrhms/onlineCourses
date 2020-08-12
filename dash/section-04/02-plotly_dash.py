import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 

import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([
    html.H1(
        children='Dash graph',
        style={
            'textAlign':'center'
        }
    ),

    dcc.Graph(
        id='scatter3',
        figure={
            'data':[
                go.Scatter(
                    x=random_x,
                    y=random_y,
                    mode='markers',
                    marker={
                        'size':12,
                        'color':'rgb(51,204,153',
                        'symbol':'pentagon',
                        'line':{'width':2}
                    }
                )
            ],
            'layout':go.Layout(
                title='Random Data Scatterplot',
                xaxis={'title':'Random x-values'},
                yaxis={'title':'Random y-values'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()