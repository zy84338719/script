from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *
import os
# image =Image.open()
output = '/'
# image.save(output, quality = 60)

info = {'path':[]}

def make_app():
    app = Tk()
    app.title('图片压缩')
    Label(app, text = 'Image compress tool').pack()
    Listbox(app, name = 'lbox', bg = '#f2f2f2').pack(fill= BOTH, expand = True)
    Button(app,text = 'open',command =ui_getdata).pack()
    Button(app,text = 'compress',command = compress).pack()
    app.geometry('300x400')
    return app

def ui_getdata():
    file_names = askopenfilenames()
    info['path']=file_names
    lbox = app.children['lbox']
    if info['path']:
        for name in file_names:
            lbox.insert(END,name.split('/')[-1])

def compress():
    for f_path in info['path']:
        output = os.path.expandvars('$HOME')+'/Desktop/output/'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        image.save(output+'c_'+name, quality=60)

app = make_app()
app.mainloop()
