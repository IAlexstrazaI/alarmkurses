#Для работы бота вам нужно найти токен и заменить его в 9-й строчке
#Также, нужно обзавестись chat_id 
#По всем вопросам - nekker1337@gmail.com
import requests
from bs4 import BeautifulSoup
import time 
# Строчка ниже - часть апишника telegram, фактически мы просто вводим это в браузер от имени программы, в конце переменной поле текст остается открытым
y = float(0.5) #разница, рублей
x = int(30) #Время между проверками, минут 
url = "https://api.telegram.org/bot645097492:AAFFBRIL2KQOlLb1TKmVpM2Km1kUoONgR2M/sendMessage?chat_id=432886424&text=" 
user_agent = {'User-agent': 'Mozilla/5.0'} #без данных ухищерений некоторые сайты могут посчитать нас спамерами и просто не дадут доступа к контенту
http_proxy  = "http://10.10.1.10:3128"#Строчки 12 - 18 это прокси для обхода блокировки РКН
https_proxy = "https://178.168.67.89:4645"#
ftp_proxy   = "ftp://10.10.1.10:3128"#
proxyDict = {
              "http"  : http_proxy,#
              "https" : https_proxy,#
              "ftp"   : ftp_proxy}#

site = requests.get('https://www.sberometer.ru/', headers = user_agent) # производим запрос со сберометра с теми данными, что мы описали выше
soup = BeautifulSoup(site.text, "html.parser") # запихиваем в переменную весь код сайта 
kourses_of_the_day_usd_f = float(soup.find("span", id = "bcs_usd_sell").text.replace(",",".")) # здесь мы находим в куче HTML-кода нужные нам элементы по id и засовывавем их в переменную курс-ф
while True:
    time.sleep(x) #ожидаем энное кол-во часов
    site = requests.get('https://www.sberometer.ru/', headers = user_agent)#вновь проводим операцию описанную на 18 строчке...
    soup = BeautifulSoup(site.text, "html.parser")
    kourses_of_the_day_usd = float(soup.find("span", id = "bcs_usd_sell").text.replace(",","."))#... и запихтваем эти данные в переменную курс
    if  kourses_of_the_day_usd_f - kourses_of_the_day_usd > y or kourses_of_the_day_usd - kourses_of_the_day_usd_f > y: #сравниваем курс и курс-ф, и если разница заметна(скачок оказался достаточно резким)...
        TextMessage = ('''
Был полчаса назад: %g
В данный момент: %g
'''%(kourses_of_the_day_usd_f,kourses_of_the_day_usd))
        requests.post(url= url + TextMessage, proxies=proxyDict)# ...то отправляем соответствующее сообщение 
    kourses_of_the_day_usd_f = kourses_of_the_day_usd# важная строчка - в ней мы заменяем старые данные новыми, и меняем им название, освобождая переменную под новый запрос через час 
