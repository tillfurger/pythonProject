from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
from datetime import datetime as dt
import plotly.graph_objects as go
from xbbg import blp


app = DjangoDash('bloomberg_dash')
app.css.append_css({'external_url': '/_static/css/dash.css'})

# Write the HTML Code for it
app.layout = html.Div(
    [

        html.Div([
            html.Div([
                html.Label('Gebe einen gültigen Ticker ein:'),
                dcc.Input(
                    id="ticker-input",
                    type="text",
                    placeholder="Ticker",
                )], className='four columns'),
            html.Div([
                html.Label('Wähle eine Variable:'),
                dcc.Dropdown(
                    id="variable-dropdown",
                    options=[
                        {'label': 'Last Price', 'value': 'PX_LAST'},
                        {'label': 'Total Return Index', 'value': 'TOT_RETURN_INDEX_GROSS_DVDS'},
                        {'label': 'Market Cap', 'value': 'CUR_MKT_CAP'}
                    ],
                    value='PX_LAST'
                )], className='four columns'),
            html.Div([
                html.Label('Wähle deinen Zeitraum:'),
                dcc.DatePickerRange(
                    id="date-picker",
                    start_date_placeholder_text='Start',
                    end_date_placeholder_text='Ende',
                    display_format='DD.MM.YYYY',
                    max_date_allowed=dt.today()
                )], className='four columns'),
        ]),

        html.Div([
            dcc.Graph(
                id='graph',
                config={
                    'displaylogo': False,
                    'legendPosition': True,
                    'toImageButtonOptions': {'format': 'svg'}},
                figure={
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                    )
                }
            )
        ], className='twelve columns')
    ]
)


@app.callback(
    Output('graph', 'figure'),
    [Input('ticker-input', 'value'),
     Input('variable-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')])
def plot_data(ticker, variable, start, end):
    plot_data = blp.bdh(ticker, variable, start, end)
    traces = []
    traces.append(
        go.Scatter(
            dict(
                x=plot_data.index,
                y=plot_data[ticker][variable],
                mode='lines',
                opacity=0.7,
                name=ticker,
            )
        )
    )

    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    return go.Figure(data=traces, layout=layout)
