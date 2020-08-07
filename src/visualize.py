import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import plotly.graph_objects as go

import src.getData as gd

df, global_data = gd.getGlobalData()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2('Covid-19 Dashboard'),

    html.Button('Update data', id='update_data_btn', n_clicks=0),
    
    html.Div(id='update_time_container'),
    
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
    ],style={"width" : "100%"})

])

@app.callback([Output('update_time_container','children'),
               Output('dropdown','value')],
              [Input('update_data_btn','n_clicks')])
def update_data(btn1):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'update_data_btn' in changed_id:
        global df
        global global_data
        df, global_data = gd.updateGlobalData()
        print("data updated",df["Date"][0],"here")
    time = df["Date"][0]
    print(time)
    return [html.Div("latest data available till {}".format(time)),'Global']


@app.callback(Output('choropleth', 'figure'),
              [Input('dropdown', 'value')])
def make_choropleth(value):
    print("updating choropleth")
    global df
    global global_data
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
