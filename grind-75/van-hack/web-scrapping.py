from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import math


def parse_html(myurl: 'str') -> 'BeautifulSoup':
    uClient = uReq(myurl)

    # read and close HTML
    page_html = uClient.read()
    uClient.close()

    # call BeautifulSoup for parsing
    page_soup = BeautifulSoup(page_html, "html.parser")
    return page_soup


RESULTS_PER_PAGE = 20


def find_n_pages(topic_page_soup: 'BeautifulSoup'):
    n_results = int(
        topic_page_soup.find(
            'form', {'method': 'get', 'class': 'form-horizontal'}
        ).strong.get_text().strip()
    )

    return math.ceil(n_results / RESULTS_PER_PAGE)


def find_book(topic_url: 'str', title: 'str'):
    topic_page_soup = parse_html(topic_url)

    bookshelf = topic_page_soup.findAll(
        "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for books in bookshelf:
        book_title = books.h3.a["title"].lower()

        if book_title == title.lower():
            return (True, topic_page_soup)

    return (False, topic_page_soup)


def in_stock(title: str, topic: str):
    base_url = 'http://books.toscrape.com'
    myurl = f'{base_url}/index.html'

    page_soup = parse_html(myurl)

    topic_url = None

    for anchor_tag in page_soup.find('div', {"class": 'side_categories'}).ul.li.ul.find_all('a'):
        url = anchor_tag['href']
        topic_found = anchor_tag.get_text().strip().lower()

        if topic_found == topic.lower():
            topic_url = f'{base_url}/{url}'
            break

    if topic_url == None:
        return False

    found, topic_page_soup = find_book(topic_url, title)

    if found:
        return True

    # book has not be found yet
    # determine if we have more pages

    pages = find_n_pages(topic_page_soup)
    if pages <= 1:
        return False

    # we have at least 2 pages
    topic_base_url = '/'.join(topic_url.split('/')[
        :-1])

    for i in range(2, pages + 1):
        topic_page_url = f'{topic_base_url}/page-{i}.html'
        found, _ = find_book(topic_page_url, title)
        if found:
            return True

    return False


print(in_stock("While You Were Mine", "Historical Fiction"))
