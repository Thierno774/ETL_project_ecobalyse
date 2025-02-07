import dash 
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px 

from dash.dependencies import Input, Output
## Creation de la figure

df = px.data.gapminder()
df_1 = df[df["year"] == 2002]

fig = px.scatter(df, x="gdpPercap", y="lifeExp",
                        color="continent",
                        size="pop",
                        hover_name="country")





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


app.layout = html.Div([
        html.H1("API Dash", style={'textAlign': 'center', 'color': 'mediumturquoise'}), 
        html.Div(dcc.Dropdown(
                id = "Dropdown", 
                options = [{'label': 'life expandency', 'value': 'lifeExp'},
                                  {'label': 'population', 'value': 'pop'}],
                        value= 'lifeExp'
        )), 
        html.Div(dcc.Graph(id = "graph_1", 
                           figure = fig)), 

        html.Div(dcc.Slider (id = "slider_1", 
                             min = df["year"].min(), 
                             max = df['year'].max(), 
                             marks = {str(i): str(i) for i in df["year"].unique()}, 
                             step = None))
], style = {"background" : "beige"})
@app.callback(Output(component_id = "graph_1", component_property = "figure"), 
              [Input(component_id = "Dropdown",component_property ="value" ), 
               Input(component_id = "slider_1", component_property = "value")])
def update_graph(indicator, filter_year): 
    df_1 = df[df["year"] == filter_year]
    # Creation de la figure plotly 
    fig = px.scatter(df_1, x="gdpPercap",
                        y=indicator,
                        color="continent",
                        hover_name="country")
    return fig

if __name__ == '__main__':
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)
