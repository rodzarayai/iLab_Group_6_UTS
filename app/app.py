import streamlit as st
import pandas as pd
from joblib import load
import datetime
import os
import xgboost as xgb
import plotly.graph_objects as go




# -- Set page config
apptitle = 'LiveWell'

st.set_page_config(page_title=apptitle, page_icon="⚕️")


#ML model
xgb_8feat_path = '/mount/src/ilab_group_6_uts/models/xgb_m2.joblib'
scaler_path = '/mount/src/ilab_group_6_uts/models/scaler_minmax.joblib'

scaler_mm = load(scaler_path)
xgb_model = load(xgb_8feat_path)





# Function to initialize session state
def init_session_state():
    return st.session_state.setdefault('selected_page', 'Home')



#####============================================================GENERATE PLANS=================================================

def generate_plans(diabetes_condition, bmi, age_group, physical_health):
    # Convert diabetes condition code to string label
    if diabetes_condition == 0:
        condition = "Normal Person"
    elif diabetes_condition == 1:
        condition = "Prediabetes"
    else:
        condition = "Diabetes"
    
    # Initialize exercise and diet plans
    exercise_plan = ""
    diet_plan = ""
    
    # Determine exercise plan based on condition, age group, and physical health
    if condition == "Diabetes":
        if age_group in range(18, 25):
            if physical_health <= 10:
                exercise_plan = """
                Exercise Plan:
                - Establish a consistent exercise routine.
                - Incorporate low-impact aerobic exercises like brisk walking or cycling for at least 30 minutes a day, 5 days a week."""
            else:
                exercise_plan = """
                Exercise Plan:
                - Focus on low-impact exercises such as swimming or stationary cycling to reduce strain on joints.
                - Include strength training exercises targeting major muscle groups 2-3 days a week."""
        elif age_group in range(25, 30):
            if physical_health <= 15:
                exercise_plan = """
                Exercise Plan:
                - Combine aerobic exercises with strength training to improve overall fitness.
                - Include high-intensity interval training (HIIT) workouts for cardiovascular health."""
            else:
                exercise_plan = """
                Exercise Plan:
                - Incorporate activities like hiking or rowing for cardiovascular benefits.
                - Include strength training exercises to maintain muscle mass."""
        else:
            if physical_health <= 20:
                exercise_plan = """
                Exercise Plan:
                - Focus on a balanced exercise routine including aerobic exercises, strength training, and flexibility exercises."""
            else:
                exercise_plan = """
                Exercise Plan:
                - Consult with a fitness professional to design a personalized exercise program considering your health condition and physical limitations."""
    elif condition == "Prediabetes":
        if physical_health <= 10:
            exercise_plan = """
            Exercise Plan:
            - Focus on regular aerobic exercises such as brisk walking or cycling to improve cardiovascular health."""
        else:
            exercise_plan = """
            Exercise Plan:
            - Incorporate activities like swimming or dancing to increase physical activity levels."""
    else:
        if physical_health <= 5:
            exercise_plan = """
            Exercise Plan:
            - Emphasize regular physical activity such as walking or jogging to maintain overall health."""
        else:
            exercise_plan = """
            Exercise Plan:
            - Consider low-impact exercises like yoga or tai chi to improve flexibility and reduce stress."""
    
    # Determine diet plan based on condition and BMI
    if condition == "Diabetes":
        if bmi >= 25:
            diet_plan = """
            Diet Plan:
            - Focus on portion control and healthy food choices to manage weight.
            - Choose low-glycemic index foods and limit refined carbohydrates.
            - Examples of foods: Quinoa, leafy greens, lean proteins like chicken or fish, nuts and seeds."""
        else:
            diet_plan = """
            Diet Plan:
            - Aim for a balanced diet with a variety of nutrient-rich foods.
            - Monitor carbohydrate intake and choose complex carbohydrates.
            - Examples of foods: Whole grains like brown rice or oats, fruits, vegetables, beans, and lentils."""
    elif condition == "Prediabetes":
        if bmi >= 25:
            diet_plan = """
            Diet Plan:
            - Emphasize portion control and incorporate more fruits, vegetables, and whole grains.
            - Examples of foods: Berries, sweet potatoes, whole grain bread, quinoa, lean proteins like turkey or tofu."""
        else:
            diet_plan = """
            Diet Plan:
            - Follow a balanced diet with emphasis on portion control and regular meal timings.
            - Examples of foods: Lean proteins like chicken or fish, plenty of vegetables, whole grain pasta or bread."""
    else:
        if bmi >= 25:
            diet_plan = """
            Diet Plan:
            - Focus on weight management through portion control and regular exercise.
            - Limit intake of high-calorie and processed foods.
            - Examples of foods: Lean proteins like grilled chicken or fish, plenty of vegetables, healthy fats like avocado or olive oil."""
        else:
            diet_plan = """
            Diet Plan:
            - Emphasize a balanced diet with plenty of fruits, vegetables, lean proteins, and healthy fats.
            - Examples of foods: Leafy greens, colorful vegetables, beans and legumes, nuts and seeds, whole grains like quinoa or barley."""
    
    return exercise_plan, diet_plan





###==============================================================END GENERATE PLANS============================================


###=============================================================MAIN===============================================


          
def page_home():
    st.write('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    # Centered title using markdown and HTML
    # Centered titles
    st.markdown("<h1 style='text-align: center; font-family: Segoe UI, sans-serif'>LiveWell 🌱</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-family: Segoe UI, sans-serif'>Obesity Prevention & Diabetes Learning Platform 📚</h2>", unsafe_allow_html=True)

    # Aligned headers
    st.markdown("<h3 style='text-align: justify; font-family: Segoe UI, sans-serif'>Obesity is a major risk factor for a range of diseases, including heart disease, stroke, diabetes, and various types of cancer.</h3>", unsafe_allow_html=True)
    st.markdown("""
            <h3 style='text-align: justify; font-family: Segoe UI, sans-serif; font-size: 20px'>
            The diabetes epidemic is one of the largest and most complex health challenges Australia has faced. 
            It touches millions of lives across the country and impacts every part of our health system.
            <br><br>
            And its impact is growing. In the past 20 years, the numbers have dramatically increased by around 220%. 
            If the growth rates continue, there will be more than 3.1 million Australians living with diabetes by 2050 
            and the annual cost is forecast to grow to about $45 billion per annum in this time.
            </h3>
            """, unsafe_allow_html=True)
    
    st.title("Do you want to know your status?")
    st.header('Tell us about yourself')
    
    age = height = st.slider('Your age', 18, 90, 18)
    gender = st.radio('Your Gender',['Female','Male', 'I prefer not to answer'])
    
    # Calculate BMI with user inputted height and weight (in metric)
    height = st.slider('Insert your height in cm', 0, 230, 170)
    weight = st.slider('Insert your weight in kg', 0, 300, 70)
    
    height_m = height/100.0        
     
    
    bmi = round((weight / (height_m ** 2)), 1)
    

    #smoke = st.selectbox('Have you smoked at least 100 cigarettes in your entire life?',['Yes','No'])


    #[Note: 5 packs = 100 cigarettes] 
    #stroke = st.selectbox('(Ever told) you had a stroke.',['Yes','No'])
    #chdmi = st.selectbox('(Ever told) you had coronary heart disease (CHD) or myocardial infarction (MI)',['Yes','No'])
    #phys_act = st.selectbox('Have you done any physical activity in past 30 days - not including job?',['Yes','No'])
    #fruits = st.selectbox('Do you consume one fruit or more times per day?',['Yes','No'])
    #veggies = st.selectbox('Do you consume one vegetables or more times per day?',['Yes','No'])
    #drinker = st.selectbox('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) ',['Yes','No'])
    #health_cov = st.selectbox('Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. ?',['Yes','No'])
    #doct_vis = st.selectbox('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',['Yes','No'])
    
    
    
    st.header('Tell us about your Health')
    high_bp = st.radio('Do you have high Blood Pressure?',['Yes','No'])
    high_col = st.radio('Have you check your cholesterol level in the last 5 years?',['Yes','No'])
    drinker = st.radio('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) ',['Yes','No'])
    
    phys_act = st.radio('Have you done any physical activity in past 30 days - not including job?',['Yes','No'])
    gen_health = st.selectbox('Would you say that in general your health is',['Excellent','Very good','Good', 'Fair', 'Poor'])
    men_health = st.slider('Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? ',  0, 30, 15)
    phys_health = st.slider('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? ', 0, 30, 15)
    walk = st.radio('Do you have serious difficulty walking or climbing stairs?',['Yes','No'])
    
    
    ##===========================================================Variables conversion
    
    
    # Convert gender to numeric form
    gender_map = {'Female': 0, 'Male': 1, 'I prefer not to answer': 2}
    gender_numeric = gender_map[gender]

    # Convert age to numeric form
    
    # Classify age into categories
    if age >= 18 and age <= 24:
        age_category = 'Age 18 - 24'
    elif age >= 25 and age <= 29:
        age_category = 'Age 25 to 29'
    elif age >= 30 and age <= 34:
        age_category = 'Age 30 to 34'
    elif age >= 35 and age <= 39:
        age_category = 'Age 35 to 39'
    elif age >= 40 and age <= 44:
        age_category = 'Age 40 to 44'
    elif age >= 45 and age <= 49:
        age_category = 'Age 45 to 49'
    elif age >= 50 and age <= 54:
        age_category = 'Age 50 to 54'
    elif age >= 55 and age <= 59:
        age_category = 'Age 55 to 59'
    elif age >= 60 and age <= 64:
        age_category = 'Age 60 to 64'
    elif age >= 65 and age <= 69:
        age_category = 'Age 65 to 69'
    elif age >= 70 and age <= 74:
        age_category = 'Age 70 to 74'
    else:
        age_category = 'Age 75 or older'

    
    age_map = {'Age 18 - 24': 1, 'Age 25 to 29': 2, 'Age 30 to 34': 3, 'Age 35 to 39': 4, 
               'Age 40 to 44': 5, 'Age 45 to 49': 6, 'Age 50 to 54': 7, 'Age 55 to 59': 8,
               'Age 60 to 64': 9, 'Age 65 to 69': 10, 'Age 70 to 74': 11, 'Age 75 to 79': 12,
               'Age 80 or older': 13}
    age_numeric = age_map[age_category]

    # Calculate BMI (already numeric)

    # Convert high_bp to numeric form
    high_bp_numeric = 1 if high_bp == 'Yes' else 0

    # Convert high_col to numeric form
    high_col_numeric = 1 if high_col == 'Yes' else 0
    # Convert phys_act to numeric form
    phys_act_numeric = 1 if phys_act == 'Yes' else 0
    # Convert high_col to numeric form
    drinker_numeric = 1 if drinker == 'Yes' else 0

    # Convert gen_health to numeric form
    gen_health_map = {'Excellent': 1, 'Very good': 2, 'Good': 3, 'Fair': 4, 'Poor': 5}
    gen_health_numeric = gen_health_map[gen_health]

    # Phys_health (already numeric)

    # Convert walk to numeric form
    walk_numeric = 1 if walk == 'Yes' else 0


    input_mapping_xgb = {
                        'BMI': bmi,
                        'GenHlth': int(gen_health_numeric),
                        'HighBP': int(high_bp_numeric),
                        'Age': int(age_numeric),
                        'PhysHlth': int(phys_health),
                        #'Income': int(income_numeric),
                        'HighChol': int(high_col_numeric),
                        'MentHlth': int(men_health),
                        #'Education': int(edu_numeric),
                        'HvyAlcoholConsump': int(drinker_numeric),
                        'DiffWalk': int(walk_numeric),
                        'PhysActivity': int(phys_act_numeric)
            }

    input_df_xgb = pd.DataFrame([input_mapping_xgb])
    input_scaled = scaler_mm.transform(input_df_xgb)
    
    preds_val_xgb = xgb_model.predict(input_scaled)
    workout_plan, diet_plan = generate_plans(preds_val_xgb, bmi, age, phys_health)

    if st.button('Calculate Diabetes'):
     
        
        if int(preds_val_xgb) == 0:
            result = "<span style='color:green;'>Your Health looks great! You do not appear to be at risk for diabetes 🥗</span>"
        else:
            result = "<span style='color:red;'>You Health need attention. You are at risk of having Diabetes and you should visit a doctor ❗️</span>"

        st.subheader('Model Predictions')
        st.markdown(result, unsafe_allow_html=True)
        st.write("*The results of the model do not replace a Medical appointment. If you have any doubts you should visit your doctor.")
        
        bmi_categories = {"Underweight": [0.0, 18.49], "Normal weight": [18.5, 24.9], "Pre-obesity": [25.0, 29.9], 
                          "Obesity class II":[35.0, 39.9], "Obesity class III": [40.0, 100]}
        bmi_df = pd.DataFrame(bmi_categories, index = ['min weight', 'max weight'])
        st.write(f"Your BMI is: {bmi}")


        fig = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = bmi,
            mode = "gauge+number",
            title = {'text': "BMI"},
            gauge = {'axis': {'range': [None, 60]},
                    'bar': {'color': "darkblue"},
                    'steps' : [
                        {'range': [0, 18.5], 'color': "royalblue"},
                        {'range': [18.5, 25], 'color': "green"},
                        {'range': [25, 30], 'color': "yellow"},
                        {'range': [30, 40], 'color': "orange"},
                        {'range': [40, 60], 'color': "red"}]}))
        st.plotly_chart(fig, use_container_width=True)  
        
    
    
    
####===============================================================Recommendation button===============================
    if st.button('Diet Recommendations'):
        st.write(diet_plan)

    if st.button('Workout Recommendations'):
        st.write(workout_plan)   

    


def page_results():
    st.title("Know your status")
    st.write('Results based on ML models trained')
    
def page_recommendations():
    st.title("Recommendations")
    st.write('Find recommendations based on the results')
    

    
#def page_explore():
#    st.title("Explore Obesity in the World/Australia")
#    st.write('Explore data of obesity around the world and show how the person is in relation to the world/Australia')
    
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

          
          




          
          
