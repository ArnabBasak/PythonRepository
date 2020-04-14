"""
In this file we will perfom some EDA on the cricket records using dash application
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

sachin_data = pd.read_csv('sachin.csv')
virat_data = pd.read_csv('virat.csv')
rohit_data = pd.read_csv('rohit.csv')

app = dash.Dash()
app.layout = html.Div(children=[
        html.H1("ODI Runs analysis"),
        dcc.Graph(id="Sachin_Record",
                figure={
                    'data':[
                    {'x':sachin_data.Year,'y':sachin_data.Runs,'type':'bar','name':'runs'},
                    ],
                    'layout':{
                    'title':"Sachin's ODI Runs"
                    }
                }),
        dcc.Graph(id="Virat_Record",
                figure={
                    'data':[
                    {'x':virat_data.Year,'y':virat_data.Runs,'type':'bar','name':'runs'},
                    ],
                    'layout':{
                    'title':"Virat's ODI Runs"
                    }
                }),
        dcc.Graph(id="Rohit_Record",
                figure={
                    'data':[
                    {'x':rohit_data.Year,'y':rohit_data.Runs,'type':'bar','name':'runs'},
                    ],
                    'layout':{
                    'title':"Rohit's ODI Runs"
                    }
                }),
        dcc.Graph(id="compare",
                figure={
                    'data':[
                    {'x':rohit_data.Year,'y':rohit_data.Runs,'type':'line','name':'Rohit Sharma'},
                    {'x':virat_data.Year,'y':virat_data.Runs,'type':'line','name':'Virat Kohli'},
                    ],
                    'layout':{
                    'title':"Virat Kohli Rohit sharma's comparision"
                    }
                }),
])
if __name__ == "__main__":
    app.run_server(debug=True)
