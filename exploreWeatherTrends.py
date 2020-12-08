# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:16:50 2020

@author: alism
"""

import pandas as pd
import matplotlib.pyplot as plt

cityData = pd.read_csv("cityLevelData.csv")
globalData = pd.read_csv("globalData.csv")

#To Explore Data 
print( cityData.head() )
print( globalData.head() )

cTempMAVG = cityData["avg_temp"].rolling(5).mean()
gTempMAVG = globalData["avg_temp"].rolling(5).mean()

plt.plot(cityData["year"],cTempMAVG,c="r",label="Damascus Temp.")
plt.plot(cityData["year"],gTempMAVG,c="b",label="Global Temp.")
plt.xlabel("Year")
plt.ylabel("Temperature (℃)")
plt.legend()
plt.show()



