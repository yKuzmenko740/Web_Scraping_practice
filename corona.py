import pandas as pd
import requests
from bs4 import BeautifulSoup
values = []
text = []
page = requests.get("https://covid19.gov.ua")
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find(class_="after-title")
fields = title.find(class_="fields")
boxes = fields.find_all(class_="one-field light-box info-count")
for info in boxes:
    values.append(info.find(class_="field-value").get_text().strip())
    text.append(info.find(class_="field-label").get_text().strip())
information = pd.DataFrame(
    {
        "text": text,
        "num": values,
    })
print(information)