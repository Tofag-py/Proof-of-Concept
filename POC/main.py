import requests
#from pprint import pprint


page = 0
all_data_entries = []
per_page = 20

while True:
    print("----------")
    endpoint = f"https://informed-data-challenge.netlify.app/api/breweries?page={page}&per_page={per_page}"
    print("Requesting data..." + endpoint)
    #payload = {'page': page, 'per_page': 20}
    r = requests.get(url=endpoint).json()

    print(r)
    try:
        result = r['data'][0]
    except IndexError:
        # We found an error
        print("Extraction Completed, No more data.....")
        break
    all_data_entries.extend(r['data'])
    page = page + 1
