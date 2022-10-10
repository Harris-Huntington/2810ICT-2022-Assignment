import wx
import wx.grid as grid

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (600,500))


        mygrid = grid.Grid(self)
        mygrid.CreateGrid(26, 9)

    def getData(self):



class myApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Table or Grids")
        self.frame.Show()
        return True

app = myApp()
app.MainLoop()