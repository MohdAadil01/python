import os
from dotenv import load_dotenv
import requests

load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"


STOCK_NAME = input("Enter the stock symbol for which you want to subscribed.\n")

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}
response = requests.get(STOCK_URL, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_close = data_list[0]["4. close"]
day_before_yesterday_close = data_list[1]["4. close"]

change_percent = (abs(float(yesterday_close) - float(day_before_yesterday_close)) / float(yesterday_close)) * 100
print(change_percent)

if change_percent > 1:
    news_params = {
        "qInTitle" : STOCK_NAME,
        "apiKey" : NEWS_API_KEY
    }
    news_list = requests.get(NEWS_URL, news_params).json()["articles"][:3]
    news = [f"Headline: {news['title']}. \nBrief: {news['description']}" for news in news_list]
    print(news)

