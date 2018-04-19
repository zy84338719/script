from wxpy import *
import csv
import time
import datetime
import os

def read_info():
    f = open('.././get weather/天气数据.csv','r',encoding='utf8')
    reader =csv.DictReader(f)
    return [info for info in reader]

def limit_msg():
    pass

def make_msg(raw_info):
    t = '{city}{date},天气{type}，最高气温{C_max},最低气温{C_min}，空气PM2.5浓度{pm25}，建议：{advise}'
    return [t.format(date=info['date'],
                     city = info['city'],
                     type=info['type'],
                     C_max = info['C_max'],
                     C_min = info['C_min'],
                     pm25 = info['pm25'],
                     advise = info['advise']
                     ) for info in raw_info]

def send(msg,bot):

    大家庭 =bot.groups().search('大家庭')[0]
    大家庭.send(msg)
    time.sleep(3)

def do(bot):
    raw_info = read_info()
    msg = make_msg(raw_info)
    send(msg[0],bot)


# 定时程序
def timerFun(sched_Timer,bot):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now == sched_Timer:
            os.system('python3 weather.py')
            do(bot)
            flag = 1
        else:
            if flag ==1:
                sched_Timer = sched_Timer+datetime.timedelta(days=1)
                flag = 0

if __name__ == '__main__':
    bot = Bot()
    sched_Timer = datetime.datetime(2018, 4, 20, 7, 30)
    print('程序运行时间{}'.format(sched_Timer))
    do(bot)
    timerFun(sched_Timer,bot)