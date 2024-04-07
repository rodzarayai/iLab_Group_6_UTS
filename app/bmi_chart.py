import matplotlib
import matplotlib.pyplot as plt


def make_bmi_chart(BMI):
    
    # Set colours and values for each BMI class
    colors = ['#B71C1C','#F44336','#FF9800', '#FFCA28', '#27ae60', '#FFEE58']
    values = [60, 40, 35, 30, 25, 18.5, 0,]

    # Set figure size
    fig = plt.figure(figsize = (18,18))

    # Make polar projection half circle plot
    ax = fig.add_subplot(projection='polar');
    ax.set_thetamin(0)
    ax.set_thetamax(180)

        # Add BMI class sections
    ax.bar(x=[0, 0.97, 1.31, 1.57, 1.83, 2.09], width=1.05, height=0.5, bottom=2,
        linewidth=3, edgecolor='white',
        color=colors, align='edge');
    
    # Add lables to BMI class sections
    plt.annotate('Obesity Class III', xy=(0.4, 2.02), rotation=-65, color='white', fontweight='bold', fontsize=12);
    plt.annotate('Obesity Class II', xy=(1.22, 2.05), rotation=-25, color='white', fontweight='bold', fontsize=12);
    plt.annotate('Obesity Class I', xy=(1.55, 2.19), rotation=-7, color='white', fontweight='bold', fontsize=12);
    plt.annotate('Overweight', xy=(1.79, 2.25), rotation=7, color='black', fontweight='bold', fontsize=12);
    plt.annotate('Healthy Weight', xy=(2.08, 2.28), rotation=20, color='white', fontweight='bold', fontsize=12);
    plt.annotate('Underweight', xy=(2.7, 2.25), rotation=60, color='black', fontweight='bold', fontsize=12);

        # Add number lables
    for loc, val in zip([0, 0.97, 1.31, 1.57, 1.83, 2.09, 3.14], values):
        plt.annotate(val, xy=(loc, 2.5), fontsize=15, ha='right' if val<=25 else 'left')
        
    # Make pointer
    plt.annotate(BMI, xytext=(0,0), xy=(3.14 - (BMI*(3.14/60)), 2.0), 
                arrowprops=dict(arrowstyle='wedge, tail_width=0.4', color='black', shrinkA=0),
                bbox=dict(boxstyle='circle', facecolor='black', linewidth=2.0),
                fontsize=45, color='white', ha='center'
                );

    # Make chart title
    plt.title('BMI Chart', loc='center', pad=20, fontsize=35, fontweight='bold');

    # Turn off axes
    ax.set_axis_off();

    return fig