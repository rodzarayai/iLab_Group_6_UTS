import streamlit as st
import pandas as pd
from joblib import load
import datetime
import os
import xgboost as xgb




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, page_icon="⚕️")


#ML model
xgb_8feat_path = '/mount/src/ilab_group_6_uts/models/xgb_8features.joblib'
xgb_model = load(xgb_8feat_path)





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
    st.title("Tell us about your lifestyle/habits")
    st.write('Quiz with the necessary information to fed the model. All the questions are related to lifestyle and habits')
    
    gender = st.radio('Gender',['Female','Male', 'I prefer not to answer'])
    age = height = st.slider('Your age', min_value = 0.0, max_value = 90.0)

    
    # Calculate BMI with user inputted height and weight (in metric)
    height = st.slider('Insert your height in cm', 0, 230, 170)
    weight = st.slider('Insert your weight in kg', 0, 300, 70)
    
    
    
    # Do no show conversion button until height and weight are selected
    if height == None or weight == None:
        st.write('Please input height and weight')
    else:
    # When reasonable input is provided, add a button to get and display the BMI
        if st.button('Calculate BMI'):
            bmi = round((weight / (height ** 2)), 1)
            # df of WHO nutritional status by weight
            bmi_categories = {"Underweight": [0.0, 18.49], "Normal weight": [18.5, 24.9], "Pre-obesity": [25.0, 29.9], 
                              "Obesity class II":[35.0, 39.9], "Obesity class III": [40.0, 100]}
            bmi_df = pd.DataFrame(bmi_categories, index = ['min weight', 'max weight'])
            st.write("Your BMI is: ", bmi)
            st.write(bmi_df)
    
    bmi = round((weight / (height ** 2)), 1)
    
    high_bp = st.radio('Do you have high Blood Pressure?',['Yes','No'])
    high_col = st.radio('Have you check your cholesterol level in the last 5 years?',['Yes','No'])
    #smoke = st.selectbox('Have you smoked at least 100 cigarettes in your entire life?',['Yes','No'])


    #[Note: 5 packs = 100 cigarettes] 
    #stroke = st.selectbox('(Ever told) you had a stroke.',['Yes','No'])
    #chdmi = st.selectbox('(Ever told)  you had coronary heart disease (CHD) or myocardial infarction (MI)',['Yes','No'])
    #phys_act = st.selectbox('Have you done any physical activity in past 30 days - not including job?',['Yes','No'])
    #fruits = st.selectbox('Do you consume one fruit or more times per day?',['Yes','No'])
    #veggies = st.selectbox('Do you consume one vegetables or more times per day?',['Yes','No'])
    #drinker = st.selectbox('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) ',['Yes','No'])
    #health_cov = st.selectbox('Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. ?',['Yes','No'])
    #doct_vis = st.selectbox('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',['Yes','No'])
    #gen_health = st.selectbox('Would you say that in general your health is',['Excellent','Very good','Good', 'Fair', 'Poor'])
    men_health = st.slider('Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? ',  0, 30, 15)
    phys_health = st.slider('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? ', 0, 30, 15)
    walk = st.radio('Do you have serious difficulty walking or climbing stairs?',['Yes','No'])
    
    edu = st.radio('Education level', ['Never attended school or only kindergarten'
                                        ,'Elementary'
                                        ,'Some high school'
                                        ,'High school graduate'
                                        ,'Some college or technical school'
                                        ,'College graduate' ])

    income = st.radio('Monthly Income (AUD)', ['[1 - 22,500]'
                                                ,'[22,501 - 33,750]'
                                                ,'[33,751 - 45,000]'
                                                ,'[45,001 - 52,500]'
                                                ,'[52,501 - 67,500]'
                                                ,'[67,501 - 75,000]'

                                               
    
    if st.button('Calculate Diabetes'):
            bmi = round((weight / (height ** 2)), 1)
            # df of WHO nutritional status by weight
            bmi_categories = {"Underweight": [0.0, 18.49], "Normal weight": [18.5, 24.9], "Pre-obesity": [25.0, 29.9], 
                              "Obesity class II":[35.0, 39.9], "Obesity class III": [40.0, 100]}
            bmi_df = pd.DataFrame(bmi_categories, index = ['min weight', 'max weight'])
            st.write("Your BMI is: ", bmi)
            st.write(bmi_df)
    
    input_mapping_xgb = {
    'startingAirport': int(starting_airport_xgb),
    'destinationAirport': int(destination_aiport_xgb),
    'departureTime1': hour_of_day,
    'segmentsCabinCode': int(cabin_encoded)
 
}

input_df_xgb = pd.DataFrame([input_mapping_xgb])

column_order_model_xgb = ['departureTime1', 'segmentsCabinCode', 'startingAirport', 'destinationAirport']
input_df_xgb = input_df_xgb[column_order_model_xgb]



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

          
          




          
          