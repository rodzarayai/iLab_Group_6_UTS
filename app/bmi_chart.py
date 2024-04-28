import plotly.graph_objects as go
import numpy as np



#### HOW TO MAKE FIGURES IN STREAMLIT ####
'''
    st.write(make_bmi_chart(bmi))
'''



def make_bmi_chart(BMI):
    # define colours
    plot_bgcolor = "#DDF0F0"
    quadrant_colors = [plot_bgcolor, "#f22626", "#f25926", "#f28c26", "#f2bf26", "#85e043", "#eff229"] 
    
    # Text for each quadrent
    quadrant_text = ["", "<b>Obesity Class III</b>", "<b>Obesity Class II</b>", "<b>Obesity Class I</b>", "<b>Overweight</b>", "<b>Healthy Weight</b>", "<b>Underweight</b>"]
    
    # Number of quadrants 
    n_quadrants = len(quadrant_colors) - 1
    
    # Weight category levels
    weight_values = [60, 40, 35, 30, 25, 18.5, 0,]

    # Min and max BMI for chart
    min_value = 0
    max_value = 60

    # Configure pointer
    hand_length = np.sqrt(2) / 4
    hand_angle = np.pi * (1 - (max(min_value, min(max_value, BMI)) - min_value) / (max_value - min_value))

    # Make BMI figure
    fig = go.Figure(
        data=[
            # Pie chart
            go.Pie(
                values = [0.5] + (np.array(weight_values) / 69 / n_quadrants).tolist(),
                rotation=90,
                hole=0.5,
                marker_colors=quadrant_colors,
                text=quadrant_text,
                insidetextorientation='tangential',
                textinfo="text",
                hoverinfo="skip"
            ),
        ],
        # Plot layout
        layout=go.Layout(
            showlegend=False,
            margin=dict(b=0,t=10,l=10,r=10),
            width=650,
            height=650,
            paper_bgcolor=plot_bgcolor,
            annotations=[
                go.layout.Annotation(
                    text=f"<b>BMI:</b><br>{BMI}",
                    font_size=50,
                    x=0.5, xanchor="center", xref="paper",
                    y=0.15, yanchor="bottom", yref="paper",
                    showarrow=False,
                )
            ],
            # Make pointer
            shapes=[
                go.layout.Shape(
                    type="circle",
                    x0=0.48, x1=0.52,
                    y0=0.48, y1=0.52,
                    fillcolor="#333",
                    line_color="#333",
                ),
                go.layout.Shape(
                    type="line",
                    x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                    y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                    line=dict(color="#333", width=4)
                )
            ]
        )
    )

    return fig