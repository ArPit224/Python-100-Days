import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import smtplib
import html

load_dotenv()

class internetBrwsr:
    
    def __init__(self):
        
        pass
        
        
    def chkStocks(self):
        
        STOCK_NAME = "MSFT"

        STOCK_ENDPOINT = "https://www.alphavantage.co/query"

        API_STOCKS = os.getenv(key = "API_STOCKS", default = "o")
        
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": STOCK_NAME,
            "apikey": API_STOCKS
        }
        
        with requests.get(url = STOCK_ENDPOINT, params = params) as response:
            
            response.raise_for_status()
            
            return response.json()
            
            #Not a fan of no exceptions
            
    def chkNews(self, queryNum:int, dateFrm:str, dateTo:str, sortByCode:int):
        
        '''
        queryNum for the list Query: ["MSFT AND stocks", "Microsoft AND stocks", "MSFT", "\"Microsoft\""],
        dateFormal: YYYY-MM-DD,
        sortByCode for the list: ["publishedAt", "popularity"]
        '''
        API_NEWS = os.getenv(key = "API_NEWS", default = "1")
        
        NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
        #NEWS_ENDPOINT = "https://newsapi.org/v2/everything?q=MSFT%20AND%20stocks&from=2022-12-11&language=en&sortBy=publishedAt&apiKey=1218aa81c17b4b13ba5fe175514b371e"
        
        
        querys = ["MSFT AND stocks", "Microsoft AND stocks", "MSFT", "\"Microsoft\""]
        
        sortBy = ["publishedAt", "popularity"]
        
        
        paramsN = {
            "q": querys[queryNum],
            "from": dateFrm,
            "to": dateTo,
            "language": "en",
            "sortBy": sortBy[sortByCode],
            "apiKey": API_NEWS
        }
        
        with requests.get(url = NEWS_ENDPOINT, params = paramsN) as response:
            
            return response.json()

class newsHolder:
    
    def __init__(self, name, author, title, description, url, content):
        
        self.name = html.unescape(name)
        self.author = html.unescape(author)
        self.title = html.unescape(title)
        self.description = html.unescape(description)
        self.url = html.unescape(url)
        self.content = html.unescape(content)
    
    def printer(self):
        
        '''
        Prints out neatly formatted news article
        '''
        
        return f"{self.title}\n{self.name}\nby: {self.author}\nDesc: {self.description}\nurl: {self.url}\nContent: {self.content}"


class emailer:
    
    def __init__(self):
        pass
            
    def sendEmail(self, msg:str):
        
        EMAIL = os.getenv(key = "EMAIL", default = "0")
        TO_EMAIL = os.getenv(key = "TO_EMAIL", default = "0")
        PASS = os.getenv(key = "EMAIL_STMP_PASS", default = "0")
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            
            connection.starttls()
            connection.login(user = EMAIL, password = PASS)
            connection.sendmail(from_addr = EMAIL,
                                to_addrs = TO_EMAIL,
                                msg = f"Subject: Stock ALert!!!\n\n{msg}")
 
#bro = internetBrwsr()

#stocks = bro.chkStocks() #BRO check Stocks, Lol

#print(stocks) #Stocks API works

#news = bro.chkNews(1, "2022-12-09", "2022-12-11", 0) #Bro Check News, LOL

#print(news)