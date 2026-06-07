import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_para ={
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT,params= stock_para)
data = response.json()["Time Series (Daily)"]
data_list = [data for (key,data) in data.items()]
yesterdays_data_closing = data_list[0]["4. close"]
#print(yesterdays_data_closing)

day_before_yesterday_data_closing = data_list[1]["4. close"]
#print(day_before_yesterday_data_closing)

difference = abs(float(yesterdays_data_closing) - float(day_before_yesterday_data_closing))
#print(difference)


diff_percent = (difference/float(yesterdays_data_closing)) * 100
#print(diff_percent)

if diff_percent > 5:
    news_para ={
        "apikey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME

    }
    news = requests.get(NEWS_ENDPOINT,params=news_para)
    article = news.json()["articles"]
    #print(article)

    three_article= article[:3]
    #print(three_article)    

    formatted_article_List =[f"Headline : {article['title']}. \n Breif : {article['description']}. " for article in three_article]

    client = Client(TWILIO_SID, TWILIO_API_KEY)
    for articles in formatted_article_List:
        message = client.messages.create(
        body=articles,
        from_="+18125613056",
        to="Your phone number",
    )