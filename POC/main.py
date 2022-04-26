import requests
from pprint import pprint

endpoint = "https://informed-data-challenge.netlify.app/api/breweries"


def base_url(endpoint, x):
    per_page = requests.get(endpoint + f'?per_page={x}')
    return per_page.json()


def get_pages(response):
    return response['pages']


def parse_data(response):
    charlist = []
    for item in response['result']:
        char = {
            'name': item['data'],
            'no_ep': len(item['id']),
        }

        charlist.append(char)
        return charlist


data = base_url(endpoint, 20)
print(data)

get_pages = endpoint + f'?page={y}'
per_page = get_pages(endpoint, 2)
print(parse_data(per_page))
