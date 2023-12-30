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

# Directories are created only if directory does not exist
def createDirectories(destination_list, base_path):
    for dest_dir in destination_list:
        dir_path = os.path.join(base_path, dest_dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            print(f"Created a directory for '{dest_dir}'")

# Map files from folder based on their file extension
def mapFileExtensions(source_path):
    # Create map
    files_mapping = collections.defaultdict(list)
    # Create a list of files in directory
    files_list = os.listdir(source_path)

    # Splitting file name from extension
    for file_name in files_list:
        # Ignore hidden files
        if file_name[0] != ".":
            # Extract file extension
            file_ext = file_name.split(".")[-1]
            files_mapping[file_ext].append(file_name)
    return files_mapping


# Move all files given a file extension to a target directory
def moveFiles(source_path, base_path, map):
    for f_ext, f_list in map.items():
        if f_ext in EXT_INSTL:
            # Move installer files to the 'Executables' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Executables', file))
        elif f_ext in EXT_AUDIO:
            # Move audio files to the 'Music' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Music', file))
        elif f_ext in EXT_PROG:
            # Move programming files to the 'Programming' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Programming', file))
        elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
            # Move document and compressed files to the 'Documents' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Documents', file))
        elif f_ext in EXT_IMGS:
            # Move image files to the 'Pictures' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Pictures', file))
        elif f_ext in EXT_VIDEO:
            # Move video files to the 'Movies' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Movies', file))
        else:
            # Move other files to the 'Other' directory
            for file in f_list:
                os.rename(os.path.join(source_path, file), os.path.join(base_path, 'Other', file))