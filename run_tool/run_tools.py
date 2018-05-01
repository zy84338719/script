from runpy import run_path
from tkinter import *
from tkinter.filedialog import *
import multiprocessing
import os



# 创建GUI框体
def make_app():
    app = Tk()
    Listbox(app, name='listb').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=get_path).pack()
    Button(app, text='run', command=run_script).pack()
    Button(app, text='stop', command=stop_script).pack()
    app.geometry('300x400')
    return app
# 填充listbox
def get_path():
    file_names = askopenfilenames()
    info['path'] = file_names
    lbox = app.children['lbox']
    if info['path']:
        for name in file_names:
            lbox.insert(END, name.split('/')[-1])

def ui_make_list():
    # 获取listbox，以便修改其内容
    listb = app.children['listb']
    for d in os.listdir(path):
        if d.split('.')[-1] == 'py':
            listb.insert(END,d)
# 运行脚本文件
def run_script():
    # 获取listbox
    listb = app.children['listb']
    # 获取listbox中当前点击的的元素
    s_path = listb.get(ACTIVE)

    # 检查需要run的脚本是否已经在运行
    for child in multiprocessing.active_children():
        if child.name == s_path:
            print("This script is already running.")
            return

    p = multiprocessing.Process(name=s_path, target=run_path, args=(s_path,))
    p.start()
# 停止脚本运行

def stop_script():
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    for p in multiprocessing.active_children():
        if p.name == s_path:
            p.terminate()
            return
    print("This script is not running.")

# 监测程序状态
def watcher():
    print(multiprocessing.active_children())
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000, watcher)



if __name__ == '__main__':
    app = make_app()
    app.after(100, ui_make_list)
    # app.after(0, watcher)
    app.mainloop()
