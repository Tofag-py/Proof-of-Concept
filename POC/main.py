import requests
from pprint import pprint

endpoint = "https://informed-data-challenge.netlify.app/api/breweries"


def base_url(endpoint, x):
    per_page = requests.get(endpoint + f'?per_page={x}')
    return per_page.json()


data = base_url(endpoint, 20)

pprint(data)
