from bs4 import BeautifulSoup
#import lxml

def run():
  with open("part3/website.html", "r") as f:
    contents = f.read()
    #print(contents)

  soup = BeautifulSoup(contents, "html.parser")

  #print(soup.title)
  #print(soup.title.string)
  #print(soup)
  #print(soup.prettify())
  #print(soup.p)
  #print(soup.find_all(name="a"))

  all_anchor_tags = soup.find_all(name="a")
  for a_tag in all_anchor_tags:
    print(a_tag.getText())
    print(a_tag.get("href"))

  heading = soup.find(name="h1", id="name")
  print(heading)
  print(heading.getText())
  
  section_heading = soup.find(name="h3", class_="heading")
  print(section_heading)
  print(section_heading.name)
  print(section_heading.get("class"))

  company_url = soup.select_one(selector="p a")
  print(company_url)

  name = soup.select_one(selector="#name")
  print(name)

  print(soup.select(selector=".heading"))