from bs4 import BeautifulSoup
from notification_manager import NotificationManager
import requests
import lxml

product_link = "https://www.amazon.com.mx/Akozon-Spoiler-Inferior-Parachoques-2017-2021/dp/B09ZKS5HH4/ref=sr_1_4?__mk_es_MX=ÅMÅŽÕÑ&crid=R9N7DPJY480K&dib=eyJ2IjoiMSJ9.Xw7A3tCFHY5D2BE1--vdonQsIQ5bpmKbRkoGGBscYteZoszPhwgrrd404EQfATn1iGjycAnACKoDhaLoKM3RcuwAmAoKrTCxps13iPn9BMuXAT3ZvYUfg6DSXanSPI-hZ4phfQmhgHIT803BCvsLahB16NY6q-ktzUiKSiJsjLJJonYNtw-OhgHJCMHGdMyDK4cnnkYbZ3qdlFOsJkoQSy_BgrFJfM6LR5MjWhDARNP9wN74kbYtUhnQlN_i8CM_Nv5jMzCY4LRwJs_0shGvFPzqsbJ5yLzEonAo7oQwJ-Y.MwXiO4DqV8PQtrkmeyzDxkEXaGHaxog9GBiejm4wG9U&dib_tag=se&keywords=difusor+ibiza&qid=1709568890&sprefix=difusor+ibiza%2Caps%2C143&sr=8-4&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47#customerReviews"

response = requests.get(product_link,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15",
    "Accept-Language":"en-US,en;q=0.9"
})
soup = BeautifulSoup(response.text, 'lxml')

product_price = soup.find(name="span", class_="a-offscreen").get_text()
product_price = product_price.split("$")[1].replace(",","")
product_price = float(product_price)

product_name = soup.find(name="span", id="productTitle").get_text()

target_price = 3000.0
email_receiver = "adrian.villalobos.0917@gmail.com"

if product_price < target_price:
    nm = NotificationManager()
    nm.send_email(email_receiver,"Amazon Price Alert",f"{product_name} is now ${product_price}\n{product_link}")