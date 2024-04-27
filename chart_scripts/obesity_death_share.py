import streamlit as st
import pandas as pd
import plotly.express as px

def chart_ob_dea():

    data = pd.read_csv("../chart_data/death-rate-vs-share-obesity.csv").dropna()

    fig = px.scatter(data,
                    x='Percentage',
                    y='Deaths', color='Continent',
                    hover_data=['Country', 'Country_code', 'Year'],
                    title='Death rate from obesity vs. share of adults who are obese<br><sup>Premature deaths attributed to obesity per 100,000 individuals.</sup>',
                    animation_frame='Year')
    fig.update_layout(xaxis_title='Adult obesity',
                    yaxis_title='Death rate from obesity',
                    updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=75, redraw=False), fromcurrent=True)]),
                                                dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])]
                                                )
    plotly_chart = st.plotly_chart(fig)

if __name__ == "__main__":
    chart_ob_dea()
