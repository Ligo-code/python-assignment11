from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("GDP Per Capita Over Time by Country"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in df['country'].unique()],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    filtered_df = df[df["country"] == selected_country]
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita in {selected_country}",
        labels={"gdpPercap": "GDP Per Capita ($)", "year": "Year"}
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)

server = app.server
