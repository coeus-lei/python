import requests,json
import random,string

#get site list and obtain domain, site_id
api_id = 'xxxxxx'
api_key = 'xxxxxxx'
account_id = 'xxxxxx'
#original site ip
site_ip = 'xx.xx.xx.xx'
get_site_list = 'https://my.imperva.com/api/prov/v1/sites/list'
data_site = {
        'api_id': api_id,
        'api_key': api_key,
        'account_id': account_id
}

#get all domains in current account and generate a new dict with "domain": "site_id"
def get_site_status ():
    response = requests.post(get_site_list, data=data_site)
    str = response.json()
    # len_str =  len(str["sites"])
    domain_site = {}
    for items in str["sites"]:
        domains = items["domain"]
        site_ids = items["site_id"]
        domain_site[domains] = site_ids
        
    return domain_site

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

#randomly generated ref_id with eight numbers
def ref_id():
    result = ''.join(random.sample(string.digits, 8))
    # print(result)
    return result

def pretty(params):
    return json.dumps(params, indent=4, ensure_ascii=False)
# print(pretty(get_site_cname()))
