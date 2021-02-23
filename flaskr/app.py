from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


class Prod(object):
    def __init__(self, name, vendor, price):
        self.name = name
        self.vendor = vendor
        self.price = price

class Officials(object):
    def __init__(self, name, vendor):
        self.name = name
        self.vendor = vendor


@app.route('/')
def index():
    end_page_num = 3
    svens = []
    for i in  range(1,end_page_num+1):
        page = requests.get('https://svens.is/collections/frontpage?page={}'.format(i))
        soup = BeautifulSoup(page.content, 'html.parser')
        
        for productContainer in soup.find_all("div", {"class": "grid-view-item product-card"}):
            productItem = productContainer.find("div", {"class": "h4 grid-view-item__title product-card__title"}).get_text(strip=True, separator='\n')
            productVendor = productContainer.find("div", {"class": "price__vendor price__vendor--listing"}).find("dd").get_text(strip=True, separator='\n')
            productPrice = productContainer.find("span", {"class": "price-item price-item--regular"}).get_text(strip=True, separator='\n')

            svens.append(Prod(productItem, productVendor, productPrice))    
    
    # myList.sort(key=lambda x: x.vendor, reverse=False)

    pages = ['loop', 'lyft', 'paz', 'shiro', 'skruf', 'white-fox']
    snusari = []
    for p in pages:        
        page = requests.get('https://snusari.is/products/{}'.format(p))
        soup = BeautifulSoup(page.content, 'html.parser')

        for productContainer in soup.find_all("span", {"gf_swatch"}):
            productItem = productContainer.find("span").get_text(strip=True, separator='\n')
            productVendor = p
            productPrice = soup.find("span", {"gf_product-price money"}).get_text(strip=True, separator='\n')
            snusari.append(Prod(productItem,productVendor,productPrice))

    page = requests.get('https://loopmania.com/#products')
    soup = BeautifulSoup(page.content, 'html.parser')
    loop = []

    for productContainer in soup.find_all("div", {"product-item-content"}):
        productItem = productContainer.find("h3", {"product-item-title"}).get_text(strip=True, separator='\n')
        productVendor = "Loop"
        loop.append(Officials(productItem, productVendor))

    page = requests.get('https://www.golyft.se/se/en/lyft-products')
    soup = BeautifulSoup(page.content, 'html.parser')
    lyft = []

    for productContainer in soup.find_all("div", {"product details product-item-details"}):
        # print(productContainer)
        productItem = productContainer.find("a", {"product-item-link"}).get_text(strip=True, separator='\n')
        productVendor = "Lyft"
        lyft.append(Officials(productItem, productVendor))

    # page = requests.get('https://www.snussie.com/en/nicotine-pouches/zyn/')
    # soup = BeautifulSoup(page.content, 'html.parser')
    # zyn = []

    # for productContainer in soup.find_all("li", {"product  has-label getted-image filled"}):

    return render_template('hello.html', svens=svens, snusari=snusari, loop=loop, lyft=lyft)




if __name__ == '__main__':
    app.run(debug = True)
