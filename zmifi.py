from selenium import webdriver
import pandas as pd
import time

url = 'http://192.168.21.1/'


def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver


def login(driver):
    driver.get(url)
    sel_passwd = '#tbarouter_password'
    elem_passwd = driver.find_element_by_css_selector(sel_passwd)
    elem_passwd.send_keys('zimifi')

    sel_login = '#btnSignIn'
    Btn_login = driver.find_element_by_css_selector(sel_login)
    Btn_login.click()

def find_info(driver):
    
    '''
    sign 信号强度
    power 电量剩余
    flow 流量剩余
    '''

    sel_flow = '#lTotalPackets'
    flow = driver.find_element_by_css_selector(sel_flow)
    sel_power = '#lDashBatteryQuantity'
    power = driver.find_element_by_css_selector(sel_power)
    sel_sign = '#imgSignalStrength'
    sign_raw = driver.find_element_by_css_selector(sel_sign)
    sign = sign_raw.get_attribute('src').split('/')[-1].split('.')[0][-1]    
    info = {'flow':flow.text,'power':power.text,'sign':sign}
    return info

driver = start_chrome()
login(driver)
info = find_info(driver)
DataFrame = pd.DataFrame([info])
DataFrame.to_csv('flow.csv',index=False, sep=',')
driver.close()
driver.quit()