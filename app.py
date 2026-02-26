import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# -------------------------
# Load and Prepare Data
# -------------------------

df = pd.read_csv("formatted_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# -------------------------
# Create Dash App
# -------------------------

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f8e8dc",
        "padding": "40px",
        "minHeight": "100vh"
    },
    children=[

        # Header
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#8b0000",
                "fontFamily": "Georgia",
                "marginBottom": "30px"
            }
        ),

        # Region Dropdown
        html.Div([
            html.Label(
                "Select Region:",
                style={
                    "fontWeight": "bold",
                    "color": "#5c4033",
                    "marginRight": "10px"
                }
            ),
            dcc.Dropdown(
                id="region-dropdown",
                options=[
                    {"label": region.title(), "value": region}
                    for region in df["Region"].unique()
                ],
                value=df["Region"].unique()[0],
                clearable=False,
                style={"width": "250px"}
            )
        ], style={"marginBottom": "30px"}),

        # Graph Container (Card Style)
        html.Div([
            dcc.Graph(id="sales-graph")
        ],
            style={
                "backgroundColor": "#fdf6ec",
                "padding": "25px",
                "borderRadius": "15px",
                "boxShadow": "0px 4px 15px rgba(0,0,0,0.1)"
            }
        )
    ]
)

# -------------------------
# Callback for Interactive Filtering
# -------------------------

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):

    filtered_df = df[df["Region"] == selected_region]

    daily_sales = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales"
    )

    # Pink line
    fig.update_traces(line=dict(color="#d63384", width=4))

    # Vertical line for price increase
    fig.add_vline(
        x="2021-01-15",
        line_width=2,
        line_dash="dash",
        line_color="#8b0000"
    )

    # Annotation
    fig.add_annotation(
        x="2021-01-15",
        y=max(daily_sales["Sales"]),
        text="Price Increase",
        showarrow=True,
        arrowhead=2,
        font=dict(color="#8b0000"),
        bgcolor="#fff0f5"
    )

    fig.update_layout(
        plot_bgcolor="#fdf6ec",
        paper_bgcolor="#fdf6ec",
        font=dict(color="#5c4033"),
        xaxis_title="Date",
        yaxis_title="Total Sales",
        title=f"Pink Morsel Sales in {selected_region.title()}"
    )

    return fig


# -------------------------
# Run Server
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)