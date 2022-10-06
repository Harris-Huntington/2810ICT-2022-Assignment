import matplotlib.pyplot as plt
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import main

import math

#1
def infoByTime():
    #print(len(stats.loc[:, ['ACCIDENT_NO','ACCIDENT_DATE','ACCIDENT_TIME','ALCOHOLTIME']][stats["ACCIDENT_DATE"] == "1/7/2013"]))
    print(stats.loc[:, ['ACCIDENT_NO','ACCIDENT_DATE','ACCIDENT_TIME','ALCOHOLTIME']][stats["ACCIDENT_DATE"] == "1/7/2013"])
#2
def accidentByHour():
    date = "3/7/2013"
    dict1 = {}
    dict2 = {}

    for x in range(len(stats[stats["ACCIDENT_DATE"] == date].iloc[:, 4])):

        if int(str(stats[stats["ACCIDENT_DATE"] == date].iloc[x, 4][0:2])) in dict1:
            dict1[int(str(stats[stats["ACCIDENT_DATE"] == date].iloc[x, 4][0:2]))] += 1
        else:
            dict1.update({int(str(stats[stats["ACCIDENT_DATE"] == date].iloc[x, 4][0:2])): 1})


    xpoints = np.array([min(dict1, key=dict1.get),max(dict1, key=dict1.get)])
    ypoints = np.array([dict1[xpoints[0]], dict1[xpoints[1]]])

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Hour (24hr time)")
    plt.ylabel("Number of accidents")

    plt.show()

#3
def keywordByTime():
    date = ''
    keyword = 'collision'
    keyword = keyword.capitalize()
    type = stats[stats["ACCIDENT_DATE"] == date]["ACCIDENT_TYPE"]

    index = 0
    a = []
    for t in type:
        print(re.search(keyword, t))
        if re.search(keyword, t) != None:
            a.append(index)
        index += 1
    print(stats[stats["ACCIDENT_DATE"] == date].iloc[a,[0,3,4,6]])

#4
def alcoholAnalysis():
    date = "3/7/2013"

#5
def weekdayAnalysis():
    date = "3/7/2013"
    dict1 = {}
    dict2 = {}

    for x in range(len(stats[stats["ACCIDENT_DATE"] == date].iloc[:, 7])):

        if str(stats[stats["ACCIDENT_DATE"] == date].iloc[x, 7][0:2]) in dict1:
            dict1[str(stats[stats["ACCIDENT_DATE"] == date].iloc[x, 4])] += 1
        else:
            dict1.update({str(stats[stats["ACCIDENT_DATE"] == date].iloc[x, 4]): 1})


    xpoints = np.array([min(dict1, key=dict1.get),max(dict1, key=dict1.get)])
    ypoints = np.array([dict1[xpoints[0]], dict1[xpoints[1]]])

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Weekday")
    plt.ylabel("Number of accidents")

    plt.show()


stats = pd.read_csv('../data/Crash Statistics Victoria.csv', index_col=0)




weekdayAnalysis()



#Keyword by timeframe


#[stats[["ACCIDENT_DATE"] == "1/7/2013"]