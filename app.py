
## First Example

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    html.Div([
        html.H1(children='Hello World'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [10, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        ),

    ])
)

@app.callback(dash.dependencies.Output('example-graph', 'children'),
              [dash.dependencies.Input('dropdown', 'value')]))
if __name__ == '__main__':
    app.run_server(debug=True)