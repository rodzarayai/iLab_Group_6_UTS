import streamlit as st
import pandas as pd
from joblib import load




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, page_icon="⚕️")


# Function to initialize session state
def init_session_state():
    return st.session_state.setdefault('selected_page', 'Home')

          
def page_home():
    st.write('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    st.title('How lifestyle/habits can lead to obesity and diabetes type 2')
    
    st.header('Research Question')
    st.markdown("""
    How do lifestyle factors and habits lead to obesity and type 2 diabetes and which one is the strongest predictive values?
    1. Examine the role of socio-economic status in lifestyle choices and its subsequent impact on health outcomes.
    2. Investigate specific lifestyle factors (diet, physical activity, sleep patterns, etc.) and their correlation with obesity and diabetes incidence.
    """)

    

def page_survey():
    """Displays the survey page title and introductory text with flexbox and adjusted markdown."""

    # Title
    font_family = "Copperplate, Fantasy"  

    text = f"""
<h1 style='text-align: center; color: #008080; font-size: 63px; font-family: {font_family}; font-weight: bolder'>
  Unlock Your Health Insights: Take Our Personalized Survey
</h1>
"""

    st.markdown(text, unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: #008080; font-size: 60px'; font-family: Papyrus, Fantasy'> Unlock Your Health Insights: Take Our Personalized Survey</h1>", unsafe_allow_html=True)


    # Subheader
    text2 = """
<h1 style='text-align: center; color: #2F4F4F; font-style: italic; font-size: 25px; font-family: Times New Roman, sans-serif;'>
  Help us get a quick snapshot of your health and well-being by answering a few quick questions!
</h1>
"""
    st.markdown(text2, unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: black; font-style: italic; font-size: 20px'>Help us get a quick snapshot of your health and well-being by answering a few quick questions!</h1>", unsafe_allow_html=True)


    st.divider()

    st.header('Tell us about yourself')

    gender = st.radio('Select your gender:',['Male','Female','I prefer not to say'])
    st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
    </style>
    """, unsafe_allow_html=True)


    age = st.slider('Please select your age:', min_value=0, max_value=90, step=1)
    st.markdown(
    """<style>
div[class*="Slider"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
    </style>
    """, unsafe_allow_html=True)
    
    
    # Calculate BMI with user inputted height and weight (in metric)
    height = st.number_input('Please enter your height in cm:', min_value = 0.0, max_value = 250.0)
    weight = st.number_input('Please enter your weight in kg', min_value = 0.0, max_value = 300.0)
    st.markdown(
    """<style>
div[class*="NumberInput"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
    </style>
    """, unsafe_allow_html=True)
    
    

    # Calculate BMI
    height_in_ms = height/100
    
    if st.button('Calculate BMI') :
        if height != 0:
            bmi = round((weight / (height_in_ms ** 2)), 1)
            # df of WHO nutritional status by weight
            bmi_categories = {"Underweight": [0.0, 18.49], "Normal weight": [18.5, 24.9], "Pre-obesity": [25.0, 29.9], 
                                "Obesity class II":[35.0, 39.9], "Obesity class III": [40.0, 100]}
            bmi_df = pd.DataFrame(bmi_categories, index = ['Minimum Weight', 'Maximum Weight'])
            st.write("Your BMI is: ", bmi)
            st.write(bmi_df)
        elif height == None or weight == None:
            st.write('Please input height and weight')
        elif height == 0:
            st.write('Entered height cannot be 0. Please enter again')

    
    st.divider()

    st.header('Tell us about your health status')
    
    
    high_bp = st.radio('Do you have high blood pressure?',['Yes','No'])
    high_col = st.radio('Have you checked your cholesterol level in the last 5 years?',['Yes','No'])
    

    gen_health = st.radio('What would you say your health status is in general?',['Excellent','Very good','Good', 'Fair', 'Poor'])

    info3 = "Mental health includes stress, depression, and all problems connected with emotions etc."  
    men_health = st.slider("How many days in the past 30 days did you feel metnally unwell?", max_value=30)
    # HTML box
    st.markdown(f'<span title="{info3}"> ⓘ </span>', unsafe_allow_html=True)

    
    info4 = "Physical health includes all types of physical injuries and illnesses."
    phys_health = st.slider("How many days in the past 30 days did you feel physically unwell?", max_value=30)
    # HTML box
    st.markdown(f'<span title="{info4}"> ⓘ </span>', unsafe_allow_html=True)

    walk = st.radio('Do you have a serious difficulty walking or climbing stairs?',['Yes','No'])

    st.divider()

    st.header('Tell us about your education and income')

    st.radio('Your educational level:', ['Never attended school or only kindergarten',
                                         'Elementary',
                                         'High school dropout',
                                         'High school graduate',
                                         'Colleug or technical school dropout',
                                         'College graduate or above'])
    
    st.radio('Your annual income range:', ['[1 - 22,500]',
                                           '[22,501 - 33,750]',
                                           '[33,751 - 45,000]',
                                           '[45,001 - 52,500]',
                                           '[52,501 - 67,500]',
                                           '[67,501 - 75,000]'])
    st.info('st.info test')



def page_results():
    st.title("Know your status")
    st.write('Results based on ML models trained')
    
def page_recommendations():
    st.title("Recommendations")
    st.write('Find recommendations based on the results')
    

    
def page_explore():
    st.title("Explore Obesity in the World/Australia")
    st.write('Explore data of obesity around the world and show how the person is in relation to the world/Australia')
    
def page_team():
    st.title("Know the team")
    st.write('Group 6 members')
    
def page_resources():
    st.title("Resources")
    st.write('Resources, papers, etc used. in the project')

def main():
    st.sidebar.title("Explore")
 

    # Create links for each page
    # Create buttons with icons for each page
    button_home = st.sidebar.button("🏠 Home")
    button_survey = st.sidebar.button("📝 Survey")
    button_results = st.sidebar.button("📊 Know Your Status")
    button_recommendation = st.sidebar.button("⭐ Recommendation") 
    button_explore = st.sidebar.button("🌐 Explore obesity in the World")
    button_team = st.sidebar.button("👥 Team")
    button_resources = st.sidebar.button("📚 Resources")


    
    # Initialize session state
    init_session_state()

    # Check which button is clicked and execute the corresponding function
    if button_home:
        st.session_state.selected_page = 'Home'

    if button_survey:
        st.session_state.selected_page = 'Survey'

    if button_results:
        st.session_state.selected_page = 'Know Your Status'

    if button_recommendation:
        st.session_state.selected_page = 'Recommendation'

    if button_explore:
        st.session_state.selected_page = 'Explore'

    if button_team:
        st.session_state.selected_page = 'Team'

    if button_resources:
        st.session_state.selected_page = 'Resources'

    # Execute the corresponding function based on the selected page
    if st.session_state.selected_page == 'Home':
        page_home()
    elif st.session_state.selected_page == 'Survey':
        page_survey()
    elif st.session_state.selected_page == 'Know Your Status':
        page_results()
    elif st.session_state.selected_page == 'Recommendation':
        page_recommendations()
    elif st.session_state.selected_page == 'Explore':
        page_explore()
    elif st.session_state.selected_page == 'Team':
        page_team()
    elif st.session_state.selected_page == 'Resources':
        page_resources()

if __name__ == "__main__":
    main()

          
          




          
          