from bs4 import  BeautifulSoup
import  requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

maximum_score_index = -1
maxi = scores[0]
for i in range(0, len(scores)):
    if scores[i] > maxi:
        maxi = scores[i]
        maximum_score_index = i

print(article_texts[maximum_score_index])
print(article_links[maximum_score_index])
print(maxi)