import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(450, 350))
        text1 = open("help.txt", "r")

        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, text1.read(), (45, 25), style=wx.ALIGN_LEFT)
        self.Centre()

app1 = wx.App(False)
frame = MyFrame(None, -1, 'Help')