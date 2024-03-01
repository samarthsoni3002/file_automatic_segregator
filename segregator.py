import os
import glob
import time
import shutil


downloads_path = r"/home/samarth/Downloads/"
recent_file = r"/*"

prev_no_file = len(os.listdir(path = downloads_path))
print(prev_no_file)
prev_file = downloads_path + "not_a_file"

ext = []

while True:
    total_no_of_files = len(os.listdir(path = downloads_path))
    if(total_no_of_files>prev_no_file):
        prev_no_file = total_no_of_files
        files = glob.glob(downloads_path+recent_file)
        max_file = max(files,key=os.path.getctime)
        if(max_file == prev_file):
            continue
        else:
            prev_file = max_file
            file = max_file.split("/")
            file_ext = file[4].split(".")
            if(len(file_ext)>2):
                print(file_ext[-1])
                if(file_ext[-1] in ext):
                    print(max_file)
                    shutil.move((max_file),(downloads_path+file_ext[-1]))           
                else:
                    os.mkdir(f"/home/samarth/Downloads/{file_ext[1]}")
                    ext.append(file_ext[-1])
                    shutil.move((max_file),(downloads_path+file_ext[-1]))
                    print(ext)
            else:
                if(file_ext[1] in ext):
                    print(max_file)
                    shutil.move((max_file),(downloads_path+file_ext[1]))           
                else:
                    os.mkdir(f"/home/samarth/Downloads/{file_ext[1]}")
                    ext.append(file_ext[1])
                    shutil.move((max_file),(downloads_path+file_ext[1]))
                    print(ext)


            