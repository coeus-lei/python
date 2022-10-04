#get site status
from xml import dom
import requests,json
from config import api_id, api_key, account_id, get_site_status

api_id = '52742'
api_key = '31bcccbf-85d4-49d8-bfe2-66baaa658b87'
account_id = '1966488'
site_ip = '35.229.209.207'
get_site_list = 'https://my.imperva.com/api/prov/v1/sites/list'
data_site = {
        'api_id': api_id,
        'api_key': api_key,
        'account_id': account_id
}
#get all domain and record infomations
def get_site_cname ():
    response = requests.post(get_site_list, data=data_site)
    str = response.json()
    domain_dns_cname = {}
    domain_dns_a = {}
    for items in str["sites"]:
        for items in items["dns"]:
            dns_record_name = items["dns_record_name"]
            dns_type = items["set_type_to"]
            dns_data = items["set_data_to"]
            if dns_type == "CNAME":
                domain_dns_cname[dns_record_name] = dns_data
            else:
                domain_dns_a[dns_record_name] = dns_data
    return domain_dns_cname,domain_dns_a

def pretty(params):
    return json.dumps(params, indent=4, ensure_ascii=False)
print(pretty(get_site_cname()))