import urllib.parse, urllib.request, urllib.error, json
from flask import Flask, render_template, request, logging
import random
import pip
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


def safe_get(url):
    try:
        return urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request." )
        print("Error code: ", e.code)
    except urllib.error.URLError as e:
        print("We failed to reach a server")
        print("Reason: ", e.reason)
    return None


snowstr = ['Expeditions-Disasters-and-Adventures', 'Religion-Spirituality-and-Faith', 'Childrens-Middle-Grade']
rainstr = ['Paperback-Graphic-Books', 'Science', 'Animals']
sunstr = ['Family', 'Travel', 'Young-Adult']
cloudstr = ['Espionage', 'Health', 'Picture-Books']


class book():
    def __init__(self, booksdata):
        self.title = booksdata['title']
        self.author = booksdata['author']
        self.image = booksdata['book_image']
        self.description = booksdata['description']

    def __str__(self):
        return str(self.image + '\n' + self.title + '\n' + self.author + '\n' + self.description)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/results")
def results():
    value = request.args.get('weather')
    queries = {
    'snow': 'https://api.nytimes.com/svc/books/v3/lists/current/' + str(random.choice(snowstr)) + '.json?api-key=GUyidHNuX60WGmxjB9I7lSpG7KTdYqtf',
    'rain': 'https://api.nytimes.com/svc/books/v3/lists/current/' + str(random.choice(rainstr)) + '.json?api-key=GUyidHNuX60WGmxjB9I7lSpG7KTdYqtf',
    'sun': 'https://api.nytimes.com/svc/books/v3/lists/current/' + str(random.choice(sunstr)) + '.json?api-key=GUyidHNuX60WGmxjB9I7lSpG7KTdYqtf',
    'clouds': 'https://api.nytimes.com/svc/books/v3/lists/current/' + str(random.choice(cloudstr)) + '.json?api-key=GUyidHNuX60WGmxjB9I7lSpG7KTdYqtf'
    }
    bookrequest = urllib.request.urlopen(queries[value])
    bookdict = json.load(bookrequest)
    bookdictlist = [book(x) for x in bookdict['results']['books']]
    booklist = []
    randomlist = random.sample(range(10), 5)
    for num in randomlist:
        booklist.append(bookdictlist[num])
    return render_template('results.html', value=value, booklist=booklist)


app.run(host='localhost', port=8000, debug=True)

