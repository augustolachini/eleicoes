import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

app.layout = html.Div([
    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=[trace1, trace2],
                               layout=go.Layout(barmode='stack'))
              )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)