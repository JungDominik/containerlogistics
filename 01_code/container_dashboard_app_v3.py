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
df_initial = df_initial.dropna(subset=['Humidity']) #Remove rows with missing Humidity values
df_initial['Temperature'] = df_initial['Temperature'].astype('float')
df_initial['Humidity'] = df_initial['Humidity'].astype('float')

#Manage Datetimes
df_initial['Datetime'] = pd.to_datetime(
    df_initial['Date'] + ' ' + df_initial['Time_UTC']
)

#Identify list of unique Containers for use in search (query)
list_containers = df_initial['SXXJ number'].unique()


###Set up Dashboard 

#Get stylesheets
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
#Set up app
app = Dash(__name__, external_stylesheets=external_stylesheets)

#Layout
app.layout = html.Div(
    children=[
        
        #This it the Container Selection menu. The selection correctly shows the available containers however selection does not yet impact the graph
        #Pretty ayout still TODO
        html.Div(
            children = [
                        html.Div(children="Container Selection", className="menu-title"),
                        dcc.Dropdown(
                            id="container-filter",
                            options=[
                                {"label": container, 
                                "value": container}
                                for container in list_containers
                            ],
                            value="A",
                            clearable=False,
                            className="dropdown",
                        )
            ]
        ),
        
        html.Div(
                    children=[
                        html.Div(children="Type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {
                                    "label": container.title(),
                                    "value": container,
                                }
                                for container in list_containers
                            ],
                            value="organic",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
        
        html.Div(
            children =[
                html.Div(
                    children = "Date Range", className ="menu-title"
                ),
                dcc.DatePickerRange(
                    id = "date-range",
                    min_date_allowed=df_initial["Date"].min(),
                    max_date_allowed=df_initial["Date"].max(),
                    start_date=df_initial["Date"].min(),
                    end_date=df_initial["Date"].max()
                )
            ],
            className = "menu"
        ),
        
        
        html.Div(
            children = [
                html.P(children="🚢📦", className="header-emoji"),
                html.H1(
                    children="Container Dashboard",
                    className="header-title"
                ),
                html.P(
                    children=(
                        "See the temperature and humidity inside your sea container during the transport."
                    ), 
                    className="header-description",
            ),
        ],
        className= "header",
    ),

    
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_initial['Datetime'],
                                    "y": df_initial['Temperature'],
                                    #"y": df_initial.loc[df_initial['SXXJ number'] == 'C', 'Temperature'],  ### Possible implementation of filtering for Container (identified in column SXXJ Number)
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}°C<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Container Temperature",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_initial['Datetime'],
                                    "y": df_initial['Humidity'],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Container Humidity",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#3399ff"],
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
    
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": df_initial['Datetime'],
#                         "y": df_initial['Temperature'],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Container Temperature"},
#             },
#         ),
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": df_initial['Datetime'],
#                         "y": df_initial['Humidity'],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Container Humidity"},
#             },
#         ),
#     ]
# )

# Update Map Graph based on date-picker, selected data on histogram and location dropdown
#@app.callback
#pass

#Making the app react to user interaction
def update_graph(datePicked, selectedData, selectedLocation):
    pass

# Run the app
if __name__ == "__main__":
   app.run_server(debug=True)