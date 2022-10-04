#Redirect HTTPS and Full domain
from config import api_id, api_key, account_id, site_ip, get_site_status
import requests
url_redirect = 'https://my.imperva.com/api/prov/v1/sites/performance/advanced'

def redirect_url():
    with open('./domain.txt', 'r', encoding="utf-8") as file:
        domain_site = get_site_status()
        for domain in file:
            domain = domain.strip()
            site_id = domain_site[domain]
            data_http = {
                'api_id': api_id,
                'api_key': api_key,
                'site_id': site_id,
                'param': 'redirect_http_to_https',
                'value': 'true'
            }
            data_domain = {
                'api_id': api_id,
                'api_key': api_key,
                'site_id': site_id,
                'param': 'redirect_naked_domain_to_full',
                'value': 'true'
            }
            print(domain, site_id)
            response_http = requests.post(url_redirect, data=data_http)
            response_domain = requests.post(url_redirect, data=data_domain)
            return response_http.json(),response_domain.json()
            # print(response_http.json())
            # print(response_domain.json())

# redirect_url()