#upload custom certificate
from email.mime import base
import re, os, sys, os.path
import requests, base64
from pathlib import Path
from config import api_id, api_key, account_id, site_ip, get_site_status
# from AddSite import read_domain_files

url_upload_ssl = 'https://my.imperva.com/api/prov/v1/sites/customCertificate/upload'
def site_id ():
    return get_site_status()

crt_key = {}
def base64_crt_key(domain):  
    main_domain_crt = domain.split(".")[-2] + '.' + domain.split(".")[-1] + "_chain.crt"
    main_domain_key = domain.split(".")[-2] + '.' + domain.split(".")[-1] + "_key.key"
    current_path = Path(os.path.split(os.path.realpath(__file__))[0]) / "ssl/"
    crt_path = current_path / main_domain_crt
    key_path = current_path / main_domain_key
    if os.path.isfile(crt_path) and os.path.isfile(key_path):
        f_crt = open(crt_path, 'r').read()
        f_key = open(key_path, 'r').read()
        content_crt = f_crt.encode()
        content_key = f_key.encode()
        encode_crt = base64.b64encode(content_crt).decode()
        encode_key = base64.b64encode(content_key).decode()
        crt_key[encode_crt] = encode_key
        return crt_key
    else:
        return domain + ":该域名证书或key文件不存在"

    # content1 = content.encode(encoding='utf-8')
def upload_ssl():
    with open('./domain.txt', 'r', encoding="utf-8") as file:
        domain_site = get_site_status()
        for domain in file:
            domain = domain.strip()
            site_id = domain_site[domain]
            if type(base64_crt_key(domain)).__name__ == 'dict':
                for key,value in base64_crt_key(domain).items():
                    encode_crt = key
                    encode_key = value
                    data_site = {
                        'api_id': api_id,
                        'api_key': api_key,
                        'site_id': site_id,
                        'certificate': encode_crt,
                        'private_key': encode_key,
                        'passphrase': ''
                    }
                    response = requests.post(url_upload_ssl, data=data_site)
                    return response.json()
# def get_site_id():
#     with open('./domain.txt', 'r', encoding="utf-8") as file:
#         domain_site = get_site_status()
#         for domain in file:
#             domain = domain.strip()
            # site_id = domain_site[domain]
# upload_ssl()