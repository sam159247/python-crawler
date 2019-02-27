import numpy as np
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

def replace_str(s):
    s = s.replace('\r\n', '')
    s = s.replace(' ', '')
    s = s.replace(u'\xa0', '')
    return s

def get_hiddenvalue(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    viewstate = soup.find('input', {'name': '__VIEWSTATE'})["value"]
    eventvalidation = soup.find('input', {'name': '__EVENTVALIDATION'})["value"]
    viewstategenerator = soup.find('input', {'name': '__VIEWSTATEGENERATOR'})["value"]
    return viewstate,eventvalidation,viewstategenerator

VIEWSTATE, EVENTVALIDATION, VIEWSTATEGENERATOR = get_hiddenvalue('https://www.taiwanpay.com.tw/content/info/others.aspx')

country = []
place_name = []
address = []
total_pages = 157

for x in range(1, total_pages):
    payload = {
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$AspNetPager1',
        '__EVENTARGUMENT': x,
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        '__EVENTVALIDATION': EVENTVALIDATION,
        'ctl00$ContentPlaceHolder1$ddlCountry': '全部國家',
        'ctl00$ContentPlaceHolder1$txtTitle': '',
        'ctl00$ContentPlaceHolder1$AspNetPager1_input': '1',
        'ctl00$OnTestCheck': 'N'
    }
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

    r = requests.post('https://www.taiwanpay.com.tw/content/info/others.aspx', data=payload, headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    all_trs = soup.body.table.tbody.find_all('tr')
    sleep = np.random.randint(2,4)
    time.sleep(sleep)
    for tr in all_trs:
        try:
            data = tr.find_all('td')
            country.append(replace_str(data[0].text))
            place_name.append(replace_str(data[2].text))
            address.append(replace_str(data[3].text))
        except AttributeError:
            country.append('NaN')
            place_name.append('NaN')
            address.append('NaN')
    print("Page:", x, "\n")
   

address = [a.replace('\u3000', ' ') for a in address]
df = pd.DataFrame({'名稱': place_name, '地址': address, '國家': country}, columns=["國家","名稱","地址"])
df.to_csv('mapsdata.csv', index=False, sep=',')
