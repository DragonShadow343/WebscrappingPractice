from bs4 import BeautifulSoup
import requests

b = 0

for i in range(0,200):
    University_site = requests.get(f'https://www.utoronto.ca/news/searchnews?query_news=&field_topic=2812&changed%5Bdate%5D=&changed_1%5Bdate%5D=&page={i-1}').text
    soup = BeautifulSoup(University_site, 'lxml')
    articles = soup.find_all('h4', class_='field-content')
    for a in articles:
        link = a.a['href']
        a = a.text
        date = soup.find('p', class_='field-content').text

        if ('software' in a) or ('engineering' in a) or ('robots' in a) or ('physic' in a) or ('green' in a) or ('AI' in a):

            print(f"Page {i}")
            print(f"Date: {date}")
            b = b + 1
            print(f"{b}. {a}")
            print(f"Link: https://www.utoronto.ca{link}")
            print("\n")
