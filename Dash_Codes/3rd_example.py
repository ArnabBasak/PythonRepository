"""
In this example we will create charts based on user input and dynamic data
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015,1,1)
end = datetime.datetime.now()
stocks = 'TSLA'
df = web.DataReader(stocks,'yahoo',start,end)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('OMG finance'),
    dcc.Graph(id='Example',
                 figure={
                     'data': [
                         {'x':df.index,'y':df.Close,'type':'line','name':stocks},
                     ],
                     'layout':{
                         'title':stocks
                     }
                 })

])

if __name__ == '__main__':
    app.run_server(debug=True)
