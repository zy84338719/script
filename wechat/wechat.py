from wxpy import *
import csv
import time
import datetime
import os

def read_info():
    f = open('天气数据.csv','r',encoding='utf8')
    reader =csv.DictReader(f)
    return [info for info in reader]

def limit_msg():
    pass

def weather_msg(raw_info,City):
    try:
        for info in raw_info:
            if City == info['city']:
                t = '{city}{date},\n天气{type}，气温{C_min}-{C_max}，\nPM2.5浓度:{pm25}，空气质量{quality}。\n\n建议：{advise}'
                return t.format(date=info['date'],
                                city = info['city'],
                                type=info['type'],
                                C_max = info['C_max'],
                                C_min = info['C_min'],
                                pm25 = info['pm25'],
                                advise = info['advise'],
                                quality = info['quality']
                                 )
    except KeyError:
        return None



def family_send(msg,bot):

    m =bot.groups().search('大家庭')[0]
    m.send(msg)
    time.sleep(3)

def self_send(msg,bot):
    zj = bot.friends().search('张易1')[0]
    zj.send(msg)
    time.sleep(3)

def do(bot):
    raw_info = read_info()
    f_msg = weather_msg(raw_info,'北京')
    family_send(f_msg,bot)

    s_msg = weather_msg(raw_info,'镇江')
    self_send(s_msg, bot)


# 定时程序
def timerFun(sched_Timer,bot):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now > sched_Timer and now < sched_Timer+datetime.timedelta(minutes=1):
            os.system('python3 ./get\ weather/weather.py')
            do(bot)
            flag = 1
            print('程序执行成功')
            time.sleep(60)
        else:
            if flag == 1:
                sched_Timer = sched_Timer+datetime.timedelta(days=1)
                # sched_Timer = sched_Timer + datetime.timedelta(minutes=1)
                flag = 0

        time.sleep(30)

if __name__ == '__main__':
    bot = Bot(console_qr = 2)
    now = datetime.datetime.now()
    sched_Timer = datetime.datetime(now.year, now.month, now.day, 7, 30)
    # sched_Timer = datetime.datetime(now.year, now.month, now.day , now.hour, now.minute+1)
    print('程序运行时间{}'.format(sched_Timer))
    timerFun(sched_Timer,bot)

