import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Suman(unittest.TestCase):
    '''This is a docstring for Python Selenium and Unittest'''

    # initialize your web driver
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_guvi(self):
        driver = self.driver
        driver.get('https://www.guvi.in')
        print(driver.current_url)
        self.assertEqual(driver.current_url, 'https://www.guvi.in/')

    # close the test
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
