from cmath import exp
from email import message
import ssl, socket  
import requests  
from dateutil import parser  
import pytz  
import datetime, time
import telegram

requests.packages.urllib3.disable_warnings()  
  
try:  
    _create_unverified_https_context = ssl._create_unverified_context  
except AttributeError:  
    # Legacy Python that doesn't verify HTTPS certificates by default  
    pass  
else:  
    # Handle target environment that doesn't support HTTPS verification  
    ssl._create_default_https_context = _create_unverified_https_context  
  
  
def get_domain_content(domain):  
    requests.packages.urllib3.disable_warnings()  
    url = 'https://' + domain  
    response = requests.get(url, verify=False).headers
    print(response)  
  
  
def get_my_domain(mydomain):  
    try:  
        socket.setdefaulttimeout(5)  
        my_addr = socket.getaddrinfo(mydomain, None)  
        c = ssl.create_default_context()  
        s = c.wrap_socket(socket.socket(), server_hostname=mydomain)  
        s.connect((mydomain, 443))  
        my_cert = s.getpeercert()  
        get_my_cert_dated(mydomain, my_cert, my_addr)  
    except ssl.CertificateError and socket.gaierror as e:  
        pass  
  
def days(str1, str2):
    date1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    # print(num)
    return num

def msg_push(message):
    bot = telegram.Bot(token="1661802605:AAEBujopJfJiE5YcvBiBl-IP6KY6FcrGL_0")
    bot.send_message(chat_id='-739268984', text=message)

def get_my_cert_dated(domain, certs, my_addr):  
    cert_beginning_time = parser.parse(certs['notBefore']).astimezone(pytz.utc)  
    cert_end_time = parser.parse(certs['notAfter']).astimezone(pytz.utc)
    # cert_end_time_str = datetime.datetime.strptime(cert_end_time[0:10], "%Y-%m-%d")
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # print(days(str(cert_end_time), str(local_time)))
    # print('域名:(%s)  证书失效时间: %s' % (domain,  cert_end_time))
    expired_days = days(str(cert_end_time), str(local_time))
    # print(expired_days)
    if (expired_days < 7):
        # print('域名:(%s) 证书还有: %s' % (domain, expired_days))
        message = '域名:(%s)  证书过期天数: %s 证书失效时间： %s' % (domain,  expired_days, cert_end_time)
        msg_push(message)
        # print('域名:(%s)  证书过期天数: %s 证书失效时间： %s' % (domain,  expired_days, cert_end_time))
  
def read_domain_files():
    with open('./domain.txt', 'r',
              encoding="utf-8") as file:
        for domain in file:
            try:
                get_my_domain(domain.strip())
            except Exception as e:
                print('域名: (%s)-%s' %(domain.strip(), e))
  
# print("code") 
if __name__ == "__main__":
    read_domain_files()
