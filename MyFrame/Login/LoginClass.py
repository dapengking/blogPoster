# -*- coding:utf-8 -*-
import cookielib
import urllib2

def Login_51():
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    
    #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    urllib2.urlopen('http://www.51.com/')
    
    h = urllib2.urlopen('http://passport.51.com/login.5p?callback=jsonp1346394532801&_=1346394563592&passport_51_jsonp=true&passport_51_user=31321313@qq.com&passport_51_password=aassaass&from=www_index_v_b&passport_auto_login=1&version=2')
    content = h.read()
#    print content
#    print content[content.find('errno')+7]
    if content[content.find('errno')+7] == '0':
        #成功
        return 1
    else:
        return 0

#测试登陆功能
#Login_51()