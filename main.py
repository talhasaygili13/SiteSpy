import requests
from bs4 import BeautifulSoup


print('******************************************...****\n*                  SiteSpy                      *\n*                                               *\n*    Enter target website like example.com      *\n******************************************...****')




target_input = input('Enter target url:\n')
target_url = 'https://' + target_input
foundLinks = []

def make_request(url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        foundLink = link.get('href')
        if foundLink:
            if '#' in foundLink:
                foundLink = foundLink.split('#')[0]
            if target_url in foundLink and foundLink not in foundLinks:
                foundLinks.append(foundLink)
                print(foundLink)
                crawl(foundLink)

try:
    crawl(target_url)
except:
    print('Try again with the correct url')