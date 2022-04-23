from bs4 import BeautifulSoup
import requests
import csv


class Suman:
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')

    def Flipkart(self):
        print(self.soup.prettify())

    def Name_Flipkart(self):
        name = self.soup.find('div', class_='_4rR01T')
        return name.text

    def Price_Flipkart(self):
        price = self.soup.find('div', class_='_30jeq3 _1_WHN1')
        return price.text 
    
    def all_data(self):
        products = []
        prices = [] 

        for data in self.soup.findAll('div', class_='_3pLy-c row'):
            names = data.find('div', class_='_4rR01T')
            price = data.find('div', class_='_30jeq3 _1_WHN1')
            products.append(names.text)
            prices.append(price.text)
        
        print(products)
        print("########################################################")
        print(prices)


s = Suman()


s.all_data()
