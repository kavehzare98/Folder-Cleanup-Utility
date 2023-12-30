import os
import collections
from pprint import pprint

# Define file extension categories
ext_dict = {'Music': ['mp3','wav','wma','mid','midi'], 
            'Movies': ['mp4', 'mpg', 'mpeg', 'avi','mov','flv','mkv', 'mwv', 'm4v', 'h264'],
            'Pictures': ['png','jpg','JPG','jpeg','gif','svg','bmp','psd','tiff','tif','HEIC'],
            'Documents': ['txt','pdf','csv','xls','xlsx','ods','doc','docx','ppt','pptx'],
            'Compressed Files': ['zip', 'z', 'tar', 'pkg', 'deb'],
            'Executables': ['dmg','exe','iso'],
            'Programming': ['py','cpp', 'h']}

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
        for key in ext_dict.keys():
            if f_ext in ext_dict[key]:
                for file in f_list:
                    os.rename(os.path.join(source_path, file), os.path.join(base_path, key, file))