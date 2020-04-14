import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

mapbox_access_token = 'pk.eyJ1IjoiZ2lsdHJhcG8iLCJhIjoiY2o4eWJyNzY4MXQ1ZDJ3b2JsZHZxb3N0ciJ9.MROnmydnXtfjqjIBtC-P5g'

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id = "mapbox",
            figure={
                "data": [
                    dict(
                        type = "scattermapbox",
                        lat = ["45.5017", "46.829853"],
                        lon = ["-73.5673", "-71.254028"],
                        mode = "markers",
                        marker = dict(size = 14),
                        text = ["Montreal", "Quebec"])
                ],
                'layout': dict(
                    autosize = True,
                    hovermode = "closest",
                    margin = dict(l = 0, r = 0, t = 0, b = 0),
                    mapbox = dict(
                        accesstoken = mapbox_access_token,
                        bearing = 0,
                        center = dict(lat = 45, lon = -73),
                        pitch = 0,
                        zoom = 5
                    )
                )
            },
            style = {"height": "100%"}
        )
    ],
        style = {"height": "100%"}
    ),
    html.Div([
        dcc.Dropdown(
            id = "dist-drop",
            options = [{"label": "Montreal", "value": "Montreal"}, {"label": "Quebec", "value": "Quebec"}],
            placeholder = "Select City")
    ],
        style = {"position": "absolute", "top": "50px", "left": "50px", "width": "200px"}
    )
], style = {"border-style": "solid", "height": "95vh"})

app.run_server()
