import wx

# WX Visuals #
class WindowGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(960,540))
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
        splitCol = wx.BoxSizer(wx.HORIZONTAL) #Splitting the page
        col1 = wx.BoxSizer(wx.VERTICAL) #Left hand col - Selection
        col2 = wx.BoxSizer(wx.VERTICAL) #Right hand col - Title/Data

        splitCol.Add(col1, 1, wx.ALIGN_TOP) #Adding main cols
        splitCol.Add(col2, 1, wx.ALIGN_TOP)


        #First row within each col. Rows follow ABC... formating, Cols 123... etc
        col1A = wx.BoxSizer(wx.HORIZONTAL)
        col2A = wx.BoxSizer(wx.HORIZONTAL)

        col1.Add(col1A, 1, wx.ALIGN_CENTER, border=30 ) # Adding rows to main cols
        col2.Add(col2A, 1, wx.ALIGN_CENTER)

        col1A.Add(wx.Button(pnl, 1, 'Selected Dates'), 1) #Main selection buttons
        col1A.Add(wx.Button(pnl, 1, 'Alcohol Impacts'), 1)

        col2A.Add(wx.StaticText(pnl, 1, label="Victoria State Accident Dataset Analysis"), 1) #Title



        pnl.SetSizerAndFit(splitCol)
        self.Show(True)

app = wx.App()
frame = WindowGUI(None, "Accident Data Analysis")
app.MainLoop()