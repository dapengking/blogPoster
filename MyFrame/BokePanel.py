# -*- coding:utf-8 -*-
import wx
import Reg.onReg
import Post.PostClass

class BokePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.listOfWeb = []
        # create some sizers
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        sampleList = ['51游戏社区(www.51.com)', '百度空间(hi.baidu.com)', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen']

        lb = wx.CheckListBox(self, -1, size = wx.DefaultSize, choices = sampleList)
        self.Bind(wx.EVT_CHECKLISTBOX, self.EvtCheckListBox, lb)
        self.lb = lb
        hSizer.Add(self.lb,proportion=1,flag=wx.EXPAND)
        
        #button区域的定义
        vSizer = wx.BoxSizer(wx.VERTICAL)

        self.buttonReg = wx.Button(self,label="注册账号")
        self.buttonLogin = wx.Button(self,label="测试登陆")
        self.buttonPage = wx.Button(self,label="博客首页")
        self.buttonHome = wx.Button(self,label="我的主页")
        self.buttonPost = wx.Button(self,label="群发博客")
        self.buttonFeed = wx.Button(self,label="联系作者")
        
        self.Bind(wx.EVT_BUTTON,self.OnClickReg,self.buttonReg)
        self.Bind(wx.EVT_BUTTON,self.OnClickLogin,self.buttonLogin)
        self.Bind(wx.EVT_BUTTON,self.OnClickPage,self.buttonPage)
        self.Bind(wx.EVT_BUTTON,self.OnClickHome,self.buttonHome)
        self.Bind(wx.EVT_BUTTON,self.OnClickPost,self.buttonPost)
        self.Bind(wx.EVT_BUTTON,self.OnClickFeed,self.buttonFeed)
        
        
        vSizer.Add(self.buttonReg)
        vSizer.Add(self.buttonLogin)
        vSizer.Add(self.buttonPage)
        vSizer.Add(self.buttonHome)
        vSizer.Add(self.buttonPost)
        vSizer.AddStretchSpacer(1)
        vSizer.Add(self.buttonFeed)
        
        hSizer.Add(vSizer,proportion=0,flag=wx.EXPAND)
      
      
        self.SetSizerAndFit(hSizer)
        
#获取博客列表    
    def EvtCheckListBox(self, event):
        index = event.GetSelection()
        if self.lb.IsChecked(index):
            self.listOfWeb.append(index)
        else:
            self.listOfWeb.remove(index)

#注册  
    def OnClickReg(self,event):
        print "reg ok"
        Reg.onReg.onReg(self,self.listOfWeb)

#测试登陆    
    def OnClickLogin(self,event):
        print 'ok'

#博客首页
    def OnClickPage(self,event):
        print 'ok'
        
#我的主页
    def OnClickHome(self,event):
        print 'ok'
        
#群发博客
    def OnClickPost(self,event):
        print 'post ok'
        Post.PostClass.post()

#联系作者
    def OnClickFeed(self,event):
        print 'ok'
