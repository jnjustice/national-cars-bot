import requests


def get_location(location_name):
    import requests

    headers = {
        'authority': 'prd.location.enterprise.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.nationalcar.com',
        'referer': 'https://www.nationalcar.com/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    params = {
        'includeCarAndDriver': 'true',
        'includeCountries': 'true',
        'cor': 'US',
        'locale': 'en_US',
        'dto': 'true',
    }

    response = requests.get('https://prd.location.enterprise.com/enterprise-sls/search/location/national/web/text/'+location_name,
                            params=params, headers=headers)

    return response.json()