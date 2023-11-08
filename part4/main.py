from bs4 import BeautifulSoup
#import lxml
import requests

def run():
  response = requests.get("https://news.ycombinator.com/news")
  #print(response.text)
  soup = BeautifulSoup(response.text, "html.parser")
  #print(soup.prettify())
  #print(soup.title)
  #print(soup.title.name)
  all_anchor_tags = soup.find_all(name="a")
  story_title = soup.select(selector='span.titleline a')#find(name="a", class_="storylink")
  story_title = soup.find_all('a', {'rel': True})
  #for a_tag in story_title:
    #print(f"{a_tag.getText()} - {a_tag['href']}")
  #  print(a_tag.getText()+'\n')
  #for a_tag in all_anchor_tags:
  #  print(a_tag.getText()+'\n')
    #print(a_tag.get("href"))

  #for a in soup.find_all('a', {'rel': True}):
  #  print(a['rel'])
  article_vote = soup.select(selector='span.score')
  #for vote in article_vote:
    #print(vote.getText())
  #print(article_vote)
  #print(article_vote.getText())
  #print(article_vote.getText())
  print()
  article_tag = soup.find('a', {'rel': True})
  article_text = article_tag.getText()
  article_url = article_tag['href']#.get('href')
  article_upvote = soup.find(name="span", class_="score").getText()
  #print(article_text)
  #print(article_url)
  #print(article_upvote)

  articles_tag = soup.find_all('a', {'rel': True})
  article_texts = []
  article_links = []
  for article_tag in articles_tag:
    article_text = article_tag.getText()
    article_link = article_tag.get('href')
    article_texts.append(article_text)
    article_links.append(article_link)
    
  articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
  #print(article_texts)
  #print(article_links)
  #print(articles_upvote)

  largest_number = max(articles_upvote)
  largest_index = articles_upvote.index(largest_number)
  print(article_texts[largest_index])
  print(article_links[largest_index])
