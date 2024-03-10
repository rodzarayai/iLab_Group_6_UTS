import streamlit as st
import pandas as pd
from joblib import load




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, page_icon="⚕️")

         
          
def page_home():
    st.write('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    st.title('How lifestyle/habits can lead to obesity and diabetes type 2')

def page_survey():
    st.title("Tell us about your lifestyle/habits")


def page_results():
    st.title("Know your status")


def main():
    st.sidebar.title("Explore")
    # Create links for each page
    page_links = {
        "Home": "🏠 [Home](#home)",
        "Survey": "📝 [Survey](#survey)",
        "Know Your Status": "📊 [Know Your Status](#results)"
    }

    # Display the links in the sidebar
    selected_page = st.sidebar.markdown("\n".join(page_links.values()))

    # Check the selected link and execute the corresponding function
    if "Home" in selected_page:
        page_home()

    if "Survey" in selected_page:
        page_survey()

    if "Know Your Status" in selected_page:
        page_results()

if __name__ == "__main__":
    main()

          
          




          
          