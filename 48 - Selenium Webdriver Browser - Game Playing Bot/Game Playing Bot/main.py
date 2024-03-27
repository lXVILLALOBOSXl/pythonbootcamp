from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def main():

    actual_time = time.time()
    minutes = 2
    seconds = 5
    target_time = actual_time + (minutes * 60)
    check_time = actual_time + seconds
    cookie = driver.find_element(by=By.XPATH,value='//*[@id="cookie"]')


    while actual_time < target_time:
        actual_time = time.time()
        cookie.click()

        if actual_time > check_time:
            money = int(driver.find_element(by=By.XPATH,value='//*[@id="money"]').text.replace(",", ""))
            print(money)
            store = driver.find_element(by=By.XPATH,value='//*[@id="store"]')
            store = store.find_elements(by=By.TAG_NAME, value="div")

            for i in range(0,len(store) - 1):
                try:
                    element = store[i].find_element(by=By.TAG_NAME, value="b")
                    price = int(element.text.split()[-1].replace(",", ""))
                    if price > money:
                        store[i - 1].click()
                        purcharses += 1
                except:
                    pass
            

            check_time = actual_time + seconds

    cookies_p_second = driver.find_element(by=By.XPATH,value='//*[@id="cps"]').text.split()[-1]
    print(f"{minutes} cookies per second")


if __name__ == "__main__":
    main()