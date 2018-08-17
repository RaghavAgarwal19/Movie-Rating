import requests
from bs4 import BeautifulSoup

search = input("Enter movie name\n")
params = {"q": search}
response = requests.get('https://www.bing.com/search', params=params)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

imdb_urls = []
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    if "imdb.com" in item_href:
        # print(item_href)
        print(item_href)
        imdb_urls.append(item_href)
print(imdb_urls)
for movie in imdb_urls:
    response = requests.get(movie)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find("div", {"id": "content-2-wide"})
    if results==None:
        print('Ratings -:')
        results = soup.find("div", {"id": "pagecontent"})
        rating = results.find("span", {"class": "inline-block text-left vertically-middle"}).text
        index = rating.find('/')
        print(rating[0:index+3])
    else:
        print('Ratings -:')
        rating = results.find("span", {"itemprop": "ratingValue"}).text
        print(rating+'/10')