
import requests
import webbrowser
import time

api = 'https://api.github.com/repos/zy84338719/script'
web_page = 'https://www.github.com/zy84338719/script'


last_update = None
all_info = requests.get(api)
dict_info = all_info.json()
cur_update = dict_info['updated_at']

while True:
    if not last_update:
        last_update =cur_update

    if last_update <cur_update:
        webbrowser.open(web_page)
    time.sleep(30)
