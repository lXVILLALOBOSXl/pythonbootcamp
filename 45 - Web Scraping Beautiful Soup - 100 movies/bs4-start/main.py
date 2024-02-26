from bs4 import BeautifulSoup
import requests

# with open("/Users/luisvillalobos/Documents/Programacion/Self Study/Udemy/Python Bootcamp/45 - Web Scraping Beautiful Soup - 100 movies/bs4-start/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup)

# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup.prettify())
# print(soup.p)



# all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)




response = requests.get(url="https://news.ycombinator.com/")
# print(response.text)
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
articles_text = []
articles_links = []

for article in articles:
    article = article.a
    articles_text.append(article.getText())
    articles_links.append(article.get("href"))

articles_upvotes  = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

for article_number in articles_upvotes:
    largest_number = max(articles_upvotes)
    largest_index = articles_upvotes.index(largest_number)
    print(articles_text[largest_index])
    print(articles_links[largest_index])
    print(f"{largest_number}\n")
    articles_upvotes.pop(largest_index)
