from selenium import webdriver
from bs4 import BeautifulSoup
import time #預防網頁有防備限制設定秒數
import random #秒數隨機

url = 'http://insider.espn.com/nba/hollinger/statistics/_/page/'

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options,
                             executable_path='/Users/kevin/Web Clawer DEMO/chromedriver')
    chrome.set_page_load_timeout(10)
    for i in range(1, 9):
        _url = url + str(i)
        print(_url)
        chrome.get(_url)
        soup = BeautifulSoup(chrome.page_source, 'html5lib')
        trs = soup.find('tbody').find_all('tr')
        for tr in trs:
            tds = [td for td in tr.children]
            rk = tds[0].text.strip()
            if rk =='RK' or len(tds)<2:   #欄位值是RK或是蘭位數小於2就跳過
                continue
            name = tds[1].text
            per = tds[11].text
            print('%s :%s' % (name, per))
        wait = random.randint(2,6) #等2到6的隨機秒數
        print('wait time : %d' % wait)
        time.sleep(wait)
    
    
finally:
    chrome.quit()