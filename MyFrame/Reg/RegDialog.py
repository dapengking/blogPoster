# -*- coding:utf-8 -*-
import wx
import urllib2
from bs4 import BeautifulSoup
import cStringIO

class RegDialog(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False,
            ):
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)
        #生成对话框实例
        self.PostCreate(pre)

        # This extra style can be set after the UI object has been created.
        if 'wxMac' in wx.PlatformInfo and useMetal:
            self.SetExtraStyle(wx.DIALOG_EX_METAL)

        # 添加控件
        sizer = wx.BoxSizer(wx.VERTICAL)

        box = wx.BoxSizer(wx.HORIZONTAL)

        hosturl = 'http://passport.51.com/reg1.5p?from=www_index_v_a'
        h = urllib2.urlopen(hosturl)
        content = h.read().decode('gbk')
        
        soup = BeautifulSoup(content)
        cc = soup.find(id="pp_reg_authcode_img")
        self.srcCode = cc.get('src')
        data = urllib2.urlopen("http://passport.51.com" + self.srcCode).read()
        stream = cStringIO.StringIO(data)
        bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
        bmpmap = wx.StaticBitmap(self, -1, bmp, pos = (0, 45),size = (80,30))
        
        box.Add(bmpmap, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "输入:")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.text = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()
        
        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)
        
        btn = wx.Button(self, wx.ID_OK)
        btn.SetHelpText("The OK button completes the dialog")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.SetHelpText("The Cancel button cancels the dialog. (Cool, huh?)")
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

    def getValue(self):
        regReturn = []
        regReturn.append(self.srcCode)
        regReturn.append(self.text.GetValue())
        return regReturn