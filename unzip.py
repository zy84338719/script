import os
import shutil



def scan_file():
    files = os.listdir()
    for i in files:
        if i.endswith('.zip'):
            return i
def unzip_it(file):
    file_name = file.split('.')[0]
    targe_path = './'+ file_name
    os.makedirs(targe_path)
    shutil.unpack_archive(file,targe_path)
def delete(file):
    shutil.move(file,os.path.expanduser('~')+'/.Trash')

while True:
    zip_file = scan_file()
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)
