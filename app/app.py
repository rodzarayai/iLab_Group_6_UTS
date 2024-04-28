import streamlit as st
import pandas as pd
from joblib import load
import datetime
import os
import xgboost as xgb
import plotly.graph_objects as go
from all_obesity_charts import chart_all




# -- Set page config
apptitle = 'HealthScope'

st.set_page_config(page_title=apptitle, 
                   page_icon="⚕️",
                   initial_sidebar_state='collapsed')
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.ibb.co/yVrV6Qv/back1.jpg");
background-size: 100%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
background-attachment: fixed
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#ML model
#xgb_8feat_path = '../models/xgb_m2.joblib'
#scaler_path = '../models/scaler_minmax.joblib'

#ML model
xgb_8feat_path = '/mount/src/ilab_group_6_uts/models/xgb_m2.joblib'
scaler_path = '/mount/src/ilab_group_6_uts/models/scaler_minmax.joblib'

scaler_mm = load(scaler_path)
xgb_model = load(xgb_8feat_path)

#scaler_mm = load(scaler_path)
#xgb_model = load(xgb_8feat_path)





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
    # Title
    left_co, cent_co, last_co = st.columns(5)
    with cent_co:
        st.image('/mount/src/ilab_group_6_uts/app/app_logo.png', width=400)


    # Aligned headers
    st.markdown("<h2 style='text-align: center; font-size: 20px'>Discover a healthier you by understanding your risk of obesity and Type 2 diabetes. Our <u>quick questionnaire</u> will unlock personalised insights into your health and lifestyle choices.</h2>", unsafe_allow_html=True)
    st.markdown("""
            <h2 style='text-align: center; font-size: 20px'>
            <b>Act now</b>— Understand your risks, transform your habits, and start your journey to a healthier life today! 
            </h2>
            """, unsafe_allow_html=True)
    st.markdown("""
            <h2 style='text-align: center; font-size: 70px; font-family: Times New Roman'>
            ⬇️
            </h2>
            """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<h2 style='text-align: left; font-size: 15px; font-style: italic'>*DISCLAIMER: No user information is stored on the app or website</h2>", unsafe_allow_html=True)
    st.header('Tell us about yourself')
    # Adjusting sizes of radio box texts
    st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
}
    </style>
    """, unsafe_allow_html=True)
    # Adjusting sizes of number input texts
    st.markdown(
    """<style>
div[class*="NumberInput"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
}
    </style>
    """, unsafe_allow_html=True)
    # Adjusting sizes of slider texts
    st.markdown(
    """<style>
div[class*="Slider"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
}
    </style>
    """, unsafe_allow_html=True)
    age = st.slider('Enter your age', 18, 90, 18)
    gender = st.radio('Select your gender',['Female','Male', 'I prefer not to answer'])
    
    
    # Calculate BMI with user inputted height and weight (in metric)
    height = st.slider('Enter your height in Centimetres:', 0, 230, 170)
    weight = st.slider('Enter your weight in Kilograms:', 0, 300, 70)
    
    height_m = height/100.0  

    bmi = round((weight / (height_m ** 2)), 1) if height_m != 0 else st.warning("Height cannot be zero. Please enter a valid height value.")

   

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
    
    
    st.divider()

    st.header('Tell us about your health status')
    high_bp = st.radio('Do you have high blood pressure?',['Yes','No'])
    high_col = st.radio('Have you check your cholesterol level in the last 5 years?',['Yes','No'])
    drinker = st.radio('Do you consider yourself a heavy drinker? ',['Yes','No'])
    drinker_info = 'Definition for a heavy drinker is an adult man having more than 14 drinks per week and an adult woman having more than 7 drinks per week'
    #HTML box ⓘ
    st.markdown(f'<span title="{drinker_info}">ℹ️</span>', unsafe_allow_html=True)
    
    phys_act = st.radio('Have you done any physical activity in past 30 days - not including your job?',['Yes','No'])
    gen_health = st.selectbox('What would you say your health status is in general?',['Excellent','Very good','Good', 'Fair', 'Poor'])
    men_health = st.slider('How many days in the past 30 days did you feel metnally unwell?',  0, 30, 15)
    men_health_info = "Mental health includes stress, depression, and all problems connected with emotions etc."
    # HTML box
    st.markdown(f'<span title="{men_health_info}"> ℹ️ </span>', unsafe_allow_html=True)

    phys_health = st.slider('How many days in the past 30 days did you feel physically unwell?', 0, 30, 15)
    phys_health_info = "Physical health includes all types of physical injuries and illnesses."
    #HTML box
    st.markdown(f'<span title="{phys_health_info}"> ℹ️ </span>', unsafe_allow_html=True)
    walk = st.radio('Do you have serious difficulty walking or climbing stairs?',['Yes','No'])

    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
     
    st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #379683;">
  <a class="navbar-brand" target="_blank">HealthScope</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="https://www.uts.edu.au/about/td-school" href="#">TD school <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.uts.edu.au/" target="_blank">UTS</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Master of Data Science and Innovation 2024</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
    
    
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
    elif age >= 75 and age <= 79:
        age_category = 'Age 70 to 74'
    else:
        age_category = 'Age 80 or older'

    
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

    if 'diabetes' not in st.session_state:
        st.session_state.diabetes = False

    if st.button('Calculate Results') or st.session_state.diabetes:
        st.session_state.diabetes = True
        if int(preds_val_xgb) == 0:
            result = "<span style='color:green; font-size: 40px'>YOU'RE DOING GREAT!</span>"
            sub_text = "<h2 style='color: #2A4258; text-align: justify; font-size: 20px;'>You do not seem to have an obesity problem or to be at risk for diabetes 🥗.</h2>"
        else:
            result = "<span style='color:red; font-size: 40px;'>YOUR HEALTH NEEDS ATTENTION!</span>"
            sub_text = "<h2 style='color: #2A4258; text-align: justify; font-size: 20px;'>You may be at risk of obesity and diabetes. You should visit a doctor.❗️</h2>"


        st.markdown("<span style='color: #2A4258; font-size: 20px;   font-weight: bold'> Your results from our model's predictions </span>", unsafe_allow_html=True)
        st.markdown(result, unsafe_allow_html=True)
        st.markdown(sub_text, unsafe_allow_html=True)
        
        st.write("*The results of the model do not replace a Medical appointment. If you have any doubts you should visit your doctor.")
        
        bmi_categories = {"Underweight": [0.0, 18.49], "Normal weight": [18.5, 24.9], "Pre-obesity": [25.0, 29.9], 
                          "Obesity class II":[35.0, 39.9], "Obesity class III": [40.0, 100]}
        bmi_df = pd.DataFrame(bmi_categories, index = ['min weight', 'max weight'])
        st.write(f"Your BMI is: {bmi}")


        fig = go.Figure(go.Indicator(
            domain = {'x': [0.1, 0.9], 'y': [0.1, 0.9]},
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
        page_results(preds_val_xgb) 


        
    
    
    
####===============================================================Recommendation button===============================
    
    #if 'diet' not in st.session_state:
    #    st.session_state.diet = False
    #if st.button('Diet Recommendations') or st.session_state.diet:
    #    st.session_state.diet = True
    #    st.write(diet_plan)

    #if 'workout' not in st.session_state:
    #    st.session_state.workout = False
    #if st.button('Workout Recommendations') or st.session_state.workout:
    #    st.session_state.workout = True
    #    st.write(workout_plan) 

    # Create a hyperlink to page_facts()
    #if st.button('Go to facts'):
    #    page_facts_obesity() 
    
    

    

def page_results(preds_val_xgb):

    tab1, tab2 = st.tabs(["Learn More about Obesity", "Learn More about Diabetes"])
    with tab1:
        page_facts_obesity()
        if st.button("Support and Resources for Obesity"):
            page_resource_obesity()
    with tab2:
        page_facts_diabetes()
        if st.button("Support and Resources for Diabetes Types"):
            page_resource_diabetes()


def page_facts_obesity():
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Understanding Obesity</h1>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Definition:</b> Obesity is a medical condition characterised by an excessive amount of body fat, which poses a risk to health. The World Health Organization (WHO) identifies obesity as a leading preventable cause of death worldwide, impacting life expectancy negatively and increasing the incidence of health problems.</li>
        <li><b>BMI Classifications:</b> The Body Mass Index (BMI) is a key metric used by the WHO to classify weight categories. It divides weight status into four main categories: underweight (BMI less than 18.5), normal weight (BMI 18.5 to <25), overweight (BMI 25 to <30), and obese (BMI 30 or higher). Obesity is further subdivided into classes: Class I (BMI 30 to <35), Class II (BMI 35 to <40), and Class III (BMI 40 or higher), with the latter also known as "severe" or "morbid" obesity. </li>
        </ul>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left;  font-weight: bold; font-size: 25px'>Causes of Obesity</h1>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Diet:</b> The consumption of high-calorie foods, particularly those rich in sugars and fats, combined with large portion sizes, significantly contributes to the development of obesity. A diet that exceeds energy needs without sufficient physical activity leads to fat accumulation. </li>
        <li><b>Physical Inactivity:</b> A sedentary lifestyle, characterised by minimal physical activity, directly contributes to weight gain. Modern conveniences and technology have reduced the need for physical exertion in daily life, contributing to the obesity epidemic. </li>
        <li><b>Genetics:</b> Genetic predisposition plays a significant role in obesity. Individuals with a family history of obesity are at a higher risk, as genetics can influence fat storage and energy metabolism. </li>
        <li><b>Psychological Factors:</b> Emotional states such as stress and depression can lead to overeating as a coping mechanism, contributing to obesity. The relationship between emotions and eating behaviour is complex and multifaceted. </li>
        <li><b>Environmental Factors:</b> The environment, including access to healthy foods and safe areas for exercise, significantly affects lifestyle choices and obesity risk. Socioeconomic factors can influence diet and physical activity levels.</li>
        <li><b>Medicines:</b> Certain medications can lead to weight gain by altering the body's energy balance or increasing appetite. Medications for diabetes, depression, and high blood pressure are examples of those that can affect weight. </li>
        </ul>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left;  font-weight: bold; font-size: 25px'>Health Risks Associated with Obesity</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px;   font-weight: normal'>Obesity significantly increases the risk for numerous health conditions that can affect nearly every system in the body:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Cardiovascular Diseases:</b> Obesity contributes to heart disease and strokes, mainly through high blood pressure and abnormal cholesterol levels, posing serious risks to heart health. </li>
        <li><b>Metabolic Disorders:</b> Conditions such as type 2 diabetes and insulin resistance are closely linked to obesity, as excess body fat affects the body's ability to use insulin, leading to elevated blood sugar levels. </li> 
        <li><b>Cancer:</b> There's a heightened risk for several types of cancer, including uterine, breast, colon, and liver cancer, among others, associated with obesity.</li>
        <li><b>Digestive Issues:</b> Obesity increases the likelihood of experiencing digestive problems like heartburn, gallbladder disease, and serious liver conditions, including fatty liver disease.</li>
        <li><b>Respiratory Problems:</b> Excess weight is a key factor in the development of sleep apnoea and can contribute to other respiratory issues, impacting overall respiratory health. </li>
        <li><b>Joint and Inflammation Issues:</b> Conditions such as osteoarthritis are more common in individuals with obesity due to the increased stress on weight-bearing joints and systemic inflammation. </li>
        <li><b>Severe COVID-19 Symptoms:</b> Individuals with obesity are at a higher risk for developing more severe complications if they contract COVID-19, including increased likelihood of hospitalisation, ICU admission, and mechanical ventilation. </li>
        <li><b>Other Health Concerns:</b> Obesity also increases the risk for dyslipidaemia, kidney disease, and complications related to pregnancy, fertility, and sexual function, in addition to mental health issues like depression and anxiety and challenges with physical functioning.</li>
        </ul>""", unsafe_allow_html=True)
    
    chart_all()
    st.markdown("<h1 style='text-align: left;   font-weight: bold; font-size: 25px'>Managing and Preventing Obesity</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px;   font-weight: normal'>Effective management and prevention of obesity are critical to reducing these health risks:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Dietary Changes:</b> Adopting a balanced diet with plenty of fruits, vegetables, whole grains, and lean proteins while practising portion control and reducing the intake of sugars and saturated fats is foundational. </li>
        <li><b>Physical Activity:</b> Engaging in at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity weekly, along with muscle-strengthening exercises on two or more days a week, supports weight loss and overall health</li>
        <li><b>Behavioural Changes:</b> Healthy eating habits, regular physical activity, and effective stress management techniques are essential. Setting realistic weight loss goals can also motivate individuals toward sustained lifestyle changes. </li>
        <li><b>Medical Interventions:</b> For some, medications and surgery may be considered when significant weight loss cannot be achieved through lifestyle changes alone. These options should be discussed with healthcare professionals. </li>
        <li><b>Seeking Professional Help:</b> Consulting healthcare professionals for personalised advice and treatment options is crucial for effective obesity management and prevention. </li>
        </ul>""", unsafe_allow_html=True)

def page_facts_diabetes():
    st.markdown("<h1 style='text-align: left;   font-weight: bold; font-size: 25px'>Understanding Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Definition: </b> Type 2 diabetes is a chronic health condition where the body struggles to metabolise glucose, a crucial energy source. This form of diabetes is characterised by the body's inability to use insulin effectively, though it still produces insulin, unlike Type 1 diabetes, where insulin production is minimal or non-existent. This impairment in insulin usage leads to elevated levels of glucose in the blood.</li>
        <li><b>Prevalence:</b> It is one of the most prevalent forms of diabetes, affecting millions worldwide, and its frequency is on the rise due to factors like aging populations and increasing rates of obesity and physical inactivity. Type 2 diabetes accounts for about 90% to 95% of all diagnosed cases of diabetes in adults.</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Causes and Risk Factors</h1>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Insulin Resistance:</b> A key feature of Type 2 diabetes is the body's inefficient use of insulin, leading to insulin resistance. This condition causes glucose to accumulate in the bloodstream instead of being absorbed by the cells, significantly raising blood sugar levels.</li>
        <li><b>Obesity and Physical Inactivity:</b> These factors are strongly linked to the development of Type 2 diabetes, with obesity being a major contributor to insulin resistance. A sedentary lifestyle further exacerbates the risk, highlighting the importance of maintaining a healthy weight and engaging in regular physical activity. </li>
        <li><b>Genetics and Family History:</b> The likelihood of developing Type 2 diabetes increases if there is a family history of the disease, indicating a genetic predisposition. Shared family behaviours and lifestyles further influence this risk. </li>
        <li><b>Age, Race, and Ethnicity:</b> The risk of developing Type 2 diabetes increases with age. Additionally, certain racial and ethnic groups, including African Americans, Hispanic/Latino Americans, American Indians, and some Asian Americans and Pacific Islanders, are at a higher risk. </li>
        <li><b>Other Health Issues:</b>Conditions such as high blood pressure, abnormal cholesterol levels, and a history of gestational diabetes are associated with an increased risk of developing Type 2 diabetes. These factors underscore the interconnectedness of various health conditions and the importance of comprehensive healthcare. </li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left;   font-weight: bold; font-size: 25px'>Symptoms of Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px;   font-weight: normal'>Type 2 diabetes symptoms are often subtle and develop over time, making them easy to overlook. Key signs include:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Increased Thirst and Frequent Urination:</b> The need to expel excess glucose through urine leads to dehydration, causing increased thirst and a higher frequency of urination.</li>
        <li><b>Increased Hunger:</b> Even after eating, the body's inefficiency in using glucose can leave individuals feeling constantly hungry.</li>
        <li><b>Fatigue:</b> Energy levels drop as glucose remains in the bloodstream instead of fueling cells, resulting in tiredness.</li>
        <li><b>Blurred Vision:</b> Excess glucose can cause fluid to be drawn from the eyes, impairing vision.</li>
        <li><b>Slow-Healing Sores and Frequent Infections:</b> Elevated blood sugar levels can weaken the body's healing process and defence mechanisms.</li>
        <li><b>Numbness or Tingling:</b> High glucose levels may damage nerves, especially in the hands and feet, leading to numbness or tingling sensations.</li>
        <li><b>Unintended Weight Changes:</b> Unexpected weight loss or gain can be a consequence of disrupted glucose metabolism.</li>
        <li><b>Areas of Darkened Skin:</b>Patches of darkened skin, particularly in the armpits and neck, may signal insulin resistance.</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left;   font-weight: bold; font-size: 25px'>Managing Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px;   font-weight: normal'>Effective management of Type 2 diabetes focuses on maintaining blood sugar levels within a normal range:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Monitoring Blood Sugar:</b> Regularly checking blood sugar levels is crucial for adjusting diet, activity, and medications to manage diabetes effectively.</li>
        <li><b>Healthy Eating:</b> A diet rich in nutrients, low in fat and calories, and balanced in carbohydrates helps control blood sugar levels. Focusing on whole foods like fruits, vegetables, whole grains, and lean proteins is important.</li>
        <li><b>Physical Activity:</b> Regular physical activity helps lower blood sugar levels, boost insulin sensitivity, and maintain a healthy weight. Aim for at least 150 minutes of moderate to vigorous exercise per week.</li>
        <li><b>Medication and Insulin Therapy:</b> Many people with Type 2 diabetes require medication or insulin therapy to help manage their blood sugar levels. Adherence to prescribed treatments and close communication with healthcare providers are essential.</li>
        <li><b>Regular Checkups:</b> Ongoing medical care, including regular checkups, is important to monitor the condition and adjust treatment as necessary. This includes managing not only blood sugar but also cholesterol levels and blood pressure.</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left;   font-weight: bold; font-size: 25px'>Preventing Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px;   font-weight: normal'>Preventing Type 2 diabetes or delaying its onset is highly achievable through effective lifestyle modifications and proactive health measures:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Maintaining a Healthy Weight:</b> Excess body fat, especially around the abdomen, increases the risk of developing Type 2 diabetes. Losing even a small amount of weight if you're overweight can significantly lower your risk.</li>
        <li><b>Engaging in Physical Activity:</b> Regular physical activity helps control weight, lowers blood sugar levels, and increases insulin sensitivity. Aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week, alongside muscle-strengthening exercises on two or more days.</li>
        <li><b>Eating a Well-Balanced Diet:</b> Focus on a diet rich in fruits, vegetables, whole grains, and lean proteins. Limit intake of refined sugars and saturated fats to help maintain optimal blood sugar levels and support a healthy weight.</li>
        <li><b>Screening and Early Detection:</b> Regular screening for Type 2 diabetes is crucial, especially for those at higher risk due to factors like family history, age, overweight, and leading a sedentary lifestyle. Early detection through screening can facilitate timely interventions, such as lifestyle adjustments or medication, to prevent or delay the disease's progression. Screening recommendations can vary, but generally, adults over the age of 45 or those with risk factors should consider getting screened every 3 years.</li>
        </ul>""", unsafe_allow_html=True)



def page_resource_obesity():
    st.title('Resources and Support for Obesity')
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Trusted Information Sources:</h1>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><b>World Health Organization (WHO):</b> Discover global strategies and resources on obesity. <a href="https://www.who.int/health-topics/obesity" target="_blank">Visit WHO</a></li>
        <li><b>Centers for Disease Control and Prevention (CDC):</b> Access comprehensive information on obesity prevention and management. <a href="https://www.cdc.gov/obesity/index.html" target="_blank">Visit CDC</a></li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Support Groups and Communities:</h1>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><b>The Obesity Collective:</b> Australia’s leading coalition for obesity awareness and treatment. Connect with their cooperative network for support. <a href="https://theobesitycollective.org.au/" target="_blank">Explore The Obesity Collective</a></li>
        <li><b>Obesity Action Coalition:</b> A community offering education, tools, and resources for everyone’s journey with weight. Check their upcoming events for support opportunities. <a href="https://www.obesityaction.org/education-support/tools/" target="_blank">Find Support at Obesity Action Coalition</a></li>
        <li><b>MyObesityTeam:</b> Join the social network tailored for those living with obesity, share experiences, and receive emotional support. <a href="https://www.myobesityteam.com/" target="_blank">Connect on MyObesityTeam</a></li>
        <li><b>loseit - Reddit:</b> A Reddit community focused on healthy and sustainable weight loss methods. Share your journey and get motivated. <a href="https://www.reddit.com/r/loseit/" target="_blank">Join the conversation on Reddit</a></li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Weight Management and Loss Apps:</h1>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><b>Forbes - Top Weight Loss Apps:</b> Forbes Health editorial team provides insights on the best weight loss apps on the market, helping you choose the right tool for your journey. <a href="https://www.forbes.com/health/weight-loss/best-weight-loss-apps/" target="_blank">Read Forbes Review</a></li>
        <li><b>Healthline - Best Weight Loss Apps:</b> Check out Healthline’s selection of weight loss apps for various needs, from coaching and meal logging to grocery shopping help. <a href="https://www.healthline.com/nutrition/best-weight-loss-apps" target="_blank">See Healthline’s Picks</a></li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-weight: bold; font-style: italic'>Remember, while these resources are here to guide and support you, always consult with a healthcare professional for personalised advice and treatment plans.</h2>", unsafe_allow_html=True)
    

    
def page_resource_diabetes():
    st.title('Resources and Support for Diabetes Type 2')
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Trusted Information Sources:</h1>", unsafe_allow_html=True)
    st.markdown("""
    <ul style='text-align: justify; font-size: 20px; font-weight: normal'>
        <li><b>Centers for Disease Control and Prevention (CDC):</b> Learn about Type 2 diabetes, its risks, and management. <a href="https://www.cdc.gov/diabetes/basics/type2.html" target="_blank">Visit CDC</a></li>
        <li><b>World Health Organization (WHO):</b> Get global perspectives on diabetes care and prevention. <a href="https://www.who.int/news-room/fact-sheets/detail/diabetes" target="_blank">Visit WHO</a></li>
        <li><b>Diabetes Australia:</b> Access a wealth of resources specific to Type 2 diabetes management and care. <a href="https://www.diabetesaustralia.com.au/about-diabetes/type-2-diabetes/" target="_blank">Explore Diabetes Australia</a></li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-weight: bold; font-size: 25px'>Support Groups and Online Communities:</h1>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><b>NDSS (National Diabetes Services Scheme):</b> Find various resources to support living well with diabetes, from care to nutrition. <a href="https://www.ndss.com.au/about-diabetes/resources/" target="_blank">Access NDSS Resources</a></li>
        <li><b>Carenity:</b> Join the first social network dedicated to people with chronic conditions, offering support and information. <a href="https://www.carenity.us/who-we-are" target="_blank">Connect on Carenity</a></li>
        <li><b>DiabetesSisters:</b> A space empowering women with diabetes to manage their health and connect with others. <a href="https://diabetessisters.org/about-us" target="_blank">Learn from DiabetesSisters</a></li>
        <li><b>Diabetes Forum App:</b> Engage with a large community of people with diabetes on the UK's largest Diabetes Forum via the app. <a href="https://www.diabetes.co.uk/app/" target="_blank">Join the Diabetes Forum</a></li>
        <li><b>T2D Healthline:</b> An app offering a supportive social network for those with Type 2 diabetes, complete with live chats and community support. <a href="https://www.healthlinemedia.com/insights/t2d-healthline-resources-and-support-to-live-beyond-type-2-diabetes" target="_blank">Discover T2D Healthline</a></li>
        <li><b>Bezzy Type 2 Diabetes:</b> Find community and understanding for living with Type 2 diabetes with Healthline’s Bezzy app. <a href="https://play.google.com/store/apps/details?id=com.healthline.t2d&hl=en&gl=US" target="_blank">Get the Bezzy T2D App</a></li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-weight: bold; font-style: italic'>Remember, while these resources are here to guide and support you, always consult with a healthcare professional for personalised advice and treatment plans.</h2>", unsafe_allow_html=True)

    
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
    
 

    button_home = st.sidebar.button("🏠 Homepage - Questionaire")
    button_obesity = st.sidebar.button("📊 Learn More about Obesity")
    button_resource_obesity = st.sidebar.button("⬇️ Resources and Support tools for Obesity")
    button_facts_diabetes = st.sidebar.button("📊 Learn More about Diabetes Type 2")
    button_resource_diabetes = st.sidebar.button("⬇️ Resources and Support tools for Diabetes Type 2")
    button_team = st.sidebar.button("⭐ Meet the Team") 


    
    # Initialize session state
    init_session_state()

    # Check which button is clicked and execute the corresponding function
    if button_home:
        st.session_state.selected_page = 'Home'

    if button_obesity:
        st.session_state.selected_page = 'Learn More about Obesity'
    
    if button_resource_obesity:
        st.session_state.selected_page = 'Resources and Support tools for Obesity'

    if button_facts_diabetes:
        st.session_state.selected_page = 'Learn More about Diabetes Type 2'
    
    if button_resource_diabetes:
        st.session_state.selected_page = 'Resources and Support tools for Diabetes Type 2'
    
    if button_team:
        st.session_state.selected_page = 'Meet the Team'


    # Execute the corresponding function based on the selected page
    if st.session_state.selected_page == 'Home':
        page_home()
    elif st.session_state.selected_page == 'Learn More about Obesity':
        page_facts_obesity()
    elif st.session_state.selected_page == 'Resources and Support tools for Obesity':
        page_resource_obesity()
    elif st.session_state.selected_page == 'Learn More about Diabetes Type 2':
        page_facts_diabetes()
    elif st.session_state.selected_page == 'Resources and Support tools for Diabetes Type 2':
        page_resource_diabetes()
    elif st.session_state.selected_page == 'Meet the Team':
        page_team()


if __name__ == "__main__":
    main()
# Test 
          
          




          
          