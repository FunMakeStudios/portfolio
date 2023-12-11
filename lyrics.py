import requests
from bs4 import BeautifulSoup


url = input("🔗") # https://search.azlyrics.com/search.php?q=choppa&x=5c742c5dcd35bf8b9f17a903931608e41d4392910d011d2d82d3fda517301bc9
searchword = input("🤔")

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

lyrics = soup.find("div",{"class": "col-xs-12 col-lg-8 text-center"})

text = lyrics.get_text()
https://www.azlyrics.com/lyrics/maxthademon/demonflow.html
words = text.lower().split()

count_number = words.count(searchword)


print(f"🏆 The word {searchword} appears {count_number} of times in this song")