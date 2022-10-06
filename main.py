import wx
import wx.grid as gridlib

# WX Visuals #
import data


class WindowGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(854,480))
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
        rows = wx.BoxSizer(wx.VERTICAL)
        splitCol = wx.BoxSizer(wx.HORIZONTAL) #Splitting the page

        col1 = wx.BoxSizer(wx.VERTICAL) #Left hand col - Selection
        col2 = wx.BoxSizer(wx.VERTICAL) #Right hand col - Title/Data

        splitCol.Add(col1, 3, wx.ALIGN_TOP) #Adding main cols
        splitCol.Add(col2, 5, wx.ALIGN_TOP)

        #First row within each col. Rows follow ABC... formating, Cols 123... etc
        col1A = wx.BoxSizer(wx.HORIZONTAL)
        col1B = wx.BoxSizer(wx.HORIZONTAL)
        col2A = wx.BoxSizer(wx.HORIZONTAL)


        col1.Add(col1A, 1, wx.ALIGN_CENTER, border=30 ) # Adding rows to main cols
        col1.Add(col1B, 1, wx.ALIGN_CENTER, border=400)
        col2.Add(col2A, 1, wx.ALIGN_CENTER)

        col1A.Add(wx.RadioButton(pnl, 1, 'Selected Dates', style=wx.RB_GROUP), 1) #Main selection buttons
        col1A.Add(wx.RadioButton(pnl, 1, 'Alcohol Impacts'), 1)

        col2A.Add(wx.StaticText(pnl, 1, label="Victoria State Accident Dataset Analysis"), 1) #Title
        rows.Add(splitCol, 1, wx.ALIGN_CENTER)

        gridCol = wx.BoxSizer(wx.HORIZONTAL)

        myGrid = gridlib.Grid(pnl)
        myGrid.CreateGrid(12, 8)
        gridCol.Add(myGrid, 1, wx.EXPAND)
        rows.Add(gridCol, 1, wx.ALIGN_LEFT)



        #Selected dates box and controls
        filtery = 110
        filterx = 70
        wx.StaticBox(pnl, -1, 'Select Dates:', (25,40), size=(280,160))


        self.startDate = wx.TextCtrl(pnl, pos=(60, 70), size=(70, 20))  # Keyword Search
        self.startDate.SetHint('xx/xx/xxxx') #Set this to min date
        self.endDate = wx.TextCtrl(pnl, pos=(200, 70), size=(70, 20))  # Keyword Search
        self.endDate.SetHint('xx/xx/xxxx') #Set this to max date

        wx.StaticText(pnl, 1, label="--->", pos=(150,72))

        self.allR = wx.RadioButton(pnl, 1, 'All', (filterx,filtery),style=wx.RB_GROUP) #Filter Checkboxes
        self.hourlyR = wx.RadioButton(pnl, 1, 'Hourly', (2*filterx - 10, filtery))
        self.typeR = wx.RadioButton(pnl, 1, 'Type', (70, 160))
        self.otherR = wx.RadioButton(pnl, 1, 'Other', (3*filterx, filtery))

        self.keyword = wx.TextCtrl(pnl, pos=(120, 160), size=(140, 20))  # Keyword Search
        self.keyword.SetHint('Keyword')





        # Alcohol Impacts box and controls
        alcX = 85
        alcY = 260
        wx.StaticBox(pnl, -1, 'Alcohol Impacts:', (25, 220), size=(280, 140))

        # wx.RadioButton(pnl, 1, 'Trends', (alcX, alcY))  # Filter Checkboxes
        # wx.RadioButton(pnl, 1, 'Types', (alcX + 100, alcY))
        # wx.RadioButton(pnl, 1, 'Other1', (alcX, alcY + 50))
        # wx.RadioButton(pnl, 1, 'Other2', (alcX + 100, alcY + 50))

        wx.RadioButton(pnl, 1, 'Trends', (alcX, alcY), style=wx.RB_GROUP)  # Filter Checkboxes
        wx.RadioButton(pnl, 1, 'Types', (alcX + 100, alcY))
        wx.RadioButton(pnl, 1, 'Other1', (alcX, alcY + 50))
        wx.RadioButton(pnl, 1, 'Other2', (alcX + 100, alcY + 50))




        #Search Button
        searchBtn = wx.Button(pnl, 1, 'Search', (125,380))
        self.Bind(wx.EVT_BUTTON,self.search, searchBtn)


        pnl.SetSizer(rows)
        self.Show(True)
        self.Maximize(True)

    def search(self, event):
        if self.allR.GetValue() == True:
            data.infoByTime(self.startDate.Value, self.endDate.Value)
        elif self.hourlyR.GetValue() == True:
            data.accidentByHour(self.startDate.Value, self.endDate.Value)
        elif self.typeR.GetValue() == True:
            data.keywordByTime(self.startDate.Value, self.endDate.Value, self.keyword.Value)

        print(self.startDate.Value, self.endDate.Value)






app = wx.App()
frame = WindowGUI(None, "Accident Data Analysis")
app.MainLoop()