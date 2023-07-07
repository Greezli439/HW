import requests
from bs4 import BeautifulSoup
import json

author_name, author_url = set(), set()
data_quotes, data_authors = [], []

url_start = 'https://quotes.toscrape.com/'


def pars_for_authors_file(soup):
    quotes_divs = soup.find_all('div', class_='quote')

    for i in quotes_divs:
        author_name.add(i.find('small', class_='author').string)
        author_url.add(i.find('a')['href'])


def add_data_to_quotes_list(quotes, authors, tags):
    for i in range(0, len(quotes)):
        _tags_ = []
        tagsforquote = tags[i].find_all('a', class_='tag')
        for tagforquote in tagsforquote:
            _tags_.append(str(tagforquote.text))
        quote_dict = {
            "tags": _tags_,
            "author": authors[i].text,
            "quote": quotes[i].text
        }
        data_quotes.append(quote_dict)


def pars_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')
    add_data_to_quotes_list(quotes, authors, tags)
    pars_for_authors_file(soup)
    find_next_quotes_page(soup)


def find_next_quotes_page(soup):
    url = soup.find('li', class_='next')
    if url:
        url = url_start + url.a['href']
        main(url)
    else:
        write_to_qoutes_json(data_quotes)
        start_pars_for_authorsjson()


def start_pars_for_authorsjson():
    for url, name in zip(author_url, author_name):
        response = requests.get(url_start + url)
        soup_authors = BeautifulSoup(response.text, 'lxml')
        author_born_date = soup_authors.find('span', class_='author-born-date').string
        author_born_location = soup_authors.find('span', class_='author-born-location').string
        author_description = soup_authors.find('div', class_='author-description').string
        add_data_to_authors_list(author_born_date, author_born_location, author_description, name)
    write_to_authors_json()


def add_data_to_authors_list(author_born_date, author_born_location, author_description, author_name):
    author_dict = {
        'fullname': author_name,
        'born_date': author_born_date,
        'born_location': author_born_location,
        'description': author_description
    }
    data_authors.append(author_dict)


def write_to_qoutes_json(data_quotes):
    with open('qoutes.json', 'w') as qo:
        json.dump(data_quotes, qo)


def write_to_authors_json():
    with open('authors.json', 'w') as qo:
        json.dump(data_authors, qo)


def main(url):
    pars_data(url)


if __name__ == '__main__':
    main(url_start)

