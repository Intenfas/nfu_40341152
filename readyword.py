# coding=utf-8
from collections import Counter
import csv


#把文字檔內的文字變成小寫，再由@分割
def get_domain(email):
    return email.lower().split("@")[-1]
#讀取檔案內容
with open('email.txt','r')as f:
    #把分割後的文字匯入陣列中
    domain_counts = Counter(get_domain(line.strip())for line in f if "@" in line)
print "第一題"
print domain_counts
print "\n第二題"

def process(date,symbol,price):
    print date,symbol,price

with open('tab_delimited_stock_prices.txt','rb')as f:
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
        date=row[0]
        symbol=row[1]
        closing_price = float(row[2])
        process(date,symbol,closing_price)
print "\n第三題"
with open('colon_delimited_stock_prices.txt','rb')as f:
    reader = csv.DictReader(f,delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date,symbol,closing_price)

today_prices = {'CH1':99.99,'CH2':87.65,'CH3':86.12}

with open('comma_delimited_stock_prices.txt','wb')as f:
    writer = csv.writer(f,de)
