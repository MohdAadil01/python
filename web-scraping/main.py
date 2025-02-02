from bs4 import  BeautifulSoup
import  requests
#
# response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# articles = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []
#
# for article in articles:
#     article_texts.append(article.getText())
#     article_links.append(article.get("href"))
#
# maximum_score_index = -1
# maxi = scores[0]
# for i in range(0, len(scores)):
#     if scores[i] > maxi:
#         maxi = scores[i]
#         maximum_score_index = i
#
# print(article_texts[maximum_score_index])
# print(article_links[maximum_score_index])
# print(maxi)


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies_list = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in movies_list]

# movies.reverse()
# REVERSING USING ALGORITHM
first = 0
last = len(movies) - 1
while first <= last:
    # movies[first], movies[last] = movies[last], movies[first]
    temp = movies[first]
    movies[first] = movies[last]
    movies[last] = temp
    first += 1
    last -= 1
