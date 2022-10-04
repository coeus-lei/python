#endregionadd domain
from tracemalloc import DomainFilter
import requests
from config import api_id, api_key, account_id, site_ip, get_site_status, ref_id

ref_id = ref_id()
#check if a domain exists, if not add it
def read_domain_files():
    with open('./domain.txt', 'r', encoding="utf-8") as file:
        for domain in file:
            # print(domain,end="")
            domain = domain.strip()
            domain_site = get_site_status()
            # print(domain_site)
            if domain in domain_site.keys():
                print(domain + ':' + "该域名已经存在")
            else:
                print(domain + ':' + "该域名不存在,正在添加该域名")
                try:
                    add_domain(domain)
                except Exception as e:
                    print('域名: (%s)-%s' %(domain.strip(), e))

#send post request to add site api
def add_domain (domain):
    url_add_site = 'https://my.imperva.com/api/prov/v1/sites/add'
    data_site = {
        'api_id': api_id,
        'api_key': api_key,
        'account_id': account_id,
        'ref_id': ref_id,
        'site_ip': site_ip,
        'domain': domain,
        'send_site_setup_emails': 'true',
        'force_ssl': 'true',
        'naked_domain_san': 'true',
        'wildcard_san': 'true'
    }
    response = requests.post(url_add_site, data=data_site)
    return response.json()
    # print(data_site)
    # return data_site

# read_domain_files()
# read_domain_files()
