from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

# =====================================
# DATA
# =====================================

df = pd.DataFrame({
    "Parameter": ["pH", "COD", "BOD", "TSS"],
    "Nilai": [7.2, 80, 20, 40]
})

fig = px.bar(
    df,
    x="Parameter",
    y="Nilai",
    title="Kualitas Air"
)

# =====================================
# LAYOUT
# =====================================

app.layout = html.Div([

    html.H1("🌊 WaterLab Analyzer Pro"),

    html.H3("Evaluasi pH Air"),

    dcc.Input(
        id='ph-input',
        type='number',
        value=7
    ),

    html.Button(
        'Evaluasi',
        id='btn'
    ),

    html.Br(),
    html.Br(),

    html.Div(id='output'),

    dcc.Graph(figure=fig)

])

# =====================================
# CALLBACK
# =====================================

@app.callback(
    Output('output', 'children'),
    Input('btn', 'n_clicks'),
    Input('ph-input', 'value')
)

def evaluasi(n_clicks, ph):

    if ph is None:
        return ""

    if 6 <= ph <= 9:
        return "✅ pH memenuhi baku mutu"

    return "❌ pH melebihi baku mutu"

# =====================================
# RUN
# =====================================

if __name__ == '__main__':
    app.run(debug=True)
