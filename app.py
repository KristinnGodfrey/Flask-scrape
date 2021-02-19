from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

class Prod:
    def __init__(self, name):  
        self.name = name  



@app.route('/')
def hello():
    # Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
    page = requests.get('https://svens.is/collections/frontpage')
    soup = BeautifulSoup(page.content, 'html.parser')

    myList = []
    # products = ""
    productItem = soup.find_all("div", {"class": "product-card"})
    for tag in productItem:
        tdTags = tag.find_all("a", {"class": "grid-view-item__link"})
        for t in tdTags:
            x = t.find_all("span", {"class": "visually-hidden"})
            for s in x:
                myList.append( Prod(s.text))

    for obj in myList:
        print(obj.name) 

    return ""

if __name__ == '__main__':
    app.run()

