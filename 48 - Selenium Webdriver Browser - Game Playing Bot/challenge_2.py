from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
articles_number.click()

# Find element by Link Text
articles_number = driver.find_element(By.LINK_TEXT, value='Pages')
articles_number.click()

# Sending keyboard input to Selenium
search_bar = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
#search_bar.send_keys("Red Dead Redemption")
search_bar.send_keys("Red Dead Redemption", Keys.ENTER)

