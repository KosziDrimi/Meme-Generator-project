import os
import random

from QuoteEngine.Ingestor import Ingestor 
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote"""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/jerzykowo/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/SimpleLines/SimpleLines.txt',
                       './_data/SimpleLines/SimpleLines.docx',
                       './_data/SimpleLines/SimpleLines.pdf',
                       './_data/SimpleLines/SimpleLines.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
        
    else:
        if author is None:
            raise Exception('Author required if body is used')
            
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./memes')
    path = meme.make_meme(img, quote.body, quote.author)
    
    return path


if __name__ == "__main__":
    
    import argparse
    
    parser = argparse.ArgumentParser(description="Create a meme")

    parser.add_argument('--path', type=str, help='path to an image file')
    parser.add_argument('--body', type=str, help='quote body to add to the image')
    parser.add_argument('--author', type=str, help='quote author to add to the image')
    
    args = parser.parse_args() 
    print(generate_meme(args.path, args.body, args.author))
    
    
    
  
