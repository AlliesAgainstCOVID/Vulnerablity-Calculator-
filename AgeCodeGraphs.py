import numpy as np
from sklearn.linear_model import (LinearRegression)
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline        

def agedataframe(age):
  #AH- df = pd.read_csv("Covid_AGRAJ-master/AgeCOVID-19DeathsData.csv")
  df = pd.read_csv("AgeCOVID-19DeathsData.csv")
  df.drop(df[df['Age Group'] != age].index, inplace = True) # Dropping death counts data for all age groups except the one selected by user
  columns = df.columns
  first = columns.get_loc("COVID-19 Deaths")
  second = columns.get_loc("Total Deaths")
  deaths = np.array([ ])
  totaldeaths = np.array([ ])
  
  # Storing death counts in arrays
  i = 0
  week = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]).reshape(-1,1)
  while i < len(df.index): 
     deaths = np.append(deaths, df.iloc[i, first]) # reading file and storing weekly COVID-19 Deaths
     totaldeaths = np.append(totaldeaths, df.iloc[i, second]) # reading file and storing weekly total death counts(including COVID-19)
     i += 1
  deaths = deaths.reshape(-1,1) # reshaping the array so that it is 2-D
  totaldeaths = totaldeaths.reshape(-1,1) # reshaping the array so that it is 2-D
  numericdeaths = np.array([i[0] for i in deaths]) # converting all strings to floats
  numerictotal = np.array([i[0] for i in totaldeaths]) # converting all strings to floats
  
  # Implementing a Polynomial Regression Model to predict COVID-19 deaths for a certain week
  model = make_pipeline(PolynomialFeatures(3), LinearRegression())
  fittingmodel = model.fit(week, numericdeaths) #fitting data with a polynomial regression line 
  y_plot = model.predict(week[:, np.newaxis].reshape(-1,1))
  plt.figure(figsize=(10, 5))
  plt.xticks(np.arange(1, length + 1,1))
  plt.xlabel("Weeks(6/6-8/1)")
  plt.ylabel("Covid-19 Deaths")
  plt.title(user)
  plt.scatter(week, deaths)
  plt.plot(week, y_plot, 'turquoise', '-')
  carrying out the calculation 
  length = len(week)
  covid = int(model.predict(week[length-2].reshape(-1,1))) #predicting number of COVID-19 Deaths for the last week
  
  # Using total deaths data to calculate the scale factor that COVID-19 increases or decreases the number of deaths for an age group by
  alldeaths = int(numerictotal[length-1].reshape(-1,1))
  probability = int((covid/alldeaths)*100) # FORMULA: covid-19 deaths / total deaths(including covid-19) 
  return probability 

  
