# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
import time
import poster

def post():
    title = '你好世界'
    textContent = 'dapengking'
    
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    
    #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    urllib2.urlopen('http://www.51.com/')
    
    h = urllib2.urlopen('http://passport.51.com/login.5p?callback=jsonp1346394532801&_=1346394563592&passport_51_jsonp=true&passport_51_user=31321313@qq.com&passport_51_password=aassaass&from=www_index_v_b&passport_auto_login=1&version=2')
    content = h.read()
    
    contents = urllib2.urlopen('http://diary.51.com/diary/diary_add.php?groupid=0').read().decode('gbk')
    soup = BeautifulSoup(contents)
    cc = soup.findAll(attrs={'name':'randVerify'})
    randVerify =cc[0].get('value')
    cc = soup.findAll(attrs={'name':'f_Diary_OldGroup'})
    f_Diary_OldGroup = cc[0].get('value')
    cc = soup.findAll(attrs={'name':'home_hidden'})
    home_hidden = cc[0].get('value')
    content = ""
    f_Diary_Title = title.encode('gbk')
    f_Diary_Group = "145947"
    cc = soup.findAll(attrs={'name':'f_Diary_Order'})
    f_Diary_Order = cc[0].get('value')
    cc = soup.findAll(attrs={'name':'f_Diary_UnixTimestamp'})
    f_Diary_UnixTimestamp = cc[0].get('value')
    cc = soup.findAll(attrs={'name':'f_Diary_IP'})
    f_Diary_IP = cc[0].get('value')
    f_Diary_Heart = "18"
    ltime = time.localtime(float(f_Diary_UnixTimestamp))
    f_Diary_ShowTime = time.strftime("%Y-%m-%d %H:%M",ltime)
    f_Diary_Memo = textContent.encode('gbk')
    f_Diary_WeekDay = '1'
    share_flag = '1'
    send_feed = '0'
    hide_comment = '0'
    cc = soup.findAll(attrs={'name':'old_share_flag'})
    old_share_flag = cc[0].get('value')
    cc = soup.findAll(attrs={'name':'share_users'})
    share_users = cc[0].get('value')
    active = ''
    cc = soup.findAll(attrs={'name':'draft_key'})
    draft_key = cc[0].get('value')
    cc = soup.findAll(attrs={'name':'id'})
    myId = cc[0].get('value')
    cc = soup.findAll(attrs={'name':'status'})
    status = cc[0].get('value')
    
    headers = {
                    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                    'Referer' : 'http://diary.51.com/diary/diary_add.php?groupid=0'
              }
    postData = {
                    'subject' : f_Diary_Title,
                    'content' : f_Diary_Memo
                }
    postData = urllib.urlencode(postData)
    request = urllib2.Request("http://diary.51.com/diary/diary_check_ajax.php", postData, headers)
    response = urllib2.urlopen(request).read()

    params = {
                   'randVerify' : randVerify,
                   'f_Diary_OldGroup' : f_Diary_OldGroup,
                   'home_hidden' : home_hidden,
                   'content' : content,
                   'f_Diary_Title' : f_Diary_Title,
                   'f_Diary_Group' : f_Diary_Group,
                   'f_Diary_Order' : f_Diary_Order,
                   'f_Diary_UnixTimestamp' : f_Diary_UnixTimestamp,
                   'f_Diary_IP' : f_Diary_IP,
                   'f_Diary_Heart' : f_Diary_Heart,
                   'f_Diary_ShowTime' : f_Diary_ShowTime,
                   'f_Diary_Memo' : f_Diary_Memo,
                   'f_Diary_WeekDay' : f_Diary_WeekDay,
                   'share_flag' : share_flag,
                   'send_feed' : send_feed,
                   'hide_comment' : hide_comment,
                   'old_share_flag' : old_share_flag,
                   'share_users' : share_users,
                   'active' : active,
                   'draft_key' : draft_key,
                   'id' : myId,
                   'status' : status
              }

    opener = poster.streaminghttp.register_openers()
    opener.add_handler(cookie_support)

    datagen, headers = poster.encode.multipart_encode(params)
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1'
    headers['Referer'] = 'http://diary.51.com/diary/diary_add.php?groupid=0'
    request = urllib2.Request('http://diary.51.com/diary/diary_add.php?action=add', datagen, headers)
    result = urllib2.urlopen(request).read().decode('gbk')
    print result

post()