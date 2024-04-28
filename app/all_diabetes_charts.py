import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt
import streamlit as st

def make_diabetes_map():
    # Import databetes data file.
    file_name = '/mount/src/ilab_group_6_uts/chart_data/diabetes_world_data.csv'
    country_pct = pd.read_csv(file_name)

    # Add global country map
    map = go.Figure(data=go.Choropleth(locations=country_pct['iso_alpha'], # Spatial coordinates
                    z = country_pct['Diabetes Prevalence 2021'].astype(float), # Data to be color-coded
                    colorscale = 'temps', zmin=0, zmid=12,
                    text=country_pct['Country'], # hover text
                    marker_line_color='darkgray', # line markers between countries
                    showscale=False,))

    map.update_layout(
        title_text = 'Age-adjusted comparative prevalence of diabetes in 2021 (%)',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.60,
            y=0.03,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://diabetesatlas.org/data/en/world/">\
                International Diabetes Federation</a>',
            showarrow = False
        )]
    )

    return map

def make_diabetes_charts_altair():
    
    # Import databetes data file.
    file_name = '/mount/src/ilab_group_6_uts/chart_data/diabetes_regional_data.csv'
    region_pct = pd.read_csv(file_name)
    
    click = alt.selection_multi(encodings=['color'])
    
    bar = alt.Chart(region_pct.loc[region_pct['Year'] == 2021]).mark_bar().encode(
        x=alt.X('Region:N', axis=alt.Axis(labelAngle=-90), title=None, sort=['Global', 'Middle East and North Africa', 'North America and Caribbean', 'South-East Asia',
        'Western Pacific', 'South and Central America', 'Europe', 'Africa']),
        y=alt.Y('Prevalence:Q', title='Prevalence of diabetes, %'),
        color=alt.condition(click, 'Region', alt.value('lightgray')),
        tooltip=['Region:N', 'Prevalence:Q'],
    ).add_selection(
        click
    ).properties(
        width=300,
        height=200,
        title = 'Prevalence by Region'
    )

    line = alt.Chart(region_pct).mark_line().encode(
        x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45), title=None),
        y=alt.Y('Prevalence:Q', title=None),
        color=alt.Color('Region', legend=None),
        tooltip=['Region:N', 'Prevalence:Q'],
    ).transform_filter(
        click
    ).properties(
        width=300,
        height=200,
        title = 'Prevalence Over Time'
    )


    charts = bar | line

    final_charts = charts.configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    ).configure_title(
    fontSize=15,
    #font='Courier',
    anchor='start',
    #color='gray'
    )
    return final_charts

def chart_dia():

    tab1, tab2 = st.tabs(['Prevalence by Country', 'Prevalence by Region'])

    with tab1:
        map = make_diabetes_map()
        st.plotly_chart(map)

    with tab2:
        charts = make_diabetes_charts_altair()
        st.altair_chart(charts)