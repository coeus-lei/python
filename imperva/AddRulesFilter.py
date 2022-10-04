#Rules Filter
from config import api_id, api_key, account_id, site_ip, get_site_status
import requests
url_rules_filter = 'https://my.imperva.com/api/prov/v1/sites/incapRules/add'
url_rules_list = 'https://my.imperva.com/api/prov/v1/sites/incapRules/list'

def add_rules_filter():
    with open('./domain.txt', 'r', encoding="utf-8") as file:
        domain_site = get_site_status()
        for domain in file:
            domain = domain.strip()
            site_id = domain_site[domain]
            data_add_rules = {
                'api_id': api_id,
                'api_key': api_key,
                'site_id': site_id,
                'name': 'bot',
                'action': 'RULE_ACTION_CAPTCHA',
                'filter': 'ClientId == 7'
            }
            response = requests.post(url_rules_list, data=data_add_rules)
            if response.json()["incap_rules"] and response.json()["incap_rules"]["All"][0]["action"] == "RULE_ACTION_CAPTCHA":
                print(domain + ":已存在该规则-----不用再添加")
            else:
                response = requests.post(url_rules_filter, data=data_add_rules)
                print(domain + ":规则已经添加")
            # print(domain,response.json())

# add_rules_filter()