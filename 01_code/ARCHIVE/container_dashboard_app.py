import os 
import pandas as pd
import matplotlib.pyplot as plt
from dash import Dash, dcc, html



#File structure etc
datafolder = os.path.join("..", "00_data")
datafile = "161209_Schenker_Sensordaten.csv"

#Import
df_initial = pd.read_csv(os.path.join(datafolder, datafile))

#Clean data
df_initial = df_initial.drop(0) #Remove first row which contains the measuring units
df_initial = df_initial.dropna(subset=['Temperature']) #Remove rows with missing temperature 
df_initial = df_initial.dropna(subset=['Latitude', 'Longitude']) #Remove rows with missing GPS values
df_initial['Temperature'] = df_initial['Temperature'].astype('float')


###Set up Dashboard 

#Set up app
app = Dash(__name__)

#Layout
app.layout = html.Div(
    children=[
        # ...
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_initial['Temperature'],
                                    "y": df_initial['Temperature'],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Graph Header (Temperature)",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)



#Making the app react to user interaction
def update_graph(hoverData)    :
    pass

# Run the app
#if __name__ == "__main__":
#    app.run_server(debug=True)