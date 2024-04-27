import streamlit as st
import pandas as pd
import plotly.express as px

def chart_ob_pre():

    data = pd.read_csv("../chart_data/share-of-adults-defined-as-obese.csv")

    fig_base = px.choropleth(data,
                        locations="Code",
                        color="Percent",
                        hover_name="Entity",
                        title='Prevalence of Obesity in adults.<br><sup>Estimated prevalence of obesity, based on general population surveys and statistical modeling.</sup>',
                        animation_frame="Year",
                        range_color=[0, 40],
                        color_continuous_scale = 'temps',
                        #color_continuous_scale=px.colors.sequential.Sunsetdark,
                        projection="natural earth")

    fig_base.update_layout(geo=dict(showframe=False, showcoastlines=False, showcountries=True, countrycolor="LightGray", projection_type='equirectangular'),
                      coloraxis_colorbar=dict(tickvals=list(range(0, 45, 10))),
                      updatemenus=[dict(type='buttons', showactive=False,
                                        buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=75, redraw=True), fromcurrent=True)]),
                                                 dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=True), mode='immediate')])])])

    fig = st.plotly_chart(fig_base)

    return fig

if __name__ == "__main__":
    chart_ob_pre()