# -*- coding: utf-8 -*-

from internetAccessCode import internetBrwsr, newsHolder, emailer
from datetime import datetime
import html

bro = internetBrwsr()
postman = emailer()

data = bro.chkStocks()
#print(data)


date = datetime.now()
date = f"{date.year}-{date.month}-{date.day}"

dateRecent = data["Meta Data"]["3. Last Refreshed"]
dateLast = dateRecent[:-1] + str(int(dateRecent[-1]) - 1)
dateLast = dateLast.strip()


priceLastDay = float(data["Time Series (Daily)"][dateRecent]["4. close"])
priceDayBeforeLastDay = float(data["Time Series (Daily)"][dateLast]["4. close"])


percentChange = ((priceDayBeforeLastDay - priceLastDay) / priceDayBeforeLastDay) * 100

stockHealth = {"change": percentChange, "checkNews": abs(percentChange) >= 0}
# Check news at 2% Change in stock prices, 0 for testing

def email():
    finalNews = []

    j = 0

    for i in news["articles"]:
        
        
        try:
            temp = newsHolder(i["source"]["name"],
                            i["author"],
                            i["title"],
                            i["description"],
                            i["url"], 
                            i["content"])
            finalNews.append(temp)
            j += 1
            
            del temp
            
            if j == 3:
                break
            
            
        except KeyError:
            raise("KEY ERROR")
        except:
            pass

    msg = []

    for x in finalNews:
        msg.append(x.printer())

    msg = "".join(msg)
    
    msg = msg.encode("utf-8")
    
    postman.sendEmail(msg)
    

if(stockHealth["checkNews"]):
    news = bro.chkNews(0, dateLast, date, 1) # 1[sortByCode] Seems correct for this kind of news cycle
    email()
    
#print(news)