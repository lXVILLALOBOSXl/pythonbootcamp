from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.nike.com/mx/launch/t/air-force-1-07-fresh")
price = driver.find_element(By.CSS_SELECTOR, '.headline-5.pb6-sm').text
print(F'Price is {price}')


button = driver.find_element(By.ID, value="size_item_radio10.5")
print(F'Size: {button.text}')

# sku = driver.find_element(By.CSS_SELECTOR, value=".description-text.text-color-grey.mb9-sm.ta-sm-c p")
# print(F'Sku: {sku.text}')


link = driver.find_element(By.XPATH, value='//*[@id="gen-nav-footer"]/div/footer/div/div[1]/div[1]/div/div[1]/div/ul/li[1]/a')
print(F'Buscar tienda: {link.text}')

elements = driver.find_elements(By.CSS_SELECTOR, value=".description-text.text-color-grey.mb9-sm.ta-sm-c p")
print(F'Elements: {elements}')


# driver.close()
driver.quit()