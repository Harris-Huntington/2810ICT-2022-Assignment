import matplotlib.pyplot as plt
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np


import datetime



import datetime


#import main


import math


#stats = pd.read_csv('C:/Users/ericm/Documents/SoftwareTech/AssignmentPartB/data/Crash Statistics Victoria.csv', index_col=0)

#1
def infoByTime():
    startDate = datetime.datetime.strptime('04/07/2013', '%d/%m/%Y')
    endDate = datetime.datetime.strptime('19/07/2013', '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    #print(len(stats.loc[:, ['ACCIDENT_NO','ACCIDENT_DATE','ACCIDENT_TIME','ALCOHOLTIME']][stats["ACCIDENT_DATE"] == "1/7/2013"]))
    print(stats.iloc[n, [number,date,time,a_type,speed]])
#2

def accidentByHour(sDate, eDate):
    startDate = datetime.datetime.strptime(sDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(eDate, '%d/%m/%Y')

    # startDate = datetime.datetime.strptime('1/7/2013', '%d/%m/%Y')
    # endDate = datetime.datetime.strptime('5/7/2013', '%d/%m/%Y')
    print(startDate)

def accidentByHour():
    startDate = datetime.datetime.strptime('04/07/2013', '%d/%m/%Y')
    endDate = datetime.datetime.strptime('19/07/2013', '%d/%m/%Y')


    dict1 = {}
    dict2 = {}
    n = []
    #stats.query("(ACCIDENT_DATE >= str(startDate) or ACCIDENT_DATE <= str(endDate))")

    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    for y in range(len(stats.iloc[n,:])):
        if stats.iloc[n[y],4][0:2] in dict1:
            dict1[stats.iloc[n[y],4][0:2]] += 1
        else:
            dict1.update({stats.iloc[n[y],4][0:2]: 1})


    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})

    print(dict1)
    print(dict2)

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Hour (24hr time)")
    plt.ylabel("Number of accidents")

    plt.show()

#3
def keywordByTime():
    startDate = datetime.datetime.strptime('04/07/2013', '%d/%m/%Y')
    endDate = datetime.datetime.strptime('19/07/2013', '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    date = ''
    keyword = 'collision'
    keyword = keyword.capitalize()
    type = stats.iloc[n]["ACCIDENT_TYPE"]

    index = 0
    a = []
    for t in type:
        print(re.search(keyword, t))
        if re.search(keyword, t) != None:
            a.append(index)
        index += 1
    print(stats.iloc[a,[3,4,6]])

#4
def alcoholAnalysis():
    date = "3/7/2013"

#5
def weekdayAnalysis():
    date = pd.date_range(start = '1/2/2013', end = '10/2/2013')
    startDate = "3/07/2013"
    endDate = "9/07/2013"
    dateRange = ["1/07/2013","2/07/2013","3/07/2013"]

    if startDate[1] == '/':
        if startDate[2:3] == endDate[2:3]:
            if startDate[0] < endDate[0]:
                for x in range(0,(int(endDate[0])-int(startDate[0])+1)):
                    print('j')
                    dateRange.append(str((x+int(startDate[0])))+"/")

    print(dateRange)

    dict1 = {}
    dict2 = {}

    for x in range(len(stats[stats["ACCIDENT_DATE"] == date[1]].iloc[:, 7])):
        print(str(stats[stats["ACCIDENT_DATE"] == date[1]].iloc[x, 7]))

        if str(stats[stats["ACCIDENT_DATE"] == date[1]].iloc[x, 7]) in dict1:
            dict1[str(stats[stats["ACCIDENT_DATE"] == date[1]].iloc[x, 7])] += 1
        else:
            dict1.update({str(stats[stats["ACCIDENT_DATE"] == date[1]].iloc[x, 4]): 1})

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Weekday")
    plt.ylabel("Number of accidents")

    #plt.show()



stats = pd.read_csv('../data/Crash Statistics Victoria.csv', index_col=0)
number = 0
date = 3
time = 4
a_type = 6
speed = 14


#infoByTime()
#accidentByHour()
keywordByTime()





#weekdayAnalysis()
accidentByHour()


accidentByHour()




#Keyword by timeframe


#[stats[["ACCIDENT_DATE"] == "1/7/2013"]