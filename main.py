from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
brands = []
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
# opening up connection, grabbing the page
uClient = uReq(my_url)
# saving page information to variable
page_html = uClient.read()
# closing up connection
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

for container in containers:
    divWithInfo = container.find("div","item-info")
    brand = divWithInfo.a.img["title"]
    brands.append(brand)

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text.strip()

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping_price = shipping_container[0].text.strip()
    print(brand)
    print(title_container)
    print(shipping_price)