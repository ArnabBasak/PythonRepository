import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.H1('Bar Chart'),
    html.Div('This is a Bar chart'),
    dcc.Graph(
        id = 'Sample-Graph',
        figure = {
            'data':[
                {'x':[5,6,7],'y':[12,15,18],'type':'bar','name':'First Chart'},
                {'x':[5,6,7],'y':[10,12,25],'type':'bar','name':'Second Chart'}
            ],
            'layout' : {
                'title' : 'Sample Bar Chart'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=4050)
