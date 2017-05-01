#coding=utf-8
from bs4 import BeautifulSoup
from time import sleep
from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
from collections import Counter
import requests
import json


#判斷是不是影片
#def is_video(td):
#    pricelabels = td('span', 'pricelabel')
#    return (len(pricelabels) == 1 and
#             pricelabels[0].text.strip().startswith("Video"))


#判斷抓取數值
def shop_info(td):
 title = td.find("span","item-name-text").text
 sales_shop = td.find('td','vtop','a').text
 sales_shop_detail = [x.strip() for x in re.sub("\n                              ","",sales_shop).split(",")]
 price2 =td.find("strong","rt-text-price").text
 price2_detail = [x.strip() for x in re.sub(",", "", price2).split(".")]
 price = td.find("td","item-content-direct-price","span").text
 price_detail = [x.strip() for x in re.sub("\n                                ","",price).split(".")]
 sales_quantity = "已銷售數量："+str(td.find("td","item-content-bid-total text-center").a.text)
#格式
 return {
 "title": title,
 "sales_shop": sales_shop_detail,
 "price": price_detail,
 "sales":sales_quantity,
 "price2":price2,
 "price2_detail":price2_detail,
 }

#網站名稱
#base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
 #"data.do?sortby=publicationDate&page="

base_url2 = "http://class.ruten.com.tw/category/sub00.php?c=000500040032&p="
time=0
shops = []
shops_trn = []
NUM_PAGES = 50 # at the time of writing, probably more by now
for page_num in range(1, NUM_PAGES + 1):
 print "souping page", page_num, ",", len(shops), " found so far"
 url = base_url2 + str(page_num)
 soup = BeautifulSoup(requests.get(url).text, 'html5lib')
 for td in soup('div', 'media-body'):
     time = len(shops)
     shops.append(shop_info(td))
 sleep(1)

#原來的資料
print (shops)
#轉換編碼 unicode 轉 utf-8
print str(shops).decode('string_escape')
#shops_trn = shops.decode('big5')
#print shops_trn

#print (shops.decode("unicode-escape").encode("utf-8"))
#shops_trn = json.dumps(shops, encoding="UTF-8", ensure_ascii=False)
#print type(shops)
#print time
i = 0
a=[]
b=0
c=[]
while i <= time:
 #print shops[i]["price2_detail"]
 #a = shops[i]["price2_detail"]
 a = str(shops[i]["price2_detail"]).replace("[u'","")
 a = str(a).replace("']","")
 b = int(a)
 if (b < 2000):
  c.append(b)
 i+=1

#
#print sorted(c)

#def get_year(book):
  #return c[book]

counts = Counter(c)
prices = sorted(counts)
price_counts = [counts[price] for price in prices]

plt.plot(prices,price_counts)
plt.ylabel("Price Cumulative number of times")
plt.xlabel("Price Distributed")
plt.title("The Shop goods price distributed map --1500 piece of data--price under 2000")
plt.show()


