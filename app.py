from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

class Prod:
    def __init__(self, name, vendor, price):  
        self.name = name  
        self.vendor = vendor
        self.price = price

@app.route('/')
def hello():
    # Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
    end_page_num = 3
    i = 1
    myList = []
    while i <= end_page_num:
        page = requests.get('https://svens.is/collections/frontpage?page={}'.format(i))
        soup = BeautifulSoup(page.content, 'html.parser')

        
        # products = ""
        # productItem = soup.find_all("div", {"class": "product-card"})
        # for tag in productItem:
        #     tdTags = tag.find_all("a", {"class": "grid-view-item__link"})
        #     for t in tdTags:
        #         x = t.find_all("span", {"class": "visually-hidden"})
        #         for s in x:
        #             myList.append(Prod(s.text))
        i+=1

        for productContainer in soup.find_all("div",{"class": "grid-view-item product-card"}):

            productItem = productContainer.find("div", {"class": "h4 grid-view-item__title product-card__title"})
            print(productItem.get_text(strip=True, separator='\n'))

            productVendor = productContainer.find("div", {"class": "price__vendor price__vendor--listing"})
            print((productVendor.get_text(strip=True, separator='\n')))
            
            productPrice = productContainer.find("span", {"class": "price-item price-item--regular"})
            print(productPrice.get_text(strip=True, separator='\n'))

            print("\n")

        
        
        # print(productItem)

    # for obj in myList:
    #     print(obj.name) 
    

    return ""

if __name__ == '__main__':
    app.run()

