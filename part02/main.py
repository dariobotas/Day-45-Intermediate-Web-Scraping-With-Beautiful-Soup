from bs4 import BeautifulSoup
#import lxml

def run():
  with open("part02/website.html", "r") as f:
    contents = f.read()
    #print(contents)

  soup = BeautifulSoup(contents, "html.parser")

  #print(soup.title)
  #print(soup.title.string)
  #print(soup)
  #print(soup.prettify())
  print(soup.p)