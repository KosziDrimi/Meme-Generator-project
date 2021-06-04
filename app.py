import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine.Ingestor import Ingestor 
from MemeGenerator import MemeGenerator


app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources"""

    quote_files = ['./_data/SimpleLines/SimpleLines.txt',
                   './_data/SimpleLines/SimpleLines.docx',
                   './_data/SimpleLines/SimpleLines.pdf',
                   './_data/SimpleLines/SimpleLines.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/jerzykowo/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
        
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme"""

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information"""
    
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme"""

    url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    
    r = requests.get(url, allow_redirects=True)
    
    ext = url.split('.')[-1]
    if ext == 'jpg':
        tmp = f'./static/{random.randint(0, 100000)}.jpg'
    elif ext == 'png':
        tmp = f'./static/{random.randint(0, 100000)}.png'
        
    open(tmp, 'wb').write(r.content)
    
    path = meme.make_meme(tmp, body, author)
    
    os.remove(tmp)  

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
