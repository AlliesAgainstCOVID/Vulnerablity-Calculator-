import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.graph_objects as go
from PIL import Image
import custom_gauge as cg
import Age_Code as ag
import Gender_Code as gen
import Race_Code as rc
import Location_Code as loc
import locationggraphs as locgraphs

#This does not seem to be working - It would be good to see if can be made to worl - will solve our isue of opening the app in mobils & desktop - AH-10/17
#st.beta_set_page_config(
#        page_title="AI-19: COVID-19 Mortality Risk Predictor",
#        page_icon="🧊",
#        layout="wide",
#        initial_sidebar_state="auto",
#  )

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
st.sidebar.header ("Select your inputs:")


gender = st.sidebar.selectbox("Select Gender",("Male", "Female"))
age = st.sidebar.selectbox("Select Age group",("Under 1 year", "1-4 years", "5-14 years", "15-24 years", "25-34 years", "35-44 years", "45-54 years", "55-64 years", "65-74 years", "75-84 years", "85 years and over"))
race = st.sidebar.selectbox("Select your Race",("White", "Black", "Asian", "LatinX", "American Indian/Alaskan Native", "Native Hawaiian and Pacific Islander", "Multi-Racial"))
state = st.sidebar.selectbox("Select your state",("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut","Delaware","Florida", "Georgia","Hawaii",
            "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
            "New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
            "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"))

st.sidebar.subheader ("Do you:")
st.text ("")
NPI1 = st.sidebar.checkbox ("Practice social distancing?")
NPI2 = st.sidebar.checkbox ("Wear mask in public spaces?")
st.sidebar.subheader ("Does your state:")
st.text ("")
NPI3 = st.sidebar.checkbox ("Restrict mass gatherings?")
NPI4 = st.sidebar.checkbox  ("Limit business re-openings?")#("Non-essential business closures?")
NPI5 = st.sidebar.checkbox ("Take measures to isolate symptomatic individuals and their contacts?")			      

#GENDER CODE(FRONT END AND BACK END INTEGRATION)
def output_gender():
	probability = gen.gender_data(gender)
	return probability 
gender_output = output_gender()

#RACE CODE(FRONT END AND BACK END INTEGRATION)
def output_race():
	probability = rc.functiontouse(race)
	return probability
race_output = output_race()

#AGE CODE(FRONT END AND BACK END INTEGRATION)
def output_age():
	probability = ag.agedataframe(age)
	return probability 
age_output = output_age()

# LOCATION CODE(FRONT END AND BACK END INTEGRATION) 
def output_location():
	probability = loc.location_data(state) 
	return probability
location_output = output_location()

#LocationGraphs (commented for now)

#def locationGraph():
	#locgraph = locgraphs.locationgraph(state)
	#return locgraph
#printlocgraph = locationGraph()

# NPI CODE(FRONT END AND BACK END INTEGRATION)
def output_NPI():
        data = None
        if NPI1 == 1 & NPI2 == 1 & NPI3 == 1 & NPI4 == 1 & NPI5 == 1:
            data = 0.18
        else:
            data = 1
        b = data
        return b
NPI_output = output_NPI()

#FINAL PROBABILITY CALCULATION
def aggregate_calc():
    data = (((age_output + gender_output + race_output + location_output)/4)*NPI_output)
    final_probability = data
    return final_probability
finalprob = aggregate_calc()

#st.title ("AI-19: COVID-19 Mortality Risk Predictor")
#st.write("")
#st.write("To get the results of your COVID-19 mortality risk, please fill out the fields in the left sidebar.")

#imageLocation = st.empty()
#imageone = Image.open('AI_19_image_05.jpg')
#imageLocation.image (imageone, caption='A COVID-19 Mortality Risk Predictor', use_column_width=True)


if st.sidebar.button('Submit'):
    imageLocation = st.empty()
    imagesubmit = Image.open('AI_19logo.jpg')
    imageLocation.image (imagesubmit)
    st.title ("AI-19: Your COVID-19 Mortality Rate")
    #st.markdown(""" <h1 style='text-align: center; color: blue;'>Your COVID-19 Mortality Rate</h1> """, unsafe_allow_html=True)
    cg.render_gauge((int(finalprob))) #output_df3
    #AGE PERSONALIZED MESSAGE. 
    if NPI2 == 0 and age != "Under 1 year":
        st.markdown(""" * We strongly urge you to please start wearing masks when going out to public areas. According to the CDC, multiple studies indicate masks can prevent the spread of respiratory droplets from the mouth, nose, and parts of the face. This is for your safety and others.
        Learn more here: 
	https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/cloth-face-cover-guidance.html """, unsafe_allow_html=True)
    else:
        st.write("* Please continue to follow social distancing guidelines and wear a mask in public. If you experience any symptoms, please isolate yourself and get tested as soon as possible. If you have any underlying medical conditions, it’s recommended to talk with your healthcare provider for working on a care plan to help in case of emergencies during the pandemic.")
    if age == "65-74 years" or age == "75-84 years" or age == "85 years and over":
        st.markdown(""" * Statistical analysis on CDC Data shows that older age groups 65 years and above are more vulnerable to COVID-19, and these findings are consistent with sources such as the World Health Organization.
	To minimize mortality risk as much as possible, please make sure to limit interactions with other people and travelling to gatherings or outside environments like care facilities.
	Learn more here: 
	https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/older-adults.html """, unsafe_allow_html=True)
else:
    st.title ("AI-19: COVID-19 Mortality Risk Predictor")
    st.write("")
    st.write(" To get the results of your COVID-19 mortality risk, please enter your details in the left sidebar. ")	
    imageLocation = st.empty()
    imageone = Image.open('AI_19_image_05.jpg')
    imageLocation.image (imageone, use_column_width=True)
	
# Code for disclaimer and contact info to be displayed on the UI
st.write("")
st.markdown(""" <h6 style = 'color: grey; font-size: small font-style: italic'> Disclaimer:  Please note that the information in this web app is for educational purposes only. Although it has involved content from medical professionals, it has not been endorsed by any doctor/healthcare provider. </h6> """, unsafe_allow_html=True)
st.write("")
st.markdown(""" <h4 style = 'color: black; text-align: center'><b> Contact us: alliesagainstcovid@gmail.com </b></h4> """, unsafe_allow_html=True)
fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", value = finalprob,
    gauge = {
    'shape': "bullet"},
    #'axis': {'range': [None, 100]},
    #value = output_df3,
    #delta = {'reference': 100},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Score"}))
fig.update_layout(height = 100)
#fig.show()
#st.write(fig)
#end of code

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
