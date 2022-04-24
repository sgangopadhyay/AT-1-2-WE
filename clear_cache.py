from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Suman:
    chrome_driver = webdriver.Chrome()

    def clear_cache_chrome(self):
        self.chrome_driver.get('chrome://settings/clearBrowserData')
        x_path = 'clearBrowsingDataConfirm'
        path1 = '//*[@id="clearBrowsingDataConfirm"]'
        clear = self.chrome_driver.find_element(by=By.ID, value=x_path)
        clear.click()

s = Suman()

s.clear_cache_chrome()
