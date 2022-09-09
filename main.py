
from fake_useragent import UserAgent
import requests
import bs4
from pprint import pprint



KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {'UserAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text



soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')


for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
    hubs = [hub.text.strip() for hub in hubs]
    print(hubs)



