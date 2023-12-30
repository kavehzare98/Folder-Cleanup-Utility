import os
import collections
from pprint import pprint

# Directories are created only if directory does not exist
def createDirectories(destination_list, base_path):
    for dest_dir in destination_list:
        dir_path = os.path.join(base_path, dest_dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            print(f"Created a directory for '{dest_dir}'")

# Map files from folder based on their file extension
def mapFileExtensions(path):
    # Create map
    files_mapping = collections.defaultdict(list)
    # Create a list of files in directory
    files_list = os.listdir(path)

    # Splitting file name from extension
    for file_name in files_list:
        # Ignore hidden files
        if file_name[0] != ".":
            # Extract file extension
            file_ext = file_name.split(".")[-1]
            files_mapping[file_ext].append(file_name)

