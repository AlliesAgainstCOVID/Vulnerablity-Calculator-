
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 
def race_data(a):
  if (a == 1):
    Y = 0.0042137 + (0.0021101*21)
    final_race = []
    ans = Y*100
    final_race.append(ans)
    return(final_race)
  if (a == 2):
    Y = 0.012551 + (0.004345*21)
    final_race = []
    ans = Y*100
    final_race.append(ans)
    return(final_race)
  if (a == 3):
    Y = 9.1616e-05 + (0.0024151*21)
    final_race = []
    ans = Y*100
    final_race.append(ans)
    return(final_race)
  if (a == 4):
    Y = 0.0038881 + (0.0017926*21)
    final_race = []
    ans = Y*100
    final_race.append(ans)
    return(final_race)
  if (a == 5):
    Y = -0.0065058 + (0.0034341*21)
    final_race = []
    ans = Y*100
    final_race.append(ans)
    return(final_race)
  if (a == 6):
    Y = 0.048139 + (0.0014339*21)
    final_race = []
    ans = Y*100
    final_race.append(ans)
    return(final_race)
 
race = input("Enter your race: \n")
race_date(race)

