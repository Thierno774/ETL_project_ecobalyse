import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


app.layout = html.Div([
    html.Div(
        style={'width':'5%', 'height':'100%','float':'left'},
        children=[
            dcc.Checklist(className ='checkbox_1',
                    options=[
                        {'label': 'A1', 'value': 'I1ST1'},
                        {'label': 'A2', 'value': 'I2ST1'},
                        {'label': 'A3', 'value': 'I3ST1'},
                        {'label': 'A4', 'value': 'I4ST1'},
                        {'label': 'A5', 'value': 'I5ST1'},
                        {'label': 'A6', 'value': 'I6ST1'}
                            ],
                    values=['I1ST1'],
                    labelStyle = {'display': 'block'}
                            ),
        ]
    ),
    html.Div(
        style={'width':'5%', 'height':'100%','float':'left'},
        children=[
            dcc.Checklist(className ='checkbox_1',
                    options=[
                        {'label': 'B1', 'value': 'I1ST2'},
                        {'label': 'B2', 'value': 'I2ST2'},
                        {'label': 'B3', 'value': 'I3ST2'},
                        {'label': 'B4', 'value': 'I4ST2'},
                        {'label': 'B5', 'value': 'I5ST2'},
                        {'label': 'B6', 'value': 'I6ST2'}
                            ],
                    values=['I1ST2'],
                    labelStyle = {'display': 'block'}
                            )
        ]
    ),
    html.Div(
        style={'width':'5%', 'height':'100%','float':'left'},
        children=[
            dcc.Checklist(className ='checkbox_1',
                    options=[
                        {'label': 'C1', 'value': 'I1MT'},
                        {'label': 'C2', 'value': 'I2MT'},
                        {'label': 'C3', 'value': 'I3MT'}
                            ],
                    values=['I1MT'],
                    labelStyle = {'display': 'block'}
                            )
        ]
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)