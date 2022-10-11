import pandas as pd
import re
import matplotlib.pyplot as plt
import datetime
import grid
import wx
import jupyter

#1
def infoByTime(sDate, eDate):
    startDate = datetime.datetime.strptime(sDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(eDate, '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    if len(stats.iloc[n]) == 0:
        wx.MessageBox("No Data Found","Error")
    else:
        grid.main(stats.iloc[n])



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
    plt.rcParams.update({'font.size': 22})
    plt.xlabel("Hour (24hr time)")
    plt.ylabel("Number of accidents")

    plt.show()

    return plt.plot()

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
    if len(stats.iloc[a]) == 0:
        wx.MessageBox("No Data Found","Error")
    else:
        grid.main(stats.iloc[a])

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
        if stats.iloc[n[y], 6] in dict1:
            dict1[stats.iloc[n[y], 6]] += 1
        elif stats.iloc[n[y], 6] == "Other accident":
            pass
        else:
            dict1.update({stats.iloc[n[y], 6]: 1})

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]: sort[i][1]})
    plt.rcParams['font.size'] = '5'
    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.title("Number of Alcohol Related incidents by Type")
    plt.xlabel("Type of Accident")
    plt.ylabel("Number of Accidents")

    plt.show()


#5
def alcoholWeekday():
    dict1 = {}
    dict2 = {}

    n = []
    for x in range(len(stats)):
        if str(stats.iloc[x,5]) == 'Yes':
            n.append(x)

    for y in range(len(n)):
        print(y)
        if stats.iloc[n[y], 7] in dict1:
            dict1[stats.iloc[n[y], 7]] += 1
        else:
            dict1.update({stats.iloc[n[y], 7]: 1})

    sort = sorted(dict1.items())
    for i in range(len(dict1)):
        dict2.update({sort[i][0]:sort[i][1]})


    plt.xticks(range(len(dict2)), list(dict2.keys()))
    plt.xlabel("Weekday")
    plt.ylabel("Number of accidents")
    plt.title("Number of Alcohol Related incidents by weekday")
    plt.bar(range(len(dict2)), list(dict2.values()), align='center')
    plt.show()


#6
def alcoholYearly():
    date = stats[stats["ALCOHOLTIME"]=="Yes"]["ACCIDENT_DATE"]

    index = 0
    a = []
    dict1 = {'2014': 0,'2015': 0,'2016': 0,'2017': 0,'2018': 0}
    for t in date:
        if re.search('2014', t) != None:
            dict1['2014'] +=1
        if re.search('2015', t) != None:
            dict1['2015'] +=1
        if re.search('2016', t) != None:
            dict1['2016'] +=1
        if re.search('2017', t) != None:
            dict1['2017'] +=1
        if re.search('2018', t) != None:
            dict1['2018'] +=1
        index += 1

    plt.bar(range(len(dict1)), list(dict1.values()), align='center')
    plt.xticks(range(len(dict1)), list(dict1.keys()))
    plt.xlabel("Year")
    plt.rcParams['font.size'] = '10'
    plt.ylabel("Number of accidents")
    plt.title("Number of Alcohol Related Accidents by Year")
    plt.show()
#7
def weekdayAnalysis(sDate, eDate):
    startDate = datetime.datetime.strptime(sDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(eDate, '%d/%m/%Y')

    n = []
    for x in range(len(stats)):
        newdata = stats.iloc[x, 3]
        if startDate <= datetime.datetime.strptime(newdata, '%d/%m/%Y') <= endDate:
            n.append(x)

    dict1 = {}
    dict2 = {}

    for x in range(len(stats.iloc[n])):
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
#alcoholType()
#alcoholWeekday()
#alcoholYearly()

