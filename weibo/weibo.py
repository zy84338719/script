from selenium import webdriver
import time
url = "https://weibo.com/bgsxy?refer_flag=1001030103_&is_hot=1"
def start_chrome():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.start_client()
    return driver

def find_info():
    sel = '#Pl_Official_MyProfileFeed__21 > div > div:nth-child(2) > div.WB_feed_handle > div > ul > li > a > span > span > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]

driver = start_chrome()

driver.get(url)
time.sleep(10)
info = find_info()
print(info)
driver.close()
driver.quit()