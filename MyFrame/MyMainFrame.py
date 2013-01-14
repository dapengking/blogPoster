# -*- coding:utf-8 -*-
import wx
import BokePanel
class MyMainFrame(wx.Frame):
    def __init__(self,parent,title,size,style):
        wx.Frame.__init__(self,parent,title=title,size=size,style=style)

app = wx.App(False)
frame = wx.Frame(None,title="aa",size=(400,270),style=wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU)
nb = wx.Notebook(frame)
nb.AddPage(BokePanel.BokePanel(nb),"table one")
nb.AddPage(wx.Panel(nb), "table two")

frame.Centre()
frame.Show()
app.MainLoop()
        