from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 

#Get all the webpage html code
rental_listings_link = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(rental_listings_link,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15",
    "Accept-Language":"en-US,en;q=0.9"
})
soup = BeautifulSoup(response.text, 'lxml')

#Get all the links for every rental listing
rental_links = soup.find_all(name="a", class_="property-card-link")
links=[]
for rental in rental_links:
    link = rental.get('href')
    links.append(link)

#Get all the prices for every rental listing
rental_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices=[]
for rental in rental_prices:
    price = rental.get_text()
    # Use regular expressions to find all sequences of digits
    digits = re.findall(r'\d+', price)
    # Join the sequences together and convert to an integer
    price = int(''.join(digits))
    prices.append(price)

#Get all the addresses for every rental listing
rental_addresses = soup.find_all(name="address")
addresses=[]
for rental in rental_addresses:
    address = rental.get_text()
    address = address.strip()
    addresses.append(address)

#send to the form with selenium 
    
#Load the webpage    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdu-JZj-o_t1sRVjx---z8pL7EtFAxDbfZbxGVPf5Qwcrar7w/viewform?usp=sf_link")
sleep(5)

#Send the info
for i in range(0,len(addresses)):
    address_field = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(addresses[i])
    sleep(1)
    price_field = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(prices[i])
    sleep(1)
    link_field = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(links[i])
    sleep(1)
    send_button = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send_button.click()
    sleep(1)
    driver.refresh()
    sleep(2)