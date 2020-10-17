# -*- coding: utf-8 -*-
"""LocationgGraphs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p-LafqdUyMRlZXL_BUTLnDmEXEBzIl5_
"""

def locationgraph(state):
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  from numpy.random import rand
  state_abbrev = {"Alabama" : "al", "Alaska" : "ak", "Arizona": "az", "Arkansas": "ar", "California": "ca","Colorado": "co","Connecticut": "ct", "Delaware": "de","Florida": "fl","Georgia":"ga","Hawaii": "hi","Idaho":"id","Illinois": "il", "Indiana": "in","Iowa":"ia", "Kansas": "ks","Kentucky": "ky","Louisiana": "la","Maine": "me", "Maryland": "md", "Massachusetts": "ma", "Michigan": "mi", "Minnesota": "mn", "Mississippi":"ms","Missouri": "mo", "Montana": "mt","Nebraska": "ne","Nevada": "nv","New Hampshire": "nh","New Jersey": "nj","New Mexico": "nm","New York": "ny","North Carolina": "nc","North Dakota": "nd","Ohio": "oh","Oklahoma":"ok","Oregon": "or","Pennsylvania": "pa" ,"Rhode Island": "ri","South Carolina": "sc","South Dakota": "sd", "Tennessee": "tn", "Texas": "tx","Utah": "ut","Vermont": "vt","Virginia": "va", "Washington": "wa","West Virginia": "wv", "Wisconsin": "wi", "Wyoming": "wy"}
  getState = state_abbrev.get(state)

  csv_url = "https://covidtracking.com/api/v1/states/"+getState+"/daily.csv"

  #Reading the file
  df = pd.read_csv(csv_url)

  #Here, I used the pandas package to convert any NaN values to O for consistency.
  df = df.apply(pd.to_numeric,errors='coerce')
  df = df.replace(np.nan,0)

  #At this point in the code, I edited the code so the x values (the date) is only restricted to the begginning and end of the specific month the use requested for.
  rawx = df.get("date")

  #Here, I reversed the dataset, so the date data sets starts from March instead of August.
  resX = rawx[::-1]

  #I re-shaped the x data set here to get the two dimensions.
  XX = np.array(resX)
  x = XX.reshape(-1,1)

  #Here, I used the "get" function to retrieve the deaths column for the y value.
  rawy = df.get("death")
  Y = rawy[::-1]
  y = np.array(Y)

  #Here, I defined a function, graph, to plot the scatter plot for the x and y values. (date vs. deaths)
  def graph():
    for element in y:
      plt.scatter(x,y)

  #importing Linear Regression libraries
  from sklearn.linear_model import LinearRegression

  #Now, here, I imported the PolynomialFeatures library to plot the same data as the Linear Regression to a Polynomial Graph
  from sklearn.preprocessing import PolynomialFeatures 

  #Here, I entered the degree manually as 2. However, I am confused on whether I should keep this value manually harcoded, user should input, or if there is a way
  #the program itself can create a degree by prediction or a specific function.
  poly = PolynomialFeatures(degree = 4)
  X_poly = poly.fit_transform(x) 



  #Fitting the function
  #poly.fit(X_poly, y) 
  lin2 = LinearRegression() 
  lin2.fit(X_poly, y)

  #Plotting the scatter plot
  plt.scatter(x, y, color = 'red') 

  #Plotting the Polynomial Function
  plt.plot(x, lin2.predict(poly.fit_transform(x)), color = 'blue') 

  #Defining the labels
  plt.title('Location: Deaths In Total') 
  plt.xlabel('Date') 
  plt.ylabel('Deaths') 

state = input("Enter your state")
locationgraph(state)

