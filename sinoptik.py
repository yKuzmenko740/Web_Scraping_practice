import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://ua.sinoptik.ua")
soup = BeautifulSoup(page.content, "html.parser")
tabs = soup.find("div", class_="tabs")
items = tabs.find_all("div", class_="main")
for item in items:
    title = item.find(class_="weatherIco")
    print(item.find(class_="day-link").get_text(),
          item.find(class_="date").get_text(), item.find(class_="month").get_text(),
          title.get("title"),
          item.find(class_="min").get_text(),
          item.find(class_="max").get_text(),
          end="\n")
    print()
week_day = [item.find(class_="day-link").get_text() for item in items]
date = [item.find(class_="date").get_text() for item in items]
month = [item.find(class_="month").get_text() for item in items]
titles = []
for item in items:
    title = item.find(class_="weatherIco")
    titles.append(title.get("title"))
min = [item.find(class_="min").get_text() for item in items]
max = [item.find(class_="max").get_text() for item in items]

weather2 = pd.DataFrame(
    {
        "День недели:": week_day,
        "Дата:": date,
        "Месяц:": month,
        "Погода:": titles,
        "Мин. температура": min,
        "Макс температура": max,
    })

print(weather2.iloc[0])
# # weather2.to_csv("weather2.csv")
