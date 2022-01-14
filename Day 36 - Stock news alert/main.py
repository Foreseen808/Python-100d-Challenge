import requests
from twilio.rest import Client

STOCK = "MSFT"
COMPANY_NAME = "Microsoft"
ALPHAVANTAGE_API_KEY = ""
NEWS_API_KEY = ""
ACCOUNT_SID = ""
AUTH_TOKEN = ""
SENDER_PHONE = ""
MY_PHONE = ""


alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": ALPHAVANTAGE_API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    # "country": "us",
    # "category": "business",
    "sources": "business-insider",
    "qInTitle": COMPANY_NAME,

}
# Sends an API request to Alphavantage for the previous 2 days stock price at close then compares them
alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
alpha_data = alpha_response.json()
alpha_data_slice = dict(list(alpha_data["Time Series (Daily)"].items())[:2])
data = [value for key, value in alpha_data_slice.items()]
current_day = float(data[0]["1. close"])
previous_day = float(data[1]["1. close"])

percent_change = round(((float(current_day)-previous_day)/previous_day)*100, 1)

stock_went_up = False
if percent_change > 0:
    stock_went_up = True

# Sends an API request to News API for the most recent 3 articles featuring the stock
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()
news_data_slice = news_data["articles"][:3]
print(news_data_slice)

# Sends an SMS to a phone number containing the percentage increase/decrease
# as well as the headlines and briefs for the 3 top articles
if stock_went_up:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for i in range(3):
        message = client.messages \
            .create(
                body=f"{STOCK}:🔺{percent_change}\n"
                     f"Headline: {news_data_slice[i]['title']}\n"
                     f"Brief: {news_data_slice[i]['description']}",
                from_=SENDER_PHONE,
                to=MY_PHONE
                   )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for i in range(3):
        message = client.messages \
            .create(
                body=f"{STOCK}:🔻{percent_change}\n"
                     f"Headline: {news_data_slice[i]['title']}\n"
                     f"Brief: {news_data_slice[i]['description']}",
                from_=SENDER_PHONE,
                to=MY_PHONE
                   )
