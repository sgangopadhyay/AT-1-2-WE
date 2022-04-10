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

s = Suman()

url = "https://www.w3schools.com/"
id_1 = "w3loginbtn"

s.click_link_by_id(id_1, url)
