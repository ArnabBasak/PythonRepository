"""
In this file we will analyse the spin bowling greats in the 90s
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

anil_data = pd.read_csv('anil.csv')
shane_data = pd.read_csv('shane.csv')
murli_data = pd.read_csv('murli.csv')
overall_data = pd.read_csv('overall.csv')

#print(anil_data.columns)
#print(anil_data.Runs_Conscided)
app = dash.Dash()
app.layout = html.Div(children=[
        html.H1("Spin bowler Analysis"),
        dcc.Graph(id="Overs Bowled by individuals",
                figure={
                    'data':[
                    {'x':anil_data.Year,'y':anil_data.Overs,'type':'bar','name':'Anil Kumble'},
                    {'x':shane_data.Year,'y':shane_data.Overs,'type':'bar','name':'Shane Warne'},
                    {'x':murli_data.Year,'y':murli_data.Overs,'type':'bar','name':'Murli'},
                    ],
                    'layout':{
                    'title':"Overs bowled over the years"
                    }
                }),
            dcc.Graph(id="Maidens Bowled by individuals",
                    figure={
                        'data':[
                        {'x':anil_data.Year,'y':anil_data.Maiden,'type':'bar','name':'Anil Kumble'},
                        {'x':shane_data.Year,'y':shane_data.Maiden,'type':'bar','name':'Shane Warne'},
                        {'x':murli_data.Year,'y':murli_data.Maiden,'type':'bar','name':'Murli'},
                        ],
                        'layout':{
                        'title':"Maidens bowled over the years"
                        }
                    }),
                dcc.Graph(id="Runs Consided Bowled by individuals",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.Runs_Conscided,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.Runs_Conscided,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.Runs_Conscided,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"Runs Consided over the years"
                            }
                        }),
                dcc.Graph(id="Wickets Taken by individuals",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.Wickets_Taken,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.Wickets_Taken,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.Wickets_Taken,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"Wickets Taken over the years"
                            }
                        }),
                dcc.Graph(id="Five wicket hauls",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.five_Wickets,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.five_Wickets,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.five_Wickets,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"5 for Taken over the years"
                            }
                        }),
                dcc.Graph(id="ten wicket hauls",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.ten_Wickets,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.ten_Wickets,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.ten_Wickets,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"10 for Taken over the years"
                            }
                        }),
                dcc.Graph(id="Average",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.Avg,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.Avg,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.Avg,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"Bowling average over the years"
                            }
                        }),
                dcc.Graph(id="Strike_Rate",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.Strike_Rate,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.Strike_Rate,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.Strike_Rate,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"Strike Rate  over the years"
                            }
                        }),
                dcc.Graph(id="Econ_Rate",
                        figure={
                            'data':[
                            {'x':anil_data.Year,'y':anil_data.Econ_Rate,'type':'bar','name':'Anil Kumble'},
                            {'x':shane_data.Year,'y':shane_data.Econ_Rate,'type':'bar','name':'Shane Warne'},
                            {'x':murli_data.Year,'y':murli_data.Econ_Rate,'type':'bar','name':'Murli'},
                            ],
                            'layout':{
                            'title':"Economy Rate  over the years"
                            }
                        }),
])
if __name__ == "__main__":
    app.run_server(debug=True)
