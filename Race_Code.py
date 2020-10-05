import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("Covid_AGRAJ-master/RaceDeathCOVIDFinal.csv")

white_population = 160626928
black_population = 31140331
latinx_population = 41884672
asian_population = 15221807
aian_population = 1818958
nhpi_population = 448851
multiracial_population = 4158826

def white(input):
 f = df["Deaths_White"].groupby(df["Deaths_White"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/white_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)

 
def black(input):
 f = df["Deaths_Black"].groupby(df["Deaths_Black"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/black_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)


def latinx(input):
 f = df["Deaths_LatinX"].groupby(df["Deaths_LatinX"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/latinx_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)

 
def asian(input):
 f = df["Deaths_Asian"].groupby(df["Deaths_Asian"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/asian_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)

 
def aian(input):
 f = df["Deaths_AIAN"].groupby(df["Deaths_AIAN"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/aian_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)
 
 
def nhpi(input):
 f = df["Deaths_NHPI"].groupby(df["Deaths_NHPI"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/nhpi_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)
 
 
def multiracial(input):
 f = df["Deaths_Multiracial"].groupby(df["Deaths_Multiracial"].index // 56).sum()
 a = f.astype(np.int)
 normalized = []
 for i in range (34):
     t = a[i]/multiracial_population
     normalized.append(t*100)
 days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]).reshape(-1,1)

 model = LinearRegression()
 fittingmodel = model.fit(days, normalized) #fitting data with a Linear regression line 
 y_plot = model.predict(days[:, np.newaxis].reshape(-1,1))


 probability = (y_plot[33]*100)
 return(probability)
 
 
 
#MAIN PROGRAM STARTS HERE!!!!!!!!!

if (input = white):
 white(0)
if (input = black):
 black(0)
if (input = latinx):
 latinx(0)
if (input = asian):
 asian(0)
if (input = aian):
 aian(0)
if (input = nhpi):
 nhpi(0)
if (input = multiracial):
 multiracial(0)
