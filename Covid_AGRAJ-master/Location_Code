import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
 
def location_data(b):
 
    ask_state = input("What state do you live in?\n")
 
    state_abbrev = {"Alabama" : "al", "Alaska" : "ak", "Arizona": "az", "Arkansas": "ar", "California": "ca","Colorado": "co","Connecticut": "ct", "Delaware": "de","Florida": "fl","Georgia":"ga","Hawaii": "hi","Idaho":"id","Illinois": "il", "Indiana": "in","Iowa":"ia", "Kansas": "ks","Kentucky": "ky","Louisiana": "la","Maine": "me", "Maryland": "md", "Massachusetts": "ma", "Michigan": "mi", "Minnesota": "mn", "Mississippi":"ms","Missouri": "mo", "Montana": "mt","Nebraska": "ne","Nevada": "nv","New Hampshire": "nh","New Jersey": "nj","New Mexico": "nm","New York": "ny","North Carolina": "nc","North Dakota": "nd","Ohio": "oh","Oklahoma":"ok","Oregon": "or","Pennsylvania": "pa" ,"Rhode Island": "ri","South Carolina": "sc","South Dakota": "sd", "Tennessee": "tn", "Texas": "tx","Utah": "ut","Vermont": "vt","Virginia": "va", "Washington": "wa","West Virginia": "wv", "Wisconsin": "wi", "Wyoming": "wy"}
 
    state = state_abbrev.get(ask_state)
    
    #state = input("Please enter the abbreviated form of your state in a lowercase format: \n")
    csv_url = "https://covidtracking.com/api/v1/states/"+state+"/daily.csv"
 
    totaldeaths = {"al": 29611, "ak": 2068, "az": 38945, "ar": 17293, "ca": 153910 , "co": 23447, "ct": 18372, "de": 5377, "fl": 121463, "ga": 47625, "hi": 6074, "id": 7719, "il": 65073, "in": 37404, "ia": 16424, "ks": 14288, "ky": 25005, "la": 27401, "me": 7952, "md": 31280, "ma": 38972, "mi": 58931, "mn": 25157, "ms": 18973, "mo": 34319, "mt": 5319, "ne": 8935, "nv": 14682, "nh": 7046, "nj": 55887, "nm": 10282, "ny": 66126, "nc": 42875, "nd": 3780 , "oh": 65811, "ok": 20335, "or" : 19284, "pa" :75308 , "ri": 5900, "sc": 29412, "sd": 4293, "tn": 41191, "tx": 117602, "ut": 10735, "vt": 3201 , "va": 39602, "wa": 31261, "wv": 9353, "wi": 29580, "wy": 2499} #Total Number Of Deaths For Each State
 
    df = pd.read_csv(csv_url)
 
    df = df.apply(pd.to_numeric,errors='coerce') # Making sure all NaN values are set to 0
    df = df.replace(np.nan,0)
 
    rawx = df.get("date")
    resX = rawx[::-1] 
    XX = np.array(resX)
    x = XX.reshape(-1,1)
 
    rawy = df.get("death")
    Y = rawy[::-1]
    y = np.array(Y)
 
    date_pred = int(b)
 
    clf = LinearRegression()
    clf.fit(x,y)
 
    val1 = clf.predict([[date_pred]])
    a = (totaldeaths.get(state))
    final_location = val1/a*100
    print("\nLocation percentage is " + str(final_location) + "%")
 
    return(final_location)

month = input("Enter the month in the format: 08\n")
date = input("Enter the day of the month:\n")
year = input("Enter the year: \n")
 
strval = year+month+date
location_data(strval)
