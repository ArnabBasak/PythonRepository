"""
In this file we will do analysis of swing bolwer James Anderson and Wasim Akram
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

wasim_data = pd.read_csv('wasim.csv')
james_data = pd.read_csv('anderson.csv')
glen_data = pd.read_csv('glen.csv')
waqar_data = pd.read_csv('waqar.csv')
app = dash.Dash()
app.layout = html.Div(children=[
        html.H1("Swing bowler Analysis"),
        dcc.Graph(id="Overs Bowled by individuals",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Overs,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Overs,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Overs,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Overs,'type':'bar','name':'Waqar Yonuis'},

                    ],
                    'layout':{
                    'title':"Overs bowled venus wise"
                    }
                }),
        dcc.Graph(id="Madiens Bowled by individuals",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Madiens,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Madiens,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Madiens,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Madiens,'type':'bar','name':'Waqar Yonuis'},
                    ],
                    'layout':{
                    'title':"Madiens bowled venus wise"
                    }
                }),
        dcc.Graph(id="Runs given by individuals",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Runs_Given,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Runs_Given,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Runs_Given,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Runs_Given,'type':'bar','name':'Waqar Yonuis'},
                    ],
                    'layout':{
                    'title':"Runs Given  venus wise"
                    }
                }),
        dcc.Graph(id="Wickets Taken by individuals",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Wickets_Taken,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Wickets_Taken,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Wickets_Taken,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Wickets_Taken,'type':'bar','name':'Waqar Yonuis'},

                    ],
                    'layout':{
                    'title':"Wickets Taken  venus wise"
                    }
                }),
        dcc.Graph(id="5 Wicket hauls individuals",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.four_wickets,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.four_wickets,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.four_wickets,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.four_wickets,'type':'bar','name':'Waqar Yonuis'},
                    ],
                    'layout':{
                    'title':"5 Wicket hauls individuals"
                    }
                }),
        dcc.Graph(id="Average",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Avg,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Avg,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Avg,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Avg,'type':'bar','name':'Waqar Yonuis'},
                    ],
                    'layout':{
                    'title':"Average"
                    }
                }),
        dcc.Graph(id="Strike_Rate",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Strike_Rate,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Strike_Rate,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Strike_Rate,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Strike_Rate,'type':'bar','name':'Waqar Yonuis'},

                    ],
                    'layout':{
                    'title':"Strike Rate"
                    }
                }),
        dcc.Graph(id="Econ Rate",
                figure={
                    'data':[
                    {'x':wasim_data.Venue,'y':wasim_data.Econ_Rate,'type':'bar','name':'Wasim Akram'},
                    {'x':james_data.Venue,'y':james_data.Econ_Rate,'type':'bar','name':'James Anderson'},
                    {'x':glen_data.Venue,'y':glen_data.Econ_Rate,'type':'bar','name':'Glen McGrath'},
                    {'x':waqar_data.Venue,'y':waqar_data.Econ_Rate,'type':'bar','name':'Waqar Yonuis'},
                    ],
                    'layout':{
                    'title':"Economy Rate"
                    }
                }),
])
if __name__ == "__main__":
    app.run_server(debug=True)
