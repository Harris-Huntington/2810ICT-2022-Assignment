import matplotlib.pyplot as plt
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import math

#1
def infoByTime():
    print(stats[stats["ACCIDENT_DATE"] == "1/7/2013"])

#2
def accidentByHour():
    print(stats.loc[:, ['ACCIDENT_TIME']])
    #xpoints = np.array(stats.loc['ACCIDENT_TIME'])
    #ypoints = np.array([0,250])

    #plt.plot(xpoints,ypoints)
    #plt.show()

#3
def keywordByTime():
    index = 0
    a = []
    for t in type:

        if re.search("Pedestrian", t) != None:
            a.append(index)
        index += 1
    print(stats.iloc[a,5:9], sep=',')


stats = pd.read_csv('../data/Crash Statistics Victoria.csv', index_col=0)
code = stats['DCA_CODE'].unique()
date = stats['ACCIDENT_DATE']

type = stats["ACCIDENT_TYPE"]


accidentByHour()



#Keyword by timeframe


#[stats[["ACCIDENT_DATE"] == "1/7/2013"]


