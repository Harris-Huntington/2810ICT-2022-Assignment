import matplotlib.pyplot as plt
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import datetime


import math

#1
def infoByTime():
    #print(len(stats.loc[:, ['ACCIDENT_NO','ACCIDENT_DATE','ACCIDENT_TIME','ALCOHOLTIME']][stats["ACCIDENT_DATE"] == "1/7/2013"]))
    print(stats.loc[:, ['ACCIDENT_NO','ACCIDENT_DATE','ACCIDENT_TIME','ALCOHOLTIME']][stats["ACCIDENT_DATE"] == "1/7/2013"])
#2
def accidentByHour():
    startDate = datetime.datetime.strptime('1/7/2013', '%d/%m/%Y')
    endDate = datetime.datetime.strptime('5/7/2013', '%d/%m/%Y')
    print(startDate)

    startDate1 = '{0}/{1}/{2}'.format(startDate.month, startDate.day, startDate.year)
    endDate1 = '{0}/{1}/{2}'.format(endDate.month, endDate.day, endDate.year)

    print(startDate1, endDate1)

    date = pd.date_range(start = startDate1, end = endDate1)
    dateRange = date.strftime('%#d/%#m/%Y')

    print(date)
    print(dateRange)
    dict1 = {}
    dict2 = {}

    for x in range(len(stats[(stats["ACCIDENT_DATE"] == "1/7/2013") & (stats["ACCIDENT_DATE"] == "2/7/2013")].iloc[:, 4])):
        print(stats[(stats["ACCIDENT_DATE"] == "1/7/2013") & (stats["ACCIDENT_DATE"] == "2/7/2013")].iloc[:, 4])
        if int(str(stats[(stats["ACCIDENT_DATE"] == "1/7/2013") & (stats["ACCIDENT_DATE"] == "2/7/2013")].iloc[x, 4][0:2])) in dict1:
            dict1[int(str(stats[(stats["ACCIDENT_DATE"] == "1/7/2013") & (stats["ACCIDENT_DATE"] == "2/7/2013")].iloc[x, 4][0:2]))] += 1
        else:
            dict1.update({int(str(stats[(stats["ACCIDENT_DATE"] == "1/7/2013") & (stats["ACCIDENT_DATE"] == "2/7/2013")].iloc[x, 4][0:2])): 1})


    print("1/7/2013" > "1/8/2013")

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


    xpoints = np.array([min(dict1, key=dict1.get),max(dict1, key=dict1.get)])
    ypoints = np.array([dict1[xpoints[0]], dict1[xpoints[1]]])

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})

    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Weekday")
    plt.ylabel("Number of accidents")

    #plt.show()


stats = pd.read_csv('../data/Crash Statistics Victoria.csv', index_col=0)



#weekdayAnalysis()
accidentByHour()

#Keyword by timeframe


#[stats[["ACCIDENT_DATE"] == "1/7/2013"]