
import dash 
from dash import dcc
from dash import html
from dash.dependencies import Input,Output

import pandas as pd
import plotly.express as px 
import numpy as np

app = dash.Dash(__name__)


filename = "/home/thierno/formation_dataScientest/projet_final/dags/Output/ecobalyse_data_transformed.csv"

data = pd.read_csv(filename)



data['mass'] = pd.to_numeric(data['mass'], errors='coerce')
data = data.replace(np.nan, 0, regex=True)

data = data[data["mass"] != 0]
print(data["mass"].head())


## conversion of the data 


# try:
#     data['mass'] = data['mass'].astype('float64') 
# except: 
#     data["mass"] = np.Nana
#     pass 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)




fig = px.scatter(data,y="pef",
                  x="mass")

## Pie Chart 
values = data["product"].value_counts().values
labels = data["product"].value_counts().index


fig2 = px.pie(data , values = data["product"].value_counts().values, names = labels)
categorial_variable = ["product", "makingComplexity", "fabricProcess", "countryDyeing", "countryMaking"]
dcc_cat = dcc.Dropdown(
                    id = "categorial_variable_dropdown", 
                    options = categorial_variable, 
                    value = "product"

)



app.layout = html.Div([
        html.H1("Ecoabalyse API Dash Visualization", style={'textAlign': 'center', 'color': 'mediumturquoise'}), 
        html.Div(dcc.Graph(id = "graph_1", 
                           figure = fig)), 
        html.Div(
                    dcc_cat 
        ),
        html.Div(dcc.Graph (id = "graph_2", 
                            figure = fig2))
], style={"background-color": "#e5ecf6", "height": "100vh"})

@app.callback(Output(component_id = "graph_2", component_property = "figure"), 
              [Input(component_id = "categorial_variable_dropdown",component_property ="value" )])
def update_pie_chart(colnames): 
    values = data[colnames].value_counts().values
    labels = data[colnames].value_counts().index

    fig = px.pie(data ,
        values = values, names = labels)
    ## return the values
    return fig


if __name__ == '__main__':
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)
