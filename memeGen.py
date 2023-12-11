from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import requests
import random
import time
import datetime
current_time = datetime.datetime.now()
str(current_time)

searchInput = input("🌫️: ")
textInput = input("🔤: ")
randomNum = random.randint(10000,10000000000)

def add_text(img, text):
    Image1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('impact.ttf', 15)

    text_width = Image1.textsize(text.upper(), font=myFont) [0]

    x = (img.width - text_width) / 2


    Image1.text((x,10), text.upper(), font = myFont, stroke_width = 1, fill=(255,255,255), stroke_fill=(0,0,0))
    return img

def retrieve_mem_image(search):
    response = requests.get(f'https://imgflip.com/memesearch?q={search.replace(" ", "+")}').text
    html = BeautifulSoup(response, 'html.parser')
    image_url = 'https:' + html.find('img', class_='shadow')['src']
    return Image.open(requests.get(image_url, stream=True).raw)

img = retrieve_mem_image(searchInput)
add_text(img, textInput)
img.show()
img.save(f'meme{current_time}.jpg')
