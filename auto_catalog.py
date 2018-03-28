#
import  os
import shutil
import sys


path = str(input('请输入你所要整理的路径：'))
print(path)
m = str(input('请确认路径是否正确！（yes/no）'))
if 'no' in  m or 'n' in m:
    sys.exit()
files = os.listdir(path)

if '.DS_Store' in files:
    files.remove('.DS_Store')

for i in files:
    folder_name = path +'/'+i.split('.')[-1]
    if not os.path.exists(folder_name):
        if i.split('.')[-1] not in 'py':
            os.mkdir(folder_name)
            shutil.move(path + '/' + i.split('.')[-1] + '/' + i, folder_name)
    else:
        shutil.move(path + '/' + i, folder_name)
