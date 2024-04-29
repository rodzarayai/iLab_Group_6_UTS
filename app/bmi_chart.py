import plotly.graph_objects as go
import numpy as np


def make_bmi_chart(BMI):
    # Define colours
    plot_bgcolor = 'rgba(0,0,0,0)'
    needle_color = "#333"
    gauge_colors = ["#f22626", "#f25926", "#f28c26", "#f2bf26", "#85e043", "#eff229"] 
    
    # Text for each category
    categories = ["Obesity Class III", "Obesity Class II", "Obesity Class I", "Overweight", "Healthy Weight", "Underweight"]
    
    # BMI ranges corresponding to each category
    bmi_ranges = [60, 40, 35, 30, 25, 18.5, 0]
    
    # Create gauge chart
    fig = go.Figure()

    # Add gauge trace
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = BMI,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "<b>BMI</b>"},
        gauge = {
            'axis': {'range': [10, 50]},
            'bar': {'color': needle_color},
            'steps': [
                {'range': [0, bmi_ranges[5]], 'color': gauge_colors[5], 'name': categories[5]},
                {'range': [bmi_ranges[5], bmi_ranges[4]], 'color': gauge_colors[4], 'name': categories[4]},
                {'range': [bmi_ranges[4], bmi_ranges[3]], 'color': gauge_colors[3], 'name': categories[3]},
                {'range': [bmi_ranges[3], bmi_ranges[2]], 'color': gauge_colors[2], 'name': categories[2]},
                {'range': [bmi_ranges[2], bmi_ranges[1]], 'color': gauge_colors[1], 'name': categories[1]},
                {'range': [bmi_ranges[1], bmi_ranges[0]], 'color': gauge_colors[0], 'name': categories[0]},
            ]
        }
    ))

    # Layout adjustments
    fig.update_layout(
        showlegend=False,
        margin=dict(b=0, t=10, l=25, r=25),
        width=600,
        height=400,
        paper_bgcolor=plot_bgcolor
    )
    
    
    return fig