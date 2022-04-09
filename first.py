from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class Suman_Python_Automation:
    driver = webdriver.Firefox()

    # fetch the title of the web page
    def get_title(self, url):
        self.driver.get(url)
        return (self.driver.title)

    # fetch the URL of the web page
    def browser_url(self,url):
        self.driver.get(url)
        return (self.driver.current_url)

    # fetch the entire webpage using Selenium Automation
    def get_data(self,url):
        self.driver.get(url)
        return(self.driver.page_source)


s = Suman_Python_Automation()

url = 'https://www.guvi.in'

print(s.get_data(url))
