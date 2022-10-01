import wx


class WindowGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(960,540))
        self.initialise()

    def initialise(self):
        self.Show(True)

app = wx.App()
frame = WindowGUI(None, "Accident Data Analysis")
app.MainLoop()