from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Suman:
    driver = webdriver.Firefox()

    def click_link_by_id(self, link_id,url):
        try:
            self.driver.get(url)
            link_id=self.driver.find_element(by=By.ID, value=link_id)
            if link_id:
                time.sleep(4)
                link_id.click()
        except:
            print('error:ID not found !')

    def click_link_by_class(self,link_class,url):
        try:
            self.driver.get(url)
            link_class=self.driver.find_element(by=By.CLASS_NAME, value=link_class)
            if link_class:
                time.sleep(4)
                link_class.click()
        except:
            print('error:CLASS not found !')

    def click_by_xpath(self,xpath_location, url):
        try:
            self.driver.get(url)
            xpath_location = self.driver.find_element(by=By.XPATH, value=xpath_location)
            if xpath_location:
                time.sleep(5)
                xpath_location.click()
        except:
            print('error: XPATH not found !')
s = Suman()

url = "https://www.w3schools.com/"
id_1 = "w3loginbtn"

class_1 = "w3-hover-text-green"

url_1 = 'https://www.guvi.in'
xpath_loc = '/html/body/header/nav/div/div/div[2]/div[2]/ul/li[1]/a'

s.click_by_xpath(xpath_loc,url_1)
