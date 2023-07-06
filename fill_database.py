import json
from models import Authors, Quotes
from db_connection import connect
from mongoengine import NotUniqueError


def read_from_file():
    with open('json/authors.json', 'rb') as au:
        au_json = json.load(au)
    with open('json/quotes.json', 'rb') as qu:
        qu_json = json.load(qu)
    return au_json, qu_json


def fill_data(au_json, qu_json):
    for i in au_json:
        data = Authors(**i)
        data.save()

    for i in qu_json:
        author = Authors.objects(fullname=i['author']).first()
        data = Quotes(tags=i['tags'], author=author, quote=i['quote'])
        data.save()


if __name__ == '__main__':
    au_json, qu_json = read_from_file()
    fill_data(au_json, qu_json)
