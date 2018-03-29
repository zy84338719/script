
import requests
import webbrowser
import time

api = 'https://api.github.com/repos/zy84338719/script'
web_page = 'https://www.github.com/zy84338719/script'

last_update = None

while True:
    # 获取当前api链接得到json文件
    all_info = requests.get(api)
    # 获得字典
    dict_info = all_info.json()
    # 得到文件更新时间
    cur_update = dict_info['updated_at']

    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(web_page)
        last_update = cur_update
    time.sleep(3600)