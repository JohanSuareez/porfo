import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/newest')
res2=requests.get('https://news.ycombinator.com/newest?next=37627292&n=31')
soup = BeautifulSoup(res.text, 'html.parser')
soup2=BeautifulSoup(res.text,'html.parser')
links = soup.select('.titleline')+ soup2.select('titleline')
subtext = soup.select('.subtext')+soup2.select('subtext')


def sort_stories(hmlist):
    return sorted(hmlist, key=lambda k: k['votes'], reverse=True)


def create_cus_hn(links, subtext):
    hm = []
    for inx, item in enumerate(links):
        titles = item.getText()
        href = item.get('href', None)
        votes = subtext[inx].select('.score')
        if len(votes):
            points = int((votes[0].getText().replace(' points', '').replace(' point', '')))
            if points > 1:
                hm.append({'title': titles, 'link': href, 'votes': points})
    return sort_stories(hm)


pprint.pprint(create_cus_hn(links, subtext))
