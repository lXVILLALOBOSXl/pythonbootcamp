## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client

ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_KEY")
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
TWILIO_KEY = os.environ.get("TWILIO_KEY")

TWILIO_SID = "AC3472ee9a96d72588b2f82772eb5606ca"
STOCK = "AAPL"
COMPANY_NAME = "Apple"

# Info to get specified (SYMBOl) stock data
parameters = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY,
}

# returns news data from the API in JSON
def get_news_data(parameters):
    NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything?"
    reponse = requests.get(NEWSAPI_ENDPOINT, params=parameters)
    reponse.raise_for_status()
    news_data = reponse.json()
    return news_data

# returns stock data from the API in JSON
def get_stock_data(parameters):
    ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
    reponse = requests.get(ALPHAVANTAGE_ENDPOINT, params=parameters)
    reponse.raise_for_status()
    stock_data = reponse.json()
    return stock_data

# Returns the close values in stock data for the specified dates  
def get_close_stock_points(data, *args):
    global points
    points = []
    for date in args:
        points.append(float(data['Time Series (Daily)'][date]['4. close']))
    return points

try:
    
    # Gets all the stock data for the specified symbol
    stock_data = get_stock_data(parameters=parameters)

    # Gets the closes values for yesterday and one day before yesterday
    today = datetime.now()
    yesterday = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    before = (today - timedelta(days=2)).strftime('%Y-%m-%d')

    points = get_close_stock_points(stock_data, yesterday, before) 
except:
    print(f"Error has occured trying get stock data")


# Checks if the close values are too different
difference = abs(points[0] - points[1])
percentaje = (difference / points[1]) * 100
percentaje >= 5
if True:
    #  Bring the first 3 news pieces for the COMPANY_NAME
    parameters = {
        "q": COMPANY_NAME,
        "from": before,
        "to": yesterday,
        "sortBy":'popularity',
        "apiKey": NEWSAPI_KEY,
        "pageSize": 3,
        "language":"en",
    }
    up_down =  '🔺' if difference >= percentaje else '🔻'
    try:
        news_data = get_news_data(parameters=parameters)['articles']
        for new in news_data:
            # Send the 3 news as message
            client = Client(TWILIO_SID, TWILIO_KEY)
            message = client.messages.create(
                from_='+12706068224',
                body=f"\n{STOCK}: {up_down}{difference}%\nHeadline: {new['title']}\nBrief: {new['description']}",
                to=''
            )
    except:
        print(f"Error has occured trying get news for the company")

