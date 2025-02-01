import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NO = os.getenv("TWILIO_PHONE_NO")
YOUR_PHONE_NO = os.getenv("YOUR_PHONE_NO")

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

STOCK_NAME = input("Enter the stock symbol for which you want to subscribe:\n")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_URL, params=stock_params)
response_data = response.json()

if "Time Series (Daily)" not in response_data:
    print("Error: Unable to retrieve stock data. Check API key or rate limits.")
    exit()

data = response_data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

if len(data_list) < 2:
    print("Error: Not enough stock data available.")
    exit()

yesterday_close = float(data_list[0]["4. close"])
day_before_yesterday_close = float(data_list[1]["4. close"])

change_percent = round(((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100, 2)

if change_percent > 0:
    emoji = "💹"
else:
    emoji = "📉"

print(f"Stock change: {emoji} {abs(change_percent)}%")

if abs(change_percent) > 1:
    news_params = {
        "qInTitle": STOCK_NAME,
        "apikey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_URL, params=news_params).json()

    if "articles" not in news_response:
        print("Error: Unable to retrieve news data.")
        exit()

    news_list = news_response["articles"][:3]
    news_messages = [
        f"{STOCK_NAME}: {emoji} {abs(change_percent)}%\nHeadline: {news['title']}. \nBrief: {news['description']}"
        for news in news_list
    ]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in news_messages:
        message = client.messages.create(
            from_=TWILIO_PHONE_NO,
            body=article,
            to=YOUR_PHONE_NO
        )
        print("Message sent successfully.")
