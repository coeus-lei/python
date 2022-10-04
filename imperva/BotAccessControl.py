#bot access control
from config import api_id, api_key, account_id, site_ip, get_site_status
import requests
url_bot_control = 'https://my.imperva.com/api/prov/v1/sites/configure/security'

data_bot_control = {
    'api_id': api_id,
    'api_key': api_key,
    'site_id': '',
    'rule_id': 'api.threats.bot_access_control',
    'block_bad_bots': 'true',
    'challenge_suspected_bots': 'true',
}
def security_control ():
    with open('./domain.txt', 'r', encoding="utf-8") as file:
        domain_site = get_site_status()
        for domain in file:
            domain = domain.strip()
            # if domain in domain_site.keys():
            #     print(domain + ':' + "该域名已经存在")
            # else:
            #     print(domain + ':' + "该域名不存在,正在添加该域名")
            try:
                site_id = domain_site[domain]
                data_bot_control = {
                    'api_id': api_id,
                    'api_key': api_key,
                    'site_id': site_id,
                    'rule_id': 'api.threats.bot_access_control',
                    'block_bad_bots': 'false',
                    'challenge_suspected_bots': 'false',
                }
                data_waf_control = {
                    'api_id': api_id,
                    'api_key': api_key,
                    'site_id': site_id,
                    'rule_id': 'api.threats.backdoor',
                    'security_rule_action': 'api.threats.action.quarantine_url'
                }
                data_ddos_control = {
                    'api_id': api_id,
                    'api_key': api_key,
                    'site_id': site_id,
                    'rule_id': 'api.threats.ddos',
                    'activation_mode': 'api.threats.ddos.activation_mode.on',
                    'ddos_traffic_threshold': '1000'
                }
                # response_bot_control = requests.post(url_bot_control, data=data_bot_control)
                response_waf_control = requests.post(url_bot_control, data=data_waf_control)
                response_ddos_control = requests.post(url_bot_control, data=data_ddos_control)
                return response_waf_control.json(), response_ddos_control.json()
                # print(response_bot_control.json())
                # print(response_ddos_control.json())
            except Exception as e:
                print('域名: (%s)-%s' %(domain.strip(), e))

# security_control()