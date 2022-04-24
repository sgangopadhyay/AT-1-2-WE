from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Suman:
    url = "http://127.0.0.1:5500/suman.html"
    driver = webdriver.Firefox()

    def simple_alert(self):
        self.driver.get(self.url)
        time.sleep(3)
        btn1 = self.driver.find_element(by=By.ID, value='btn1')
        btn1.click()
        # switch to the alert control box
        alert_box =  self.driver.switch_to.alert
        time.sleep(2)
        alert_box.accept()




s = Suman()

s.simple_alert()

