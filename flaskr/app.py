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
    end_page_num = 3
    myList = []
    for i in  range(1,end_page_num+1):
        page = requests.get('https://svens.is/collections/frontpage?page={}'.format(i))
        soup = BeautifulSoup(page.content, 'html.parser')
        
        for productContainer in soup.find_all("div", {"class": "grid-view-item product-card"}):

            productItem = productContainer.find("div", {"class": "h4 grid-view-item__title product-card__title"})
            productItem = productItem.get_text(strip=True, separator='\n')

            productVendor = productContainer.find("div", {"class": "price__vendor price__vendor--listing"})
            productVendor = productVendor.find("dd")
            productVendor = productVendor.get_text(strip=True, separator='\n')

            productPrice = productContainer.find("span", {"class": "price-item price-item--regular"})
            productPrice = productPrice.get_text(strip=True, separator='\n')

            myList.append(Prod(productItem, productVendor, productPrice))
            
    return render_template('hello.html', svens=myList)


if __name__ == '__main__':
    app.run(debug = True)
