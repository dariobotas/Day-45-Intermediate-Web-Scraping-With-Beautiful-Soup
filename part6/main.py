#import lxml
import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

def run():
  response = requests.get(URL)
  website_html = response.text
  #print(website_html)
  soup = BeautifulSoup(website_html, "html.parser")
  #print(soup.prettify())
  movie_titles = soup.find_all("h3", class_="listicleItem_listicle-item__title__hW_Kn")
  #print(movie_titles)

  #list of all movies
  movie_titles = [title.text for title in movie_titles]
  print(movie_titles)

  #reversed list of all 100 movies
  print(list(reversed(movie_titles)))
  movies = movie_titles[::-1]
  print(movies)
  for n in range(len(movie_titles) -1, -1, -1 ):
    print(movie_titles[n])

  if not os.path.exists('movies.txt'):
    with open("movies.txt", mode="w") as file:
      for movie in movies:
        file.write(f"{movie} \n")