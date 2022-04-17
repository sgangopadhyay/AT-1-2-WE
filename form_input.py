from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date

class Suman:
    driver = webdriver.Firefox()
    url = "https://www.google.co.in"
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd4RqX-DSzSNeFQjgTJU3JNHdurirHORE68VK0_0srHGXgLdQ/viewform"

    def form_input(self,input_word):
        self.driver.get(self.url)
        self.driver.maximize_window() # it will maximize your window
        input=self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        input.send_keys(input_word)
        search_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        search_button.click()

    def google_form(self):
        self.driver.get(self.google_form_url)
        time.sleep(2)
        self.driver.maximize_window()
        email_value = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        name_value =self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        comment_value=self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]')
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

        email_value.send_keys("nitin@example.com")
        name_value.send_keys("nitin")
        comment_value.send_keys("Suman loves Pizza")
        time.sleep(3)
        submit_button.click()

s= Suman()

print(s.google_form())
