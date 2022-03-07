from lxml import html
import requests

url = "https://runsignup.com/Race/CA/Ventura/2022CalTriVentura"
xpath = "//span[@class='event-details']/text()"
always_increment = 8

page = requests.get(url)
tree = html.fromstring(str(page.content))  
# result = tree.xpath(xpath)
result = tree.xpath(xpath)[always_increment].text()

print(result[always_increment])