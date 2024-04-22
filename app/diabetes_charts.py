import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

#### HOW TO MAKE FIGURES IN STREAMLIT ####
'''
    map = make_diabetes_map()
    charts = make_diabetes_charts_alt()

    st.plotly_chart(map, use_container_width=False)
    st.altair_chart(charts)

    Plotly bar and line chart as back up but the altair ones look better
'''


def make_diabetes_map():
    # Import databetes data file.
    file_name = '../chart_data/diabetes_world_data.csv'
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
    file_name = '../chart_data/diabetes_regional_data.csv'
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
        height=300
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
        height=300
    )


    charts = bar | line

    final_charts = charts.configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    )
    return final_charts










def make_diabetes_charts_plotly():
    # Regional data
    regional_pct = pd.DataFrame({'Year': [2000, 2011, 2021, 2030, 2045],
                           'Global':[4.6, 8.5, 9.8, 10.8, 11.2],
                           'Africa': [1.2, 4.5, 5.3, 5.5, 5.6],
                           'Europe': [4.9, 6.7, 7.0, 8.0, 8.7],
                           'Middle East and North Africa': [7.7, 11.0, 18.1 ,19.6, 20.4],
                           'North America and Caribbean': [7.8, 10.7, 11.9, 13.3, 14.2],
                           'South and Central America': [3.7, 9.2, 8.2, 9.2, 9.9],
                           'South-East Asia': [5.3, 9.2, 10.0, 10.9, 11.3],
                           'Western Pacific': [3.6, 8.3, 9.9, 10.9, 11.5]})

    # 2021 data
    data_2021 = pd.DataFrame({'Regions': ['Global', 'Middle East and North Africa', 'North America and Caribbean', 'South-East Asia',
                                                   'Western Pacific', 'South and Central America', 'Europe', 'Africa'],
                                       'Prevalence': [9.8, 18.1, 11.9, 10.0, 9.9, 8.2, 7.0, 5.3]})

    # Data for bar chart
    x_bar = data_2021['Regions']
    y_bar = data_2021['Prevalence']
    colors_bar = ['#222A2A', 'rgb(225,124,5)', 'rgb(15,133,84)', 'rgb(204,80,62)', 'rgb(111,64,112)', 'rgb(56,166,165)', 'rgb(29,105,150)', 'rgb(148,52,110)']

    # Data for line chary
    x_line = regional_pct.pop('Year')
    y_line = regional_pct
    labels = ['Global', 'Africa', 'Europe', 'Middle East and North Africa', 'North America and Caribbean', 'South and Central America', 'South-East Asia', 'Western Pacific']
    colors_line = ['#222A2A', 'rgb(148,52,110)', 'rgb(29,105,150)', 'rgb(225,124,5)', 'rgb(15,133,84)', 'rgb(56,166,165)', 'rgb(204,80,62)', 'rgb(111,64,112)']

    # Initialize figure with subplots
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.5, 0.5],
        specs=[[{"type": "bar"}, {"type": "scatter"}]])

    # Add locations bar chart
    fig.add_trace(
        go.Bar(
            x=x_bar,
            y=y_bar,
            name='Region',
            showlegend=False,
            marker_color = colors_bar),
        row=1, col=1
    )

    # Add line chart
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[0]],
                mode='lines+markers',
                name=labels[0],
                line=dict(color=colors_line[0]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[1]],
                mode='lines+markers',
                name=labels[1],
                line=dict(color=colors_line[1]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[2]],
                mode='lines+markers',
                name=labels[2],
                line=dict(color=colors_line[2]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[3]],
                mode='lines+markers',
                name=labels[3],
                line=dict(color=colors_line[3]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[4]],
                mode='lines+markers',
                name=labels[4],
                line=dict(color=colors_line[4]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[5]],
                mode='lines+markers',
                name=labels[5],
                line=dict(color=colors_line[5]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[6]],
                mode='lines+markers',
                name=labels[6],
                line=dict(color=colors_line[6]),
                showlegend=True,),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x_line, y=y_line[y_line.columns[7]],
                mode='lines+markers',
                name=labels[7],
                line=dict(color=colors_line[7]),
                showlegend=True,),
        row=1, col=2
    )

    # Update geo subplot properties
    fig.update_geos(
        projection_type="equirectangular",
        landcolor='lightgray',
        oceancolor="white",
        showocean=True,
        lakecolor="white"
    )

    # Rotate x-axis labels
    fig.update_xaxes(tickangle=45)

    # Set theme, margin, and annotation in layout
    fig.update_layout(
        template="simple_white",
        margin=dict(r=10, t=25, b=40, l=60),
    )

    return fig


def make_diabetes_charts_alt():
    
    # Import databetes data file.
    file_name2 = '../chart_data/diabetes_regional_data.csv'
    region_pct = pd.read_csv(file_name2)
    
    click = alt.selection_multi(encodings=['color'])

    line = alt.Chart(region_pct).mark_line().encode(
        x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45), title=''),
        y=alt.Y('Prevalence:Q', title=''),
        color=alt.Color('Region', legend=None),
        tooltip='Prevalence:Q',
    ).transform_filter(
        click
    ).properties(
        width=200,
        height=150
    )

    bar = alt.Chart(region_pct.loc[region_pct['Year'] == 2021]).mark_bar().encode(
        x=alt.X('Region:N', axis=alt.Axis(labelAngle=-45), title=''),
        y=alt.Y('Prevalence:Q', title='Age-adjusted comparative prevalence of diabetes, %'),
        color=alt.condition(click, 'Region', alt.value('lightgray')),
        tooltip='Prevalence:Q'
    ).add_selection(
        click
    ).properties(
        width=200,
        height=150
    )

    charts = bar | line

    charts.configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    )
    return charts