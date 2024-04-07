import streamlit as st
import pandas as pd
from joblib import load
from bmi_chart import make_bmi_chart


# -- Set page config
apptitle = 'LiveWell'

st.set_page_config(page_title=apptitle, page_icon="⚕️")


#ML model
xgb_8feat_path = '/Users/lauramckeown/iLab_Group_6_UTS/models/xgb_8features.joblib' 
#'/mount/src/ilab_group_6_uts/models/xgb_8features.joblib'
xgb_model = load(xgb_8feat_path)





# Function to initialize session state
def init_session_state():
    return st.session_state.setdefault('selected_page', 'Home')

          
def page_home():
    st.write('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    # Centered title using markdown and HTML
    # Centered titles
    st.markdown("<h1 style='text-align: center;'>LiveWell 🌱</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Obesity Prevention & Diabetes Learning Platform 📚</h1>", unsafe_allow_html=True)

    # Aligned headers
    st.markdown("<h2 style='text-align: justify;'>Obesity is a major risk factor for a range of diseases, including heart disease, stroke, diabetes, and various types of cancer.</h2>", unsafe_allow_html=True)
    st.markdown("""
            <h2 style='text-align: justify;'>
            The diabetes epidemic is one of the largest and most complex health challenges Australia has faced. 
            It touches millions of lives across the country and impacts every part of our health system.
            <br><br>
            And its impact is growing. In the past 20 years, the numbers have dramatically increased by around 220%. 
            If the growth rates continue, there will be more than 3.1 million Australians living with diabetes by 2050 
            and the annual cost is forecast to grow to about $45 billion per annum in this time.
            </h2>
            """, unsafe_allow_html=True)
    
    st.title("Do you want to know your status?")
    st.header('Tell us about your self')
    
    age = height = st.slider('Your age', 18, 90, 18)
    gender = st.radio('Your Gender',['Female','Male', 'I prefer not to answer'])
    
    # Calculate BMI with user inputted height and weight (in metric)
    height = st.number_input('Insert your height in cm', min_value = 0.0, max_value = 2.5)
    weight = st.number_input('Insert your weight in kg', min_value = 0.0, max_value = 300.0)
    
    high_bp = st.selectbox('Do you have high Blood Pressure?',['Yes','No'])
    high_col = st.selectbox('Have you check your cholesterol level in the last 5 years?',['Yes','No'])
    smoke = st.selectbox('Have you smoked at least 100 cigarettes in your entire life?',['Yes','No'])


    #[Note: 5 packs = 100 cigarettes] 
    stroke = st.selectbox('(Ever told) you had a stroke.',['Yes','No'])
    chdmi = st.selectbox('(Ever told)  you had coronary heart disease (CHD) or myocardial infarction (MI)',['Yes','No'])
    phys_act = st.selectbox('Have you done any physical activity in past 30 days - not including job?',['Yes','No'])
    fruits = st.selectbox('Do you consume one fruit or more times per day?',['Yes','No'])
    veggies = st.selectbox('Do you consume one vegetables or more times per day?',['Yes','No'])
    drinker = st.selectbox('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) ',['Yes','No'])
    health_cov = st.selectbox('Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. ?',['Yes','No'])
    doct_vis = st.selectbox('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',['Yes','No'])
    gen_health = st.selectbox('Would you say that in general your health is',['Excellent','Very good','Good', 'Fair', 'Poor'])
    men_health = st.number_input('Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? ', min_value = 0.0, max_value = 30.0)
    phys_health = st.number_input('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? ', min_value = 0.0, max_value = 30.0)
    walk = st.selectbox('Do you have serious difficulty walking or climbing stairs?',['Yes','No'])

        # Do no show conversion button until height and weight are selected
    if height == None or weight == None:
        st.write('Please input height and weight')
    else:
    # When reasonable input is provided, add a button to get and display the BMI
        if st.button('Calculate BMI'):
            bmi = round((weight / (height ** 2)), 1)
            fig = make_bmi_chart(bmi)
            st.write(fig)   

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
    #button_survey = st.sidebar.button("📝 Survey")
    button_results = st.sidebar.button("📊 Know Your Status")
    button_recommendation = st.sidebar.button("⭐ Recommendation") 
    #button_explore = st.sidebar.button("🌐 Explore obesity in the World")
    button_team = st.sidebar.button("👥 Team")
    button_resources = st.sidebar.button("📚 Resources")


    
    # Initialize session state
    init_session_state()

    # Check which button is clicked and execute the corresponding function
    if button_home:
        st.session_state.selected_page = 'Home'

    #if button_survey:
    #    st.session_state.selected_page = 'Survey'

    if button_results:
        st.session_state.selected_page = 'Know Your Status'

    if button_recommendation:
        st.session_state.selected_page = 'Recommendation'

    #if button_explore:
    #    st.session_state.selected_page = 'Explore'

    if button_team:
        st.session_state.selected_page = 'Team'

    if button_resources:
        st.session_state.selected_page = 'Resources'

    # Execute the corresponding function based on the selected page
    if st.session_state.selected_page == 'Home':
        page_home()
    #elif st.session_state.selected_page == 'Survey':
    #    page_survey()
    elif st.session_state.selected_page == 'Know Your Status':
        page_results()
    elif st.session_state.selected_page == 'Recommendation':
        page_recommendations()
    #elif st.session_state.selected_page == 'Explore':
     #   page_explore()
    elif st.session_state.selected_page == 'Team':
        page_team()
    elif st.session_state.selected_page == 'Resources':
        page_resources()

if __name__ == "__main__":
    main()

          
          




          
          