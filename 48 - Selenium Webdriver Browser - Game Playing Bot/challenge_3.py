from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

name = 'Hugey'
last_name = 'joto'
email = 'hugo_gay@mail.com'

name_box = driver.find_element(By.XPATH, '/html/body/form/input[1]')
name_box.send_keys(name)

last_name_box = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name_box.send_keys(last_name)

search_bar = driver.find_element(By.XPATH, '/html/body/form/input[3]')
search_bar.send_keys(email, Keys.ENTER)

