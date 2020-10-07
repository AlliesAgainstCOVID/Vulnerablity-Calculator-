import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.graph_objects as go
from PIL import Image
import custom_gauge as cg

#image = Image.open('AI_19_image.jpg')
#st.image (image, caption='A COVID-19 Mortality Risk Predictor', use_column_width=True)
#st.image (image, caption='A COVID-19 Mortality Risk Predictor', width=None)
st.beta_set_page_config(
	layout="wide",
	initial_sidebar_state="expanded"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
st.sidebar.subheader ("Select your inputs")


#st.sidebar(fixed=True)
#st.set_page_config(initial_sidebar_state="expanded")
#st.sidebar.header ("Select your inputs")
#st.sidebar.subheader ("Select your inputs")

# A st.sidebar.text ("")
#st.sidebar.text ("")

gender = st.sidebar.selectbox("Select Gender",("Male", "Female"))
age = st.sidebar.selectbox("Select Age group",("Under 1 year", "1-4 years", "5-14 years", "15-24 years", "25-34 years", "35-44 years", "45-54 years", "55-64 years", "65-74 years", "75-84 years", "85 years and over"))
race = st.sidebar.selectbox("Select your Race",("White", "Black", "Asian", "LatinX", "American Indian/Alaskan Native", "Native Hawaiian and Pacific Islander", "Multi-Racial"))
state = st.sidebar.selectbox("Select your state",("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colarado", "Connecticut","Delaware","Florida", "Georgia","Hawaii",
            "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
            "New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
            "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"))
# A st.sidebar.text ("")
# A st.sidebar.text ("")

#st.sidebar.text ("Does your state do the following?")
st.text ("")
st.sidebar.subheader ("Does your state do the following?")
NPI1 = st.sidebar.checkbox ("Practice social distancing?")
NPI2 = st.sidebar.checkbox ("Mandatory Mask-wearing in public spaces?")
NPI3 = st.sidebar.checkbox ("School closures?")
NPI4 = st.sidebar.checkbox ("Mass gathering restrictions?")
NPI5 = st.sidebar.checkbox ("Non-essential business closures?")
NPI6 = st.sidebar.checkbox ("Stay at home orders (with exemptions)?")
NPI7 = st.sidebar.checkbox ("Measures to isolate symptomatic individuals and their contacts?")

# A st.sidebar.text ("")
# A st.sidebar.text ("")

def user_input_features():
        data = {'gender': gender,
                'age': age,
                'race': race,
                'state': state,
                'NPI1': NPI1,
                'NPI2': NPI2,
                'NPI3': NPI3,
                'NPI4': NPI4,
                'NPI5': NPI5,
                'NPI6': NPI6,
                'NPI7': NPI7}
        features = pd.DataFrame (data,index=[0])
        return features

input_df = user_input_features()

def output_gender():
       data = None
       if gender == 'Male':
               data = 12.19
       else:
               data = 11.73
       x = data
       return x
output_df1 = output_gender ()

def output_race():
        data = None
        if race == 'White':
            data = 4.85
        elif race == 'Black':
            data = 10.38
        elif race == 'Asian':
            data = 4.15
        elif race == 'LatinX':
            data = 5.08
        elif race == 'American Indian/Alaskan Native':
            data = 6.56
        else:
            data = 7.83
        y = data
        return y
output_df2 = output_race()

def output_age():
        data = None
        if age == '0-24':
            data = 0.60
        elif age == '25-34':
            data = 1.68
        elif age == '35-44':
            data = 5.03
        elif age == '45-54':
            data = 7.52
        elif age == '55-64':
            data = 8.92
        elif age == '65-74':
            data = 9.15
        elif age == '75-84':
            data = 9.04
        else:
            data = 7.61
        a = data
        return a
output_df4 = output_age()

def output_NPI():
        data = None
        if NPI1 == 1 & NPI2 == 1 & NPI3 == 1 & NPI4 == 1 & NPI5 == 1 & NPI6 == 1 & NPI7 == 1:
            data = 0.18
        else:
            data = 1
        b = data
        return b
output_df5 = output_NPI()

def output_state():
        data = None
        if state == 'Alabama':
            data = 5.52
        elif state == 'Alaska':
            data = 1.14
        elif state == 'Arizona':
            data = 8.77
        elif state == 'Arkansas':
            data = 2.68
        elif state == 'California':
            data = 6.32
        elif state == 'Colorado':
            data = 8.54
        elif state == 'Connecticut':
            data = 30.24
        elif state == 'Delaware':
            data = 12.88
        elif state == 'Florida':
            data = 5.77
        elif state == 'Georgia':
            data = 8.83
        elif state == 'Hawaii':
            data = 0.51
        elif state == 'Idaho':
            data = 2.40
        elif state == 'Illinois':
            data = 14.22
        elif state == 'Indiana':
            data = 9.47
        elif state == 'Iowa':
            data = 6.10
        elif state == 'Kansas':
            data = 2.76
        elif state == 'Kentucky':
            data = 3.30
        elif state == 'Louisiana':
            data = 16.79
        elif state == 'Maine':
            data = 1.81
        elif state == 'Maryland':
            data = 13.47
        elif state == 'Massachusetts':
            data = 27.02
        elif state == 'Michigan':
            data = 13.68
        elif state == 'Minnesota':
            data = 7.74
        elif state == 'Mississippi':
            data = 9.31
        elif state == 'Missouri':
            data = 4.13
        elif state == 'Montana':
            data = 1.03
        elif state == 'Nebraska':
            data = 4.12
        elif state == 'Nevada':
            data = 6.03
        elif state == 'New Hampshire':
            data = 6.80
        elif state == 'New Jersey':
            data = 34.52
        elif state == 'New Mexico':
            data = 6.95
        elif state == 'New York':
            data = 48.16
        elif state == 'North Carolina':
            data = 4.87
        elif state == 'North Dakota':
            data = 2.81
        elif state == 'Ohio':
            data = 6.08
        elif state == 'Oklahoma':
            data = 2.97
        elif state == 'Oregon':
            data = 1.75
        elif state == 'Pennsylvania':
            data = 11.64
        elif state == 'Rhode Island':
            data = 20.52
        elif state == 'South Carolina':
            data = 5.50
        elif state == 'South Dakota':
            data = 3.32
        elif state == 'Tennessee':
            data = 2.62
        elif state == 'Texas':
            data = 5.22
        elif state == 'Utah':
            data = 2.86
        elif state == 'Vermont':
            data = 2.21
        elif state == 'Virginia':
            data = 6.33
        elif state == 'Washington':
            data = 5.63
        elif state == 'West Virginia':
            data = 1.49
        elif state == 'Wisconsin':
            data = 3.66
        else:
            data = 1.19
        c = data
        return c
output_df6 = output_state() 

def aggregate_calc():
    data = (((output_df1+output_df2+output_df4+output_df6)/4)*output_df5)
    z = data
    return z
output_df3 = aggregate_calc()

# A st.sidebar.text ("")
# A st.sidebar.text ("")

# A st.subheader ('User inputs:')
# A st.write(input_df)

# A st.text ("")
# A st.text ("")


imageLocation = st.empty()

imageone = Image.open('AI_19_image_01.jpg')
st.imageone (image, caption='A COVID-19 Mortality Risk Predictor', width=None)
im_resizedone = imageone.resize((image.width, 300))
imageLocation.image (imageone, caption='A COVID-19 Mortality Risk Predictor', use_column_width=True)

if st.sidebar.button('Submit'):
        imagetwo = Image.open('2AI_19_image_01.jpg')
        im_resizedtwo = imagetwo.resize((imagetwo.width, 100), (imagetwo.height, 100)) #comment this if it doesn't work
        imageLocation.imagetwo (im_resizedtwo, caption='A COVID-19 Mortality Risk Predictor', use_column_width=True)
        # AH - This did not work st.subheader('Your Mortality Rate')
        #st.write(""" ### Mortality Rate: """)
        st.markdown(""" <h1 style='text-align: center; color: red;'>Your Mortality Rate</h1> """, unsafe_allow_html=True)  #AH: I would like to make this work, not sure what's incorrect here....
        cg.render_gauge((int(output_df3)))
        #st.write(cg.render_gauge((int(output_df3))))
	#AGE PERSONALIZED MESSAGE. 
	if age == "65-74 years" or age == "75-84 years" or age == "85 years and over":
                st.markdown(""" Statistical analysis on CDC Data shows that older age groups 65 years and above are more vulnerable to COVID-19, and these findings are consistent with sources such as the World Health Organization. To minimize mortality risk as much as possible, please make sure to limit interactions with other people and travelling to gatherings or outside environments like care facilities. If you have any underlying medical conditions, it’s also recommended to talk with your doctor and healthcare provider for working on a care plan that can help for emergencies during the pandemic. 
                Learn more here: 
	        https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/older-adults.html """, unsafe_allow_html=True)
	else:
		st.write("Please  continue to social distance and wear a mask in public. Keep at least 6 feet between you and others at all times. Do not be within contact for longer than 10 minutes. If you experience any symptoms, please isolate yourself and get tested as soon as possible.")
		image2 = Image.open('DontWaitSelfIsolate_01.jpg')	 
        	im_resized2 = image2.resize((image2.width, 100)) #AH - I am not sure why this is erroring out as "inconsistent use of tabs and spaces in indentation"
		st.image2(im_resized2, use_column_width=True) #AH - I am not sure why this is erroring out as "inconsistent use of tabs and spaces in indentation"
#cg.render_gauge((int(output_df3))

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", value = output_df3,
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

