import os
import sys
path = str(input('请输入你的文件所在：'))
print(path)
m = str(input('请确认路径是否正确！（yes/no）'))
if 'no' in  m or 'n' in m:
    sys.exit()

files = os.listdir(path)
file = str(input("请输入你要找的文件名：（可为空）"))
suffix = str(input('你需要查找的文件格式，请输入后缀名（如 a.png  输入 png 即可）'))
for i in files :
    if file in i and i.endswith('.'+suffix):
        print("Found it!\n"+ str(i))
