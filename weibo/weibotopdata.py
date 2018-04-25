
# 热搜网址
# "http://s.weibo.com/top/summary?cate=realtimehot"
#
# "#realtimehot > tbody > tr:nth-child(1)"
# "#realtimehot > tbody > tr:nth-child(1) > td.td_01"   #热搜序号
# "#realtimehot > tbody > tr:nth-child(1) > td.td_02"    #热搜关键词
# "#realtimehot > tbody > tr:nth-child(1) > td.td_03"    #搜索热度


from selenium import webdriver
import time
import pandas as pd

url = "http://s.weibo.com/top/summary?cate=realtimehot"

def start_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def Top_info():
    data = []
    for i in range(1,52):

        # sel_topic 热搜话题
        # sel_hot 热搜程度
        # sel_url 热搜链
        sel_= '#realtimehot > tbody > tr:nth-child('+str(i)+')'
        sel_topic = sel_+' > td.td_02'
        sel_url = sel_topic + ' >  div > p > a '
        sel_hot = sel_+' > td.td_03'

        url = driver.find_element_by_css_selector(sel_url).get_attribute('href')
        topic = driver.find_element_by_css_selector(sel_topic).text
        hot = driver.find_element_by_css_selector(sel_hot).text

        raw = {'topic':topic,'hot':hot,'url':url}
        data.append(raw)
    return data

if __name__ == '__main__':
    driver = start_chrome()
    driver.get(url)
    time.sleep(3)
    data = Top_info()
    dataframe = pd.DataFrame(data)


    date = pd.datetime.now()
    today = date.replace(hour=0 ,minute=0, second=0,microsecond=0)
    dataframe['time'] = today
    str_today = today.strftime('%y-%m-%d')
    dataframe.to_csv(str_today+'.csv',index=False,sep=',')
    print("Done")
    driver.close()
    driver.quit()