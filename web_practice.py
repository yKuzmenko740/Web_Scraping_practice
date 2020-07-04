import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.099695000000054&lon=-118.33539999999999#.XpmUC2JR3tQ")
soup = BeautifulSoup(page.content, "html.parser")
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_="tombstone-container")
# print(items[0])
#
# print(items[0].find(class_="period-name").get_text())
# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

period_names = [item.find(class_="period-name").get_text() for item in items]
short_desc = [item.find(class_="short-desc").get_text() for item in items]
temp = [item.find(class_="temp").get_text() for item in items]

weather = pd.DataFrame(
    {
     "period": period_names,
     "short_descriptions": short_desc,
     "temperatures": temp,
     })
print(weather)
weather.to_csv("weather.csv")

