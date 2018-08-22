import requests
from bs4 import BeautifulSoup
import time 

url = "https://api.telegram.org/bot<place for your token>/sendMessage?chat_id=432886424&text="
user_agent = {'User-agent': 'Mozilla/5.0'}
http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://178.168.67.89:4645"
ftp_proxy   = "ftp://10.10.1.10:3128"
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy}

site = requests.get('https://www.sberometer.ru/', headers = user_agent)
soup = BeautifulSoup(site.text, "html.parser")
kourses_of_the_day_usd_f = soup.find("span", id = "bcs_usd_sell").text
while True:
    time.sleep(3600)
    site = requests.get('https://www.sberometer.ru/', headers = user_agent)
    soup = BeautifulSoup(site.text, "html.parser")
    kourses_of_the_day_usd = soup.find("span", id = "bcs_usd_sell").text
    if  kourses_of_the_day_usd_f - kourses_of_the_day_usd > 0.6 or kourses_of_the_day_usd - kourses_of_the_day_usd_f > 0.6:
        TextMessage = ('''
Был час назад: %g
В данный момент: %g
'''%(kourses_of_the_day_usd_f,kourses_of_the_day_usd))
        requests.post(url= url + TextMessage, proxies=proxyDict)
    kourses_of_the_day_usd_f = kourses_of_the_day_usd
