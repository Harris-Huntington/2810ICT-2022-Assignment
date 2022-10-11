import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

import data



class WindowGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(854,480))
        self.initialise()
        self.p2 = MatPlotPanel(self)



    def initialise(self):
        self.pnl = wx.Panel(self)
        rows = wx.BoxSizer(wx.VERTICAL)
        splitCol = wx.BoxSizer(wx.HORIZONTAL) #Splitting the page

        col1 = wx.BoxSizer(wx.VERTICAL) #Left hand col - Selection
        col2 = wx.BoxSizer(wx.VERTICAL) #Right hand col - Title/Data

        splitCol.Add(col1, 3, wx.ALIGN_TOP) #Adding main cols
        splitCol.Add(col2, 7, wx.ALIGN_TOP)

        #First row within each col. Rows follow ABC... formating, Cols 123... etc
        col1A = wx.BoxSizer(wx.HORIZONTAL)
        self.datesR = wx.RadioButton(self.pnl, 1, 'Selected Dates', style=wx.RB_GROUP)
        self.alcoholR = wx.RadioButton(self.pnl, 1, 'Alcohol Impacts')
        col1A.Add(self.datesR, 1)  # Main selection buttons
        col1A.Add(self.alcoholR, 1)
        col1.Add(col1A, 1, wx.ALIGN_CENTER, border=30)

        col1B = wx.BoxSizer(wx.HORIZONTAL)
        col2A = wx.BoxSizer(wx.HORIZONTAL)
        col2B = wx.BoxSizer(wx.HORIZONTAL)


         # Adding rows to main cols
        col1.Add(col1B, 1, wx.ALIGN_CENTER, border=400)
        col2.Add(col2A, 1, wx.ALIGN_CENTER)
        col2.Add(col2B, 1, wx.ALIGN_CENTER, border=400)

        col2A.Add(wx.StaticText(self.pnl, 1, label="Victoria State Accident Dataset Analysis"), 1) #Title
        rows.Add(splitCol, 1, wx.ALIGN_CENTER)

        self.infoCol = wx.BoxSizer(wx.HORIZONTAL)
        rows.Add(self.infoCol, 1, wx.ALIGN_LEFT)




        #Selected dates box and controls
        filtery = 110
        filterx = 70
        wx.StaticBox(self.pnl, -1, 'Select Dates:', (25,40), size=(280,160))


        self.startDate = wx.TextCtrl(self.pnl, pos=(60, 70), size=(70, 20))  # Keyword Search
        self.startDate.SetHint('1/07/2013') #Set this to min date
        self.endDate = wx.TextCtrl(self.pnl, pos=(200, 70), size=(70, 20))  # Keyword Search
        self.endDate.SetHint('21/03/2019') #Set this to max date

        wx.StaticText(self.pnl, 1, label="--->", pos=(150,72))

        self.allR = wx.RadioButton(self.pnl, 1, 'All', (filterx,filtery),style=wx.RB_GROUP) #Filter Checkboxes
        self.hourlyR = wx.RadioButton(self.pnl, 1, 'Hourly', (2*filterx - 10, filtery))
        self.typeR = wx.RadioButton(self.pnl, 1, 'Type', (70, 160))
        self.weekR = wx.RadioButton(self.pnl, 1, 'Weekday', (3*filterx, filtery))

        self.keyword = wx.TextCtrl(self.pnl, pos=(120, 160), size=(140, 20))  # Keyword Search
        self.keyword.SetHint('Keyword')

        # Alcohol Impacts box and controls
        alcX = 85
        alcY = 260
        wx.StaticBox(self.pnl, -1, 'Alcohol Impacts:', (25, 220), size=(280, 140))

        self.trends = wx.RadioButton(self.pnl, 1, 'Trends', (alcX, alcY), style=wx.RB_GROUP)  # Filter Checkboxes
        self.aTypes = wx.RadioButton(self.pnl, 1, 'Types', (alcX + 100, alcY))
        self.aYearly = wx.RadioButton(self.pnl, 1, 'Yearly', (alcX + 50, alcY+50))




        #Search Button
        searchBtn = wx.Button(self.pnl, 1, 'Search', (125,380))
        self.Bind(wx.EVT_BUTTON,self.search, searchBtn)


        self.pnl.SetSizer(rows)
        self.Show(True)



    def search(self, event):
        if self.datesR.GetValue() == True:
            #Get info of accidents between 2 dates
            if self.allR.GetValue() == True:
                data.infoByTime(self.startDate.Value, self.endDate.Value)

            #view graph on how many accidents per hour
            elif self.hourlyR.GetValue() == True:
                self.p2.drawHourly(data.accidentByHour(self.startDate.Value, self.endDate.Value))

            #Keyword search
            elif self.typeR.GetValue() == True:
                data.keywordByTime(self.startDate.Value, self.endDate.Value, self.keyword.Value)

            #Weekday analysis
            elif self.weekR.GetValue() == True:
                self.p2.drawWeeklyDate(data.weekdayAnalysis(self.startDate.Value, self.endDate.Value))

        elif self.alcoholR.GetValue() == True:
            #Weekday analysis of alcohol
            if self.trends.GetValue() == True:
                self.p2.drawAlcoholWeekday(data.alcoholWeekday())

            #no of crashes affected by alcohol by type
            elif self.aTypes.GetValue() == True:
                self.p2.drawAlcoholType(data.alcoholType())

            #yearly alcohol analysis
            elif self.aYearly.GetValue() == True:
                self.p2.drawAlcoholYearly(data.alcoholYearly())

        elif self.hourlyR.GetValue() == True:
            data.accidentByHour(self.startDate.Value, self.endDate.Value)

        elif self.typeR.GetValue() == True:
            data.keywordByTime(self.startDate.Value, self.endDate.Value, self.keyword.Value)





class MatPlotPanel(wx.Panel):
        def __init__(self, parent):
             wx.Panel.__init__(self, parent, -1, size=(500,400), pos=(325,25))


        def drawHourly(self, dict2):
            self.figure = Figure(figsize=(5.5,4))
            self.axes = self.figure.add_subplot(111)
            self.axes.bar(range(len(dict2)), list(dict2.values()), align='center')
            self.axes.set_xticks(range(len(dict2)), list(dict2.keys()))
            self.axes.set_xlabel("Hour (24hr time)")
            self.axes.set_ylabel("Number of accidents")
            self.canvas = FigureCanvas(self, -1, self.figure)

        def drawWeeklyDate(self, dict2):
            self.figure = Figure(figsize=(5.5, 4))
            self.axes = self.figure.add_subplot(111)
            self.axes.bar(range(len(dict2)), list(dict2.values()), align='center')
            self.axes.set_xticks(range(len(dict2)), list(dict2.keys()))
            self.axes.set_xlabel("Weekday")
            self.axes.set_ylabel("Number of accidents")
            self.canvas = FigureCanvas(self, -1, self.figure)

        def drawAlcoholWeekday(self, dict2):
            self.figure = Figure(figsize=(5.5, 4))
            self.axes = self.figure.add_subplot(111)
            self.axes.bar(range(len(dict2)), list(dict2.values()), align='center')
            self.axes.set_xticks(range(len(dict2)), list(dict2.keys()))
            self.axes.set_xlabel("Weekday")
            self.axes.set_ylabel("Number of accidents")
            self.axes.title("Number of Alcohol Related incidents by weekday")
            self.canvas = FigureCanvas(self, -1, self.figure)

        def drawAlcoholType(self, dict2):
            self.figure = Figure(figsize=(5.4, 4))
            self.axes = self.figure.add_subplot(111)
            self.axes.bar(range(len(dict2)), list(dict2.values()), align='center')
            self.axes.set_xticks(range(len(dict2)), list(dict2.keys()))
            self.axes.set_title("Number of Alcohol Related incidents by Type")
            self.axes.set_xlabel("Type of Accident")
            self.axes.set_ylabel("Number of Accidents")
            self.canvas = FigureCanvas(self, -1, self.figure)

        def drawAlcoholYearly(self, dict1):
            self.figure = Figure(figsize=(5.2, 4))
            self.axes = self.figure.add_subplot(111)
            self.axes.bar(range(len(dict1)), list(dict1.values()), align='center')
            self.axes.set_xticks(range(len(dict1)), list(dict1.keys()))
            self.axes.set_xlabel("Year")
            self.axes.set_ylabel("Number of accidents")
            self.axes.set_title("Number of Alcohol Related Accidents by Year")
            self.canvas = FigureCanvas(self, -1, self.figure)








app = wx.App()
frame = WindowGUI(None, "Accident Data Analysis")
app.MainLoop()