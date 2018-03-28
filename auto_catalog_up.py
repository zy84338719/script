import os
import shutil
import pathlib
import sys

path = str(input("请输入你整理后的文件路径:"))
print(path)
m = str(input('请确认路径是否正确！（yes/no）'))
if 'no' in  m or 'n' in m:
    sys.exit()

image = pathlib.Path(path+'/image')
if image.exists():
    os.makedirs(path + '/image')
document = pathlib.Path(path+'/document')
if document.exists():
    os.makedirs(path + '/document')

image_suffix = ['jpg','png','gif']
doc_suffix = ['doc','docx','ppt']

for i in image_suffix:
    cur_path = path + '/' + i
    print(cur_path)
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(cur_path + '/' +f,path +'/image')
    os.removedirs(cur_path)

for d in doc_suffix:
    cur_path = path + '/' + d
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(cur_path + '/' +f,path +'/document')
    os.removedirs(cur_path)
