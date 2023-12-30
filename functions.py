# Functions file
import os
import collections
from FileClass import *

# Create destination directories if they do not exist
def createDestDirectory(directory_list, base_path):
    for directory in directory_list:
        directory_path = os.path.join(base_path, directory)
        # Check if the path does not exist, then make directory
        if not os.path.isdir(directory_path):
            os.mkdir(directory_path)
            print(f"Path created for '{directory}'")

# Get the size of a file in MegaBytes
def getFileSize(base_p, f_name):
    file_path = os.path.join(base_p, f_name)
    file_stat = os.stat(file_path)
    size_MB = file_stat.st_size / (1024 * 1024)
    return size_MB

# Map file sizes to corresponding files
def mapSizeToFile(base_path, folder: FileClass):
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(base_path)

    for file_name in files_list:
        if folder.getFileType() not in file_name:
            continue
        else:
            size = getFileSize(base_path, file_name)
            file_sizes = folder.getSizes()

            if size >= file_sizes["large"]:
                files_mapping['Large'].append(file_name)
            elif size >= file_sizes["medium"]:
                files_mapping['Medium'].append(file_name)
            elif size >= file_sizes["small"]:
                files_mapping['Small'].append(file_name)
            else:
                files_mapping['Extra Small'].append(file_name)

    return files_mapping

# Move files to their respective directories based on size
def moveFiles(map, base_path):
    for f_size, f_list in map.items():
        for file in f_list:
            source_path = os.path.join(base_path, file)
            destination_path = os.path.join(base_path, f_size, file)
            os.rename(source_path, destination_path)