#Caching Mode
from config import api_id, api_key, account_id, site_ip, get_site_status
import requests

url_cache_mode = 'https://my.imperva.com/api/prov/v1/sites/performance/cache-mode'

def modify_cache_mode():
    with open('./domain.txt', 'r', encoding="utf-8") as file:
        domain_site = get_site_status()
        for domain in file:
            domain = domain.strip()
            site_id = domain_site[domain]
            data_site = {
                'api_id': api_id,
                'api_key': api_key,
                'site_id': site_id,
                'cache_mode': 'disable',
                'dynamic_cache_duration': '',
                'aggressive_cache_duration': ''
            }
            response = requests.post(url_cache_mode, data=data_site)
            return response.json()

# modify_cache_mode()