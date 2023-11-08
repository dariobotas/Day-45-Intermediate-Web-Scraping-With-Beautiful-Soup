#import lxml
import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

def run():
  response = requests.get(URL)
  website_html = response.text
  soup = BeautifulSoup(website_html, "html.parser")

  movie_titles = soup.find_all("h3", class_="title")
  print(movie_titles)
  for title in movie_titles:
    print(title.text)
  
  #movie_ratings = soup.find_all("div", class_="ratingValue")
  #for rating in movie_ratings:
  #  print(rating.text)
  
  #movie_years = soup.find_all("span", class_="lister-item-year text-muted unbold