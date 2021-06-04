from PIL import Image, ImageDraw, ImageFont
import random


class MemeGenerator:
    
    def __init__(self, output_dir):
        """Create a new meme"""
        self.output_dir = output_dir
        
    
    def make_meme(self, img_path, text, author, width=1000) -> str:
        
        meme = Image.open(img_path)
        
        if meme.size[0] != width:
            ratio = width/float(meme.size[0])
            height = int(ratio*float(meme.size[1]))
            meme = meme.resize((width, height), Image.NEAREST)
              
        message = '"' + text + '" - ' + author
    
        draw = ImageDraw.Draw(meme)
        font = ImageFont.truetype('./_data/Gidole-Regular.ttf', size=50)
        draw.text((random.randint(0,500), random.randint(0,500)), text=message,
                   font=font, fill=random.choice(['white', 'black']))
        
        if img_path.endswith('jpg'):
            path = self.output_dir + f'/meme{random.randint(0,1000)}.jpg'
        elif img_path.endswith('png'):
            path = self.output_dir + f'/meme{random.randint(0,1000)}.png'
            
        meme.save(path)
        
        return path
        