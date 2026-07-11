#web scrabing 3
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
#***********************************************************
gages=[]
now=datetime.now()
date=now.strftime("%Y-%m-%d")


def main():
    try:
        url='https://market.isagha.com/prices#gold'
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
                  }
        link=requests.get(url,headers=headers ,timeout=15)
    except Exception as error:
          print(f'network error & timeout occured{error}')
    page=link.content
    soup=BeautifulSoup(page,'lxml')
    ga=soup.find_all('div',{'class':'price-card'})
    
    gold_karats={'عيار 24','عيار 22','عيار 21','عيار 18','جنيه ذهب','أوقية الذهب'}

    for n,i in enumerate(ga,1):
        try:
              
            gage=i.find('span',{'style':"font-weight: bold; font-size: 18px; color: #deb059;"}).get_text(strip=True)
            
            if gage not in gold_karats:
                continue
            price=i.find_all('div',{'style':"font-weight: 600; color: #1e293b;"})
            if len(price)>=2:
                            sell=price[0].get_text(strip=True).replace("ج.م",'').replace("$",'')
                            buy=price[1].get_text(strip=True).replace("ج.م",'').replace("$",'')
            else:
                sell='0'
                buy='0'
            changes=i.find_all('div',class_=['change-up','change-down'])
            
            if len(changes)>=2:
                change=changes[0].get_text(strip=True).replace("ج.م",'').replace("$",'')
                rate=changes[1].get_text(strip=True).replace("ج.م",'').replace("$",'')
            else:
                change='0'
                rate="0%"
            
            gages.append({'العيار':gage,'سعر البيع':sell,'سعر الشراء':buy,'مقدار التغير':change,'نسبه التغير':rate,'التاريخ':date})
        except Exception as card:
             print(f"card number {n} due to error{card}")
            
def printing():
    header=gages[0].keys()
    try:
        path=r'C:\Users\yahia\Desktop\WebScrabing\gold_price.csv'
        file_exist=os.path.exists(path)
        with open(path,'w',newline='',encoding='utf-8-sig') as file:
            wr=csv.DictWriter(file,header)
            if not file_exist:
                  wr.writeheader()
            wr.writerows(gages)
            print('file printed successful')
    except PermissionError as er:
         print(f' error please close gold_price.csv in excel  before run code : {er}')
    except Exception as err:
         print(f'fail to save file {err}')
main()
printing()

