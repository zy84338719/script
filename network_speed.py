import psutil
import time
from tkinter import *




# def fun1():
#     print('hi')
#     app.after(1000,fun1)
#
# app =Tk()
# app.after(1000,fun1)
# app.mainloop()

def make_app():
    app = Tk()
    app.title('Speed Monitor')
    app.geometry('150x65')
    app.config(bg ='#303030')
    Label(name = 'lb2',
          text =  '上行：      kb/s',
          font = ('Hack',20,'bold'),
          bg = '#303030',
          fg = 'white'
          ).pack()
    Label(name = 'lb3',
          text =  '下行：      kb/s',
          font = ('Hack',20,'bold'),
          bg = '#303030',
          fg = 'white'
          ).pack()
    return app

def speed_test():
    s1 = psutil.net_io_counters(pernic=True)['en0']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['en0']
    recv_result = s2.bytes_recv - s1.bytes_recv
    send_result = s2.bytes_sent - s1.bytes_sent

    result = {
        '上行':'上行：'+str(send_result / 1024)+'kb/s',
        '下行':'下行：'+str(recv_result / 1024)+'kb/s'
        }
    return result

def ui_update(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text = data['上行'])
    lb3 = app.children['lb3']
    lb3.config(text=data['下行'])
    app.after(1000,lambda :ui_update(do))

app = make_app()
app.after(1000, lambda :ui_update(speed_test))
app.mainloop()
