import requests
import time
import pandas as pd

def weather(cities):
    weather_api = 'https://www.sojson.com/open/api/weather/json.shtml?city='
    data = []
    for c in cities:
        c_info = requests.get(weather_api+c).json()
        city = c_info['city']
        date = c_info['date']
        pm25 = c_info['data']['pm25']
        pm10 = c_info['data']['pm10']
        quality = c_info['data']['quality']
        C = c_info['data']['wendu']
        C_max = c_info['data']['forecast'][0]['high']
        C_min = c_info['data']['forecast'][0]['low']
        type = c_info['data']['forecast'][0]['type']
        advise = c_info['data']['ganmao']
        c_dic ={
                'city':city,
                'date':date,
                'pm25':pm25,
                'pm10':pm10,
                'quality':quality,
                'C':C,
                'C_max':C_max,
                'C_min':C_min,
                'type':type,
                'advise':advise
                }
        data.append(c_dic)
        time.sleep(3)
    return data


if __name__ == '__main__':
    data = weather(['北京', '上海','镇江','天津','河北'])
    dataframe = pd.DataFrame(data)
    dataframe.to_csv("天气数据.csv", index=False, sep=',')
