import numpy as np
import pandas as pd
import requests
import io 
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline  
from sklearn.linear_model import (LinearRegression)


def agedataframe(age):
  url = ""
  download = requests.get(url).content
  df = pd.read_csv(io.StringIO(download.decode('utf-8')))
  
  df = pd.read_csv("AgeCOVID-19DeathsData.csv") 
  df.drop(df[df['Age Group'] != user].index, inplace = True) # Dropping death counts data for all age groups except the one selected by user
  columns = df.columns
  first = columns.get_loc("COVID-19 Deaths")
  second = columns.get_loc("Total Deaths")
  deaths = np.array([ ])
  totaldeaths = np.array([ ])
  
  # Storing death counts in arrays
  i = 0
  week = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]).reshape(-1,1)
  while i < len(df.index): 
     deaths = np.append(deaths, df.iloc[i, first]) # Need to access index[i][first]
     totaldeaths = np.append(totaldeaths, df.iloc[i, second]) #[i][second ]
     i += 1
  deaths = deaths.reshape(-1,1)
  totaldeaths = totaldeaths.reshape(-1,1)
  numericdeaths = np.array([i[0] for i in deaths]) # converting all strings to floats
  numerictotal = np.array([i[0] for i in totaldeaths]) # converting all strings to floats
  
  # Implementing a linear regression model to predict COVID-19 deaths for a certain week
  model = make_pipeline(PolynomialFeatures(3), LinearRegression())
  fittingmodel = model.fit(week, numericdeaths) #polynomial regression model
  y_plot = model.predict(week[:, np.newaxis].reshape(-1,1))
  length = len(week)
  covid = int(model.predict(week[length-2].reshape(-1,1)))
  
  # Using total deaths data to calculate the scale factor that COVID-19 increases or decreases the number of deaths for an age group by
  alldeaths = int(numerictotal[length-1].reshape(-1,1))
  probability = int((covid/alldeaths)*100) # covid-19 deaths / total deaths(including covid-19) 
  return probability 
agedataframe(age)
