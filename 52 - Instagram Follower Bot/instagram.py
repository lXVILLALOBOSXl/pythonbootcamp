from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class InstagramBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def follow(self,user:str,password:str,account:str,follows:int):
        #Load instagram webpage
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        
        #Log in on instagram account
        username_field = self.driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(user)
        sleep(3)

        password_field = self.driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password)
        sleep(3)

        sign_in_button = self.driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button')
        sign_in_button.click()
        sleep(5)

        #Load instagram account 
        self.driver.get(f'{account}followers/')
        sleep(4)

        #Follow followers account
        followers_list = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'))
        )
    
        
        for i in range(0,follows):
            sleep(1)
            if i % 4 == 0 and i != 0:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
                sleep(2)
            follow_button = followers_list.find_element(by=By.CSS_SELECTOR, value="._acan._acap._acas._aj1-._ap30")
            follow_button.click()
            sleep(3)
            

        

