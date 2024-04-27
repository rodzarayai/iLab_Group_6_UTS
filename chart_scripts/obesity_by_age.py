import streamlit as st
import pandas as pd
import plotly.express as px

def chart_ob_age():

    data = pd.read_csv('../chart_data/deaths-from-obesity-by-age.csv')

    selected_country = st.selectbox('Select Country', ['World'] + data['Country'].unique().tolist())

    if selected_country == 'World':
        world_data = data.groupby('Year').sum().reset_index()
        fig_base = px.area(world_data,
                           x='Year',
                           y=['Age_70+', 'Age_50-69', 'Age_15-49', 'Age_5-14', 'Age_5-'],
                           title='Deaths from Obesity by Age in World from 1990 to 2019<br><sup>Total premature deaths due to obesity (high body-mass index) differentiated by age.</sup>',
                           labels={'value': 'Population', 'Year': 'Year', 'variable': 'Age Group'}
                           )
        fig = st.plotly_chart(fig_base)
    else:
        filtered_data = data[data['Country'] == country]
        fig_base = px.area(filtered_data,
                    x='Year',
                    y=['Age_70+', 'Age_50-69', 'Age_15-49', 'Age_5-14', 'Age_5-'],
                    title='Deaths from Obesity by Age in World from 1990 to 2019<br><sup>Total premature deaths due to obesity (high body-mass index) differentiated by age.</sup>',
                    labels={'value': 'Population', 'Year': 'Year', 'variable': 'Age Group'}
                    )
        fig = st.plotly_chart(fig_base)

    return fig

if __name__ == "__main__":
    chart_ob_age()
