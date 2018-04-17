from tkinter import *
import os
app =Tk()
app.title('用户目录隐藏文件查看')
# btn = Button(text = 'tick me')
# btn.pack()
# app.mainloop()

# 获取当前用户目录
# print(path)
# print( os.path.expandvars('$HOME'))
# print( os.path.expanduser('~') )


label = Label(text = 'ALL hidden files',font=('Hack',24,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill = BOTH,expand = True)


path = os.environ['HOME']
files = os.listdir(path)
for f in files:
    if f.startswith('.'):
        listbox.insert(END, f)



app.mainloop()
