# -*- coding: cp1252 -*-

import wx
import Help
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 600))

        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu = wx.Menu()
        viewmenu = wx.Menu()
        helpmenu = wx.Menu()

        # Oll menu item undir File
        filemenu.Append(wx.ID_NEW, "New Game", "Start a new game")
        filemenu.Append(wx.ID_UNDO,"&Undo"," Do you regret the last thing you did? Well you can undo it Faggot!")
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

        # Öll menu item undir View
        item = wx.MenuItem(viewmenu, 0, "Highscore", "View the highscore table")
        img = wx.Image('cup.jpg', wx.BITMAP_TYPE_ANY)
        scaledImg = img.Scale(15, 15, wx.IMAGE_QUALITY_HIGH)
        item.SetBitmap(wx.BitmapFromImage(scaledImg))
        viewmenu.AppendItem(item)   

        # Öll menu item undir Help
        helpmenu.Append(wx.ID_HELP, "Help", "Do you not understand the game? Click here idiot!")
        helpmenu.Append(1, "Licence", "Licence")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(viewmenu,"&View") # Adding the "viewmenu" --------------
        menuBar.Append(helpmenu,"&Help")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        # Virkni á takka
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnNewGame, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnUndo, id=wx.ID_UNDO)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnHelp, id=wx.ID_HELP)
        self.Bind(wx.EVT_MENU, self.OnHighscore, id=0)
        self.Bind(wx.EVT_MENU, self.OnLicence, id=1)

    def OnExit(self, event):
        self.Close()

    def OnNewGame(self, event):
        print "ABC"

    def OnUndo(self, event):
        print "Undo"

    def OnAbout(self, event):
        aboutInfo = wx.AboutDialogInfo()
        aboutInfo.SetName("Gooby&Dolan")
        aboutInfo.SetVersion("0.1")
        aboutInfo.SetDescription(("A BETTER version of the famous Golf Relaxed solitaire"))
        aboutInfo.SetCopyright("(C) 2014 - Infinity")
        aboutInfo.SetWebSite("https://github.com/hjorturlarsen/Kapall")
        aboutInfo.AddDeveloper("Egill Ingólfsson")
        aboutInfo.AddDeveloper("Guðni Þór Björnsson")
        aboutInfo.AddDeveloper("Hjörtur Hjartarson")
        aboutInfo.AddDeveloper("Hjörtur Larsen Þórðarson")
        aboutInfo.AddDeveloper("Hrólfur Hjörleifsson")

        wx.AboutBox(aboutInfo)

    def OnHelp(self, event):
        Help.frame.Show(True)

    def OnHighscore(self, event):
        print "Highscore"

    def OnLicence(self, event):
        print "Licence"

app = wx.App(False)
frame = MainWindow(None, "Gooby&Dolan Golf Relaxed")
app.MainLoop()