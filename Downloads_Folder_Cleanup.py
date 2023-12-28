# Import necessary modules
import os
import collections
from pprint import pprint

# Define file extension categories
EXT_AUDIO = ['mp3','wav','wma','mid','midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi','mov','flv','mkv', 'mwv', 'm4v', 'h264']
EXT_IMGS = ['png','jpg','JPG','jpeg','gif','svg','bmp','psd','tiff','tif','HEIC']
EXT_DOCS = ['txt','pdf','csv','xls','xlsx','ods','doc','docx','ppt','pptx']
EXT_COMPR = ['zip', 'z', 'tar', 'pkg', 'deb']
EXT_INSTL = ['dmg','exe','iso']
EXT_PROG = ['py','cpp', 'h']

# Create directories where we want to store the files
BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Executables', 'Other', 'Programming']

# Directories are created only if directory does not exist
for dest_dir in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, dest_dir)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map files from Downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

# Splitting file name from extension
for file_name in files_list:
    # Ignore hidden files
    if file_name[0] != ".":
        # Extract file extension
        file_ext = file_name.split(".")[-1]
        files_mapping[file_ext].append(file_name)

# Pretty print the files mapping
pprint(files_mapping)

# Move all files given a file extension to a target directory
for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_INSTL:
        # Move installer files to the 'Executables' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Executables', file))
    elif f_ext in EXT_AUDIO:
        # Move audio files to the 'Music' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Music', file))
    elif f_ext in EXT_PROG:
        # Move programming files to the 'Programming' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Programming', file))
    elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
        # Move document and compressed files to the 'Documents' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Documents', file))
    elif f_ext in EXT_IMGS:
        # Move image files to the 'Pictures' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Pictures', file))
    elif f_ext in EXT_VIDEO:
        # Move video files to the 'Movies' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Movies', file))
    else:
        # Move other files to the 'Other' directory
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Other', file))