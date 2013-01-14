# -*- coding:utf-8 -*-
import wx
import cookielib
import urllib2
import urllib
import RegDialog

def Reg_51(parent):
    #注册一个cookie处理对象
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    
    #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    
    useMetal = False
    if 'wxMac' in wx.PlatformInfo:
        useMetal = parent.cb.IsChecked()
    ret = 0
    while ret == 0:
        dlg = RegDialog.RegDialog(parent, -1, "请输入验证码", size=(350, 200),style=wx.DEFAULT_DIALOG_STYLE,useMetal=useMetal)
        dlg.CenterOnScreen()
    
        # this does not return until the dialog is closed.
        val = dlg.ShowModal()
        if val == wx.ID_OK:
            regCode = dlg.getValue()
            retData = urllib2.urlopen("http://passport.51.com/authcode/checkapi?" + regCode[0][regCode[0].find("key"):] + "&code=" + regCode[1]).read()
            if retData[retData.find(':')+1] == '1':
                ret = 1
            dlg.Destroy()
        else:
            dlg.Destroy()
    headers = {
                    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                    'Referer' : 'http://passport.51.com/reg1.5p?from=www_index_v_a'
              }
    postData = {
                    'pp_reg_type' : 'email',
                    'pp_reg_user' : '31321313@qq.com',
                    'pp_reg_pass' : 'aassaass',
                    'pp_reg_repass' : 'aassaass',
                    'pp_reg_sex' : '1',
                    'pp_reg_btype' : '1',
                    'pp_reg_byear' : '1990',
                    'pp_reg_bmonth' : '1',
                    'pp_reg_bleap' : '0',
                    'pp_reg_bday' : '1',
                    'pp_reg_prov' : '北京',
                    'pp_reg_town' : '昌平',
                    'pp_reg_authcode_key' : regCode[0][regCode[0].find("pp_reg"):],
                    'pp_reg_authcode' : regCode[1],
                    'pp_reg_from' : 'www_index_v_a',
                    'pp_reg_url' : 'http://passport.51.com/reg1.5p?from=www_index_v_a',
                    'pp_reg_referer' : '',
                    'pp_reg_redirect' : ''
                }
    postData = urllib.urlencode(postData)
    request = urllib2.Request("http://passport.51.com/reg/ajaxapi?chn=passport", postData, headers)
    response = urllib2.urlopen(request).read()
    if response[response.find('ret')+5] == '1':
        print 'ok'
    else:
        print response