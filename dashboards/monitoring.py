import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import json

# Load chaos report
with open("reports/chaos_report.json") as f:
    data = json.load(f)

# Example dummy metrics for visualization
df = pd.DataFrame({
    "Service": ["A", "B", "A", "B"],
    "Metric": ["Latency", "Latency", "Errors", "Errors"],
    "Value": [0.5, 0.8, 2, 1]
})

app = dash.Dash(__name__)
fig = px.bar(df, x="Service", y="Value", color="Metric", barmode="group")

app.layout = html.Div([
    html.H1("Chaos Simulation Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
