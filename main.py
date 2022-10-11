import wx
import wx.grid as gridlib

# WX Visuals #
import data



class WindowGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(854,480))
        self.initialise()

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


         # Adding rows to main cols
        col1.Add(col1B, 1, wx.ALIGN_CENTER, border=400)
        col2.Add(col2A, 1, wx.ALIGN_CENTER)

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

        # wx.RadioButton(pnl, 1, 'Trends', (alcX, alcY))  # Filter Checkboxes
        # wx.RadioButton(pnl, 1, 'Types', (alcX + 100, alcY))
        # wx.RadioButton(pnl, 1, 'Other1', (alcX, alcY + 50))
        # wx.RadioButton(pnl, 1, 'Other2', (alcX + 100, alcY + 50))

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
                data.accidentByHour(self.startDate.Value, self.endDate.Value)

            #Keyword search
            elif self.typeR.GetValue() == True:
                data.keywordByTime(self.startDate.Value, self.endDate.Value, self.keyword.Value)

            elif self.weekR.GetValue() == True:
                data.weekdayAnalysis(self.startDate.Value, self.endDate.Value)

        elif self.alcoholR.GetValue() == True:
            if self.trends.GetValue() == True:
                data.alcoholWeekday()
            elif self.aTypes.GetValue() == True:
                data.alcoholType()
            elif self.aYearly.GetValue() == True:
                data.alcoholYearly()


        print(self.startDate.Value, self.endDate.Value)








app = wx.App()
frame = WindowGUI(None, "Accident Data Analysis")
app.MainLoop()