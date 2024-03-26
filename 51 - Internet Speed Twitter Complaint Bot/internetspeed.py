from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        #Load sppedtest webpage
        self.driver.get("https://www.speedtest.net/")
        sleep(5)

        #Go button interactions
        go_button = self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        sleep(60)

        # Get speeds
        down_speed = self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        return float(down_speed), float(up_speed)

    def tweet_at_provider(self,user,password,message):
        #Load twitter webpage
        self.driver.get("https://twitter.com/")
        sleep(5)
        
        #Login interactions
        sign_in_button = self.driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
        sign_in_button.click()
        
        #Username form info
        username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))
        )
        username_field.send_keys(user)
        sleep(3)
        username_field.send_keys(Keys.ENTER)

        input("Press enter key when the authentication is completed: ")

        password_field = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(password)
        sleep(3)
        password_field.send_keys(Keys.ENTER)
        sleep(10)

        #Post a tweet
        tweet_field = self.driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.click()
        tweet_field.send_keys(message)
        sleep(10)
        post_button = self.driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_button.click()