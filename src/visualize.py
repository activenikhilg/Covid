import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import plotly.graph_objects as go

import src.getData as gd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2('Covid-19 Dashboard'),
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[{"label":"Global","value":"Global"}],
            value = "Global",
            multi=False
        ),
        dcc.Graph(
            id='choropleth'
        ),
    ])
])

@app.callback(Output('choropleth', 'figure'),
              [Input('dropdown', 'value')])
def make_choropleth(value):
    df, global_data = gd.getGlobalData()
    fig = go.Figure(
        data =go.Choropleth(
            locations = df['CountryCode'],
            z = df['TotalConfirmed'],
            text = df['Country'],
            colorscale = 'Reds',
            autocolorscale=False,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title = 'Total Confirmed',
            # hovertext = df['TotalDeaths']
        ) 
    )
    fig.update_layout(
        title_text='',
        autosize = False,
        height=700,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        )
    )
    return fig
