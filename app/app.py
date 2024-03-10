import streamlit as st
import pandas as pd
from joblib import load




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, page_icon="⚕️")

         
          
def page_home():
    st.header('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    st.title('How lifestyle/habits can lead to obesity and diabetes type 2')

def page_survey():
    st.title("Tell us about your lifestyle/habits")


def page_results():
    st.title("Know your status")


def main():
    st.sidebar.title("Navigation")

    selected_page = st.sidebar.button("Home")
    if selected_page:
        page_home()

    selected_page = st.sidebar.button("Survey")
    if selected_page:
        page_survey()

    selected_page = st.sidebar.button("Know your status")
    if selected_page:
        page_results()
    

if __name__ == "__main__":
    main()

          
          




          
          