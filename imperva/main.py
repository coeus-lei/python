from urllib import response
import requests,random,string,json
import AddSite
import UploadSsl
import ModifyCacheMode
import BotAccessControl
import AddRulesFilter
import Redirect

#add website
url_add_site = 'https://my.imperva.com/api/prov/v1/sites/add'
AddSite.read_domain_files()
#upload ssl
url_upload_ssl = 'https://my.imperva.com/api/prov/v1/sites/customCertificate/upload'
UploadSsl.upload_ssl()
#Caching Mode 
url_cache_mode = 'https://my.imperva.com/api/prov/v1/sites/performance/cache-mode'
ModifyCacheMode.modify_cache_mode()
#bot access control
url_bot_control = 'https://my.imperva.com/api/prov/v1/sites/configure/security'
BotAccessControl.security_control()
#Rules Filter
url_rules_filter = 'https://my.imperva.com/api/prov/v1/sites/incapRules/edit'
AddRulesFilter.add_rules_filter()
#WAF Threats and DDos
url_waf_ddos = 'https://my.imperva.com/api/prov/v1/sites/configure/security'
#Redirect HTTPS and Full domain
url_redirect = 'https://my.imperva.com/api/prov/v1/sites/performance/advanced'
Redirect.redirect_url()
#website advanced caching setting
url_cache_set = 'https://my.imperva.com/api/prov/v1/sites/performance/advanced'
