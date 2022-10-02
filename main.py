import wx

# WX Visuals #
class WindowGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(854,480))
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
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

        col1A.Add(wx.Button(pnl, 1, 'Selected Dates'), 1) #Main selection buttons
        col1A.Add(wx.Button(pnl, 1, 'Alcohol Impacts'), 1)

        col2A.Add(wx.StaticText(pnl, 1, label="Victoria State Accident Dataset Analysis"), 1) #Title


        #Selected dates box and controls
        filtery = 110
        filterx = 55
        wx.StaticBox(pnl, -1, 'Select Dates:', (25,40), size=(280,160))

        startDate = wx.TextCtrl(pnl, pos=(60, 70), size=(70, 20))  # Keyword Search
        startDate.SetHint('xx/xx/xxxx') #Set this to min date
        endDate = wx.TextCtrl(pnl, pos=(200, 70), size=(70, 20))  # Keyword Search
        endDate.SetHint('xx/xx/xxxx') #Set this to max date
        wx.StaticText(pnl, 1, label="--->", pos=(150,72))

        wx.RadioButton(pnl, 1, 'All', (filterx,filtery)) #Filter Checkboxes
        wx.RadioButton(pnl, 1, 'Hourly', (2*filterx - 10, filtery))
        wx.RadioButton(pnl, 1, 'Type', (3*filterx, filtery))
        wx.RadioButton(pnl, 1, 'Other', (4*filterx, filtery))

        keyword = wx.TextCtrl(pnl, pos=(80, 160), size=(160, 20))  # Keyword Search
        keyword.SetHint('Keyword')



        # Alcohol Impacts box and controls
        alcX = 85
        alcY = 260
        wx.StaticBox(pnl, -1, 'Alcohol Impacts:', (25, 220), size=(280, 140))

        wx.RadioButton(pnl, 1, 'Trends', (alcX, alcY))  # Filter Checkboxes
        wx.RadioButton(pnl, 1, 'Types', (alcX + 100, alcY))
        wx.RadioButton(pnl, 1, 'Other1', (alcX, alcY + 50))
        wx.RadioButton(pnl, 1, 'Other2', (alcX + 100, alcY + 50))


        #Search Button
        # col1B.Add(wx.Button(pnl, 1, 'Search', (30,30)), 1)
        wx.Button(pnl, 1, 'Search', (125,380))

        pnl.SetSizerAndFit(splitCol)
        self.Show(True)

app = wx.App()
frame = WindowGUI(None, "Accident Data Analysis")
app.MainLoop()