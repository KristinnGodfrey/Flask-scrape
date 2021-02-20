from flask import Flask
from flask import jsonify
from flask import render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

class Prod(object):
    def __init__(self, name, vendor, price):  
        self.name = name  
        self.vendor = vendor
        self.price = price

@app.route('/')
def index():
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
            productItem = productItem.get_text(strip=True, separator='\n')
            # print(productItem)

            productVendor = productContainer.find("div", {"class": "price__vendor price__vendor--listing"})
            productVendor = productVendor.find("dd")
            productVendor = productVendor.get_text(strip=True, separator='\n')
            # print(productVendor)
            
            productPrice = productContainer.find("span", {"class": "price-item price-item--regular"})
            productPrice = productPrice.get_text(strip=True, separator='\n')
            # print(productPrice)

            # print("\n")
            zeList = Prod(productItem,productVendor,productPrice)
            myList.append(zeList)
        
        for obj in myList:
            print(f"{obj.vendor}: {obj.name}\n{obj.price}")
            print()

        
        
        # print(productItem)

    # for obj in myList:
    #     print(obj.name) 
    

    return render_template('hello.html', myList=myList)

if __name__ == '__main__':
    app.run()

