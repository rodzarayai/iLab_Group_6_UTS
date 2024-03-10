import streamlit as st
import pandas as pd
from joblib import load




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, page_icon="⚕️")

         
          
def page_home():
    st.header('36105 iLab: Capstone Project - Autumn 2024 - UTS)
    # Title
    st.title('How lifestyle/habits can lead to obesity and diabetes type 2')

def page_survey():
    st.title("Tell us about your lifestyle/habits")


def page_results():
    st.title("Know your status")


def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": page_home,
        "Survey": page_survey,
        "Know your status": page_results,
    }

    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page
    pages[selected_page]()

if __name__ == "__main__":
    main()

          
          




          
          