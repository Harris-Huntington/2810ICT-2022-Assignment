import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import datetime
import wx
import wx.grid

#1
def infoByTime(sDate, eDate, df):
    startDate = datetime.datetime.strptime(sDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(eDate, '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

        df = stats.iloc[n, [number,date,time,a_type,speed]]



#2

def accidentByHour(sDate, eDate):
    startDate = datetime.datetime.strptime(sDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(eDate, '%d/%m/%Y')

    dict1 = {}
    dict2 = {}
    n = []

    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    for y in range(len(stats.iloc[n, :])):
        if stats.iloc[n[y], 4][0:2] in dict1:
            dict1[stats.iloc[n[y], 4][0:2]] += 1
        else:
            dict1.update({stats.iloc[n[y], 4][0:2]: 1})

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]: sort[i][1]})

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Hour (24hr time)",fontsize=4)
    plt.ylabel("Number of accidents")

    plt.show()


#3
def keywordByTime(sDate, eDate, key):
    startDate = datetime.datetime.strptime(sDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(eDate, '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    keyword = key
    type = stats.iloc[n]["ACCIDENT_TYPE"]

    index = 0
    a = []
    for t in type:
        if re.search(keyword, t, re.IGNORECASE) != None:
            a.append(n[index])
        index += 1
    print(stats.iloc[a,[3,4,6]])

#4
def alcoholType():
    dict1 = {}
    dict2 = {}

    n = []
    for x in range(len(stats)):
        if str(stats.iloc[x,5]) == 'Yes':
            n.append(x)
    print(n[0])

    for y in range(len(n)):
        print(y)
        if stats.iloc[n[y], 6] in dict1:
            dict1[stats.iloc[n[y], 6]] += 1
        else:
            dict1.update({stats.iloc[n[y], 6]: 1})

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]: sort[i][1]})
    plt.rcParams['font.size'] = '5'
    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Type of Accident",)
    plt.ylabel("Number of Accidents")

    plt.show()


#5
def weekdayAnalysis(sDate, eDate):
    startDate = datetime.datetime.strptime('04/07/2013', '%d/%m/%Y')
    endDate = datetime.datetime.strptime('19/07/2013', '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    dict1 = {}
    dict2 = {}

    for x in range(len(stats.iloc[n])):
        print(str(stats.iloc[n[x], 7]))

        if str(stats.iloc[n[x], 7]) in dict1:
            dict1[str(stats.iloc[n[x], 7])] += 1
        else:
            if str(stats.iloc[n[x], 7]) == 'nan':
                ""
            else:
                dict1.update({str(stats.iloc[n[x], 7]): 1})

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Weekday")
    plt.ylabel("Number of accidents")

    plt.show()



stats = pd.read_csv('../data/Crash Statistics Victoria.csv', index_col=0)
number = 0
date = 3
time = 4
a_type = 6
speed = 14


#infoByTime()
#accidentByHour()
#keywordByTime()
#weekdayAnalysis()
alcoholType()

