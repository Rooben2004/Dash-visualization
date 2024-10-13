import pandas as pd

# Load dataset (You can replace it with any dataset of your choice)
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df)

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Create a simple layout with dropdowns, graphs, etc.
app.layout = html.Div([
    html.H1("Titanic Data Visualization Dashboard"),

    # Dropdown for selecting a feature to visualize
    html.Label("Select Feature:"),
    dcc.Dropdown(
        id='feature-dropdown',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='Age'  # Default feature
    ),

    # Graph to display the distribution of selected feature
    dcc.Graph(id='feature-graph'),

    # A Bar chart for gender distribution
    html.Hr(),
    html.H3("Gender Distribution"),
    dcc.Graph(id='gender-bar', figure=px.bar(df, x='Sex', y='Survived', color='Sex', barmode='group'))
])

# Define callback to update the graph based on the selected feature
@app.callback(
    Output('feature-graph', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_graph(selected_feature):
    fig = px.histogram(df, x=selected_feature, title=f'Distribution of {selected_feature}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
