import requests, re
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

titles.reverse()

with open("/Users/luisvillalobos/Documents/Programacion/Self Study/Udemy/Python Bootcamp/45 - Web Scraping Beautiful Soup - 100 movies/Starting Code - 100 movies to watch start/movies.txt", mode="w") as file:
    for title in titles:
        file.write(f"{title}\n")

