import requests
from bs4 import BeautifulSoup

URL = input("Enter the Alibaba product URL you want to scrape: ")

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all(name="div", class_="card-info list-card-layout__info")
names = [item.find(name="h2", class_="search-card-e-title").getText() for item in items]
prices = [item.find(name="div", class_="search-card-e-price-main").getText() for item in items]  
reviews = [item.find(name="span", class_="search-card-e-review").getText() if item.find(name="span", class_="search-card-e-review") else "No reviews" for item in items]
urls = [item.find(name="a", class_="search-card-e-detail-wrapper").get("href") for item in items]

name = soup.find(name="div", class_="seb-refine-result_all").getText()
name = name.split('"')[1]


# Create a csv file with the product name, price, reviews and the product URL
# Save the csv file in the same directory as this script
# Use the following format for the csv file:
# Product Name,Price,Reviews,Product URL
with open(f"alibaba_{name}.csv", mode="w") as file:
    file.write("Product Name,Price,Reviews,Product URL\n")
    for i in range(len(names)):
        file.write(f"{names[i]},{prices[i]},{reviews[i]},{urls[i]}\n")