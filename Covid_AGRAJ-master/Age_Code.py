import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline  
from sklearn.linear_model import (LinearRegression)


def agedataframe(age):
  df = pd.read_csv("Covid_AGRAJ-master/AgeCOVID-19DeathsData.csv")
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
  deaths = deaths.reshape(-1,1) # reshaping the array so that it is 2-D
  totaldeaths = totaldeaths.reshape(-1,1) # reshaping the array so that it is 2-D
  numericdeaths = np.array([i[0] for i in deaths]) # converting all strings to floats
  numerictotal = np.array([i[0] for i in totaldeaths]) # converting all strings to floats
  
  # Implementing a Polynomial Regression Model to predict COVID-19 deaths for a certain week
  model = make_pipeline(PolynomialFeatures(3), LinearRegression())
  fittingmodel = model.fit(week, numericdeaths) #fitting data with a polynomial regression line 
  y_plot = model.predict(week[:, np.newaxis].reshape(-1,1))
  length = len(week)
  covid = int(model.predict(week[length-2].reshape(-1,1)))
  
  # Using total deaths data to calculate the scale factor that COVID-19 increases or decreases the number of deaths for an age group by
  alldeaths = int(numerictotal[length-1].reshape(-1,1))
  probability = int((covid/alldeaths)*100) # covid-19 deaths / total deaths(including covid-19) 
  return probability 
agedataframe(age)
