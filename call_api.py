import requests
import time
from pprint import pprint

def call_api(url, params=None, headers=None):
    try:
        response = requests.get(
            url,
            params=params,
            headers=headers or {},
            timeout=10
        )
        time.sleep(10)
        response.raise_for_status()   # raises on 4xx/5xx
        return response.json()

    except requests.Timeout:
        print('Request timed out. Try again.')
    except requests.ConnectionError:
        print('No internet connection.')
    except requests.HTTPError as e:
        print(f'HTTP error {e.response.status_code}: {e}')
    except requests.JSONDecodeError:
        print('Response is not valid JSON')
    return None

pprint(call_api("https://api.github.com/users/torvalds"))