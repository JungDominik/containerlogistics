from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id = "graph-with-slider"),
    dcc.Slider (
        df['year'].min(),
        df['year'].max(),
        step = None,
        value = df['year'].min(),
        marks = {str(year): str(year) for year in df['year'].unique()},
        id = 'year-slider'
    )
]
)


@app.callback(
    Output("graph-with-slider", "figure"),
    Input('year-slider', 'value'))
def linkagefunc(in_year):
    df_filtered = df[df.year == in_year]

    figure = px.scatter(df_filtered, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55    
    )

    figure.update_layout(transition_duration=500)

    return figure








if __name__ == '__main__':
    app.run_server(debug=True)