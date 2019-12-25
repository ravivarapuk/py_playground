# pulling the required utilities
import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_by_votes(final_list):
    return sorted(final_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hnews(link, text):
    hn = []

    for idx, item in enumerate(link):
        title = link[idx].getText()
        href = link[idx].get('href', None)
        vote = text[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))

            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_by_votes(hn)


pprint.pprint(create_custom_hnews(links, subtext))
