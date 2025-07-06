STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
key="SCF5D6Y6DRXF1W7M"
second_key="9d1f5d3ab7904155af6cc13481cfae67"
date="2024-07-04"
import requests
endpoint="https://www.alphavantage.co/query?"
params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":key
    
}
endpoint2="https://newsapi.org/v2/everything?"
params2={
    "q":"tesla",
    "from":date,
    "sortBy":"publishedAt",
    "apiKey":second_key
}

r2=requests.get(endpoint2,params2)
data2=r2.json()["articles"]

r = requests.get(endpoint,params)
data = r.json()

article=data2[0]
auteur=article["author"]
titre=article["title"]
desc=article["description"]
contenue=article["content"]

today="2024-08-02"
yesterday="2024-08-01"
t_stock=data[today]["2. high"]
y_stock=data[yesterday]["2. high"]
pourcentage=0.05*float(y_stock)
if t_stock>y_stock:
    dif=t_stock-y_stock
    if dif > pourcentage:
        print(contenue)
elif t_stock<y_stock:
    dif=y_stock-t_stock
    print(contenue)
    







## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 

