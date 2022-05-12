import requests
from trial import data_model


# import os
# import psycopg2

def get_all_data():
    page = 0
    all_data_entries = []
    per_page = 20

    while True:
        print("----------")
        endpoint = f"https://informed-data-challenge.netlify.app/api/breweries?page={page}&per_page={per_page}"
        print("Requesting data..." + endpoint)
        # payload = {'page': page, 'per_page': 20}
        r = requests.get(url=endpoint).json()

        print(r)
        try:
            result = r['data'][0]
        except IndexError:
            # We found an error
            print("Extraction Completed, No more data.....")
            # break
        all_data_entries.extend(r['data'])
        page = page + 1

    data = all_data_entries
    return data


data_model(get_all_data())
