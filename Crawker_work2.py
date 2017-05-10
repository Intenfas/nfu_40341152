# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import urllib,urllib2
import matplotlib

url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
#設定起始名稱 終點名稱
StartPoint=u'雲林站'
ArrivePoint=u'台北站'

#資料的格式 開始-結束-日期-時間-收尋方式
form_data = {
"StartStation":"5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f",
"EndStation":"977abb69-413a-4ccf-a109-0272c24fd490",
"SearchDate":"2017/05/24",
"SearchTime":"06:00",
"SearchWay":"DepartureInMandarin",
"RestTime":"",
"EarlyOrLater":"",
}
#字型設定-不是中文的會無法顯示中文
zhfont=matplotlib.font_manager.FontProperties(fname = 'C:\Windows\Fonts\kaiu.ttf')

form_data = urllib.urlencode(form_data)
response = urllib2.urlopen(request,data=form_data)
html = response.read()
soup = BeautifulSoup(html, 'html5lib')

StartTime=[]
for i in soup("table","touch_table"):
    StartTime.append(i.find("td","column3").text)

print StartTime

ArriveTime=[]
for i in soup("table","touch_table"):
    ArriveTime.append(i.find("td","column4").text)

print ArriveTime


xs = [i for i, _ in enumerate(StartTime)]
ys = [i for i, _ in enumerate(ArriveTime)]
plt.plot(xs, ys, 'bx')
plt.xticks([i  for i, _ in enumerate(StartTime)],StartTime)
plt.yticks([i  for i, _ in enumerate(ArriveTime)],ArriveTime)
plt.title(u"高鐵起終時間圖",fontproperties=zhfont)
plt.xlabel(u"雲林站起站" ,fontproperties=zhfont)
plt.ylabel(u"台北站終站" ,fontproperties=zhfont)
plt.show()
#Thank for FU-YU teach me