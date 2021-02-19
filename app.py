from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)




@app.route('/')
def hello():
    # Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
    page = requests.get('https://svens.is/collections/frontpage')
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract title of page
    # all_product_card_tags = []
    # for element in soup.select('product-card'):
    #     print(element)
    #     all_product_card_tags.append(element.text)
    # all_product_card_tags = []
    # for element in soup.select('div'):
    # all_product_card_tags.append(soup.find_all("div", class_=["grid-view-item","product-card","visually-hidden"]))
    # all_product_card_tags.append(soup.select("div.grid-view-item.product-card"))
    all_product_card_tags = soup.find_all("div", {"class": "product-view"})
    print(all_product_card_tags)
    # for e in all_product_card_tags:
    #     eTags = e.find_all("a", {"class": "grid-view-item__link"})
    #     print(eTags.text)
    #     for x in e:
    #         print(x.text)
    # print(all_product_card_tags)
        
    # print the result    
    # print(all_product_card_tags)
    return ""

if __name__ == '__main__':
    app.run()

