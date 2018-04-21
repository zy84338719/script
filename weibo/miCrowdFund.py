from selenium import webdriver
import time

url = 'https://weibo.com/'
follower_url = 'https://weibo.com/p/100808abc72af610e81fe7e4ba786699bb3223/home?from=page_100808&mod=TAB#place'

def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def find_info():
    driver.get(follower_url)
    time.sleep(10)
    sel = '#Pl_Third_App__10 > div > div:nth-child(1) > div.WB_feed.WB_feed_v3.WB_feed_v4 > div:nth-child(1) > div.WB_feed_detail.clearfix > div.WB_detail > div.WB_text.W_f14'
    elem = driver.find_element_by_css_selector(sel)
    text = elem.text

    info = text.split('#')
    num = info[2:3]
    pro = info[3:4]
    info_dic = {'num':num,'pro':pro}
    return info_dic

def login():
    driver.get(url)
    time.sleep(35)
    Btn_sel = '#pl_login_form > div > div:nth-child(3) > div.info_list.login_btn > a'
    Btn = driver.find_element_by_css_selector(Btn_sel)
    Btn.click()
    time.sleep(10)
    cookies = driver.get_cookies()
    print(cookies)
    

driver = start_chrome()
if True:
    login()
else:
    f = open('cookies.txt','r')
    cookies = f.read()
    f.close()
    driver.add_cookie(cookies)
print(find_info())
driver.close()
print("Done")