import requests
from datetime import date, timedelta

# stock daily data fetch api

ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "8P2PDX4F27PGNG6J"
param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": API_KEY,
}


def get_previous_business_date(check_date: date):
    if check_date.weekday() == 0:
        return check_date - timedelta(days=3)
    elif check_date.weekday() == 6:
        return check_date - timedelta(days=2)
    else:
        return check_date - timedelta(days=1)


response = requests.get(ENDPOINT, params=param)
response.raise_for_status()
api_data = response.json()["Time Series (Daily)"]

date0 = date.today()
date1 = get_previous_business_date(date0)
date2 = get_previous_business_date(date0 - timedelta(days=1))
while str(date2) in api_data:

    data1 = float(api_data[str(date1)]["4. close"])
    data2 = float(api_data[str(date2)]["4. close"])

    if abs(data1-data2)/data1 > 0.01:
        print(f" {date1} , {data1} , {data2}")

    date1 = date2
    date2 = get_previous_business_date(date1)

# weather_hourly = api_data["hourly"][0:11]
# for _weather in weather_hourly:
#     if int(_weather["weather"][0]["id"]) < 700:
#         print("Not good weather, take an umbrella")
