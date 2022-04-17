from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date

class Suman:
    driver = webdriver.Firefox()
    url = "https://www.google.co.in"

    def form_input(self,input_word):
        self.driver.get(self.url)
        input=self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        input.send_keys(input_word)
        search_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        search_button.click()

s= Suman()

print(s.form_input("guvi"))
