import os


downloads_path = "C:\\Users\\samar\\Downloads"


prev_no_file = len(os.listdir(path = downloads_path))
print(prev_no_file)

while True:
    total_no_of_files = len(os.listdir(path = downloads_path))
    if(total_no_of_files>prev_no_file):
        prev_no_file = total_no_of_files
        print(prev_no_file)

