# download_functions.py
import os
import collections
from pprint import pprint

# Define file extension categories for different types of files
ext_dict = {'Music': ['mp3', 'wav', 'wma', 'mid', 'midi'], 
            'Movies': ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264'],
            'Pictures': ['png', 'jpg', 'JPG', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'tiff', 'tif', 'HEIC', 'webp', 'ARW'],
            'Documents': ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'ppt', 'pptx'],
            'Compressed Files': ['zip', 'z', 'tar', 'pkg', 'deb'],
            'Executables': ['dmg', 'exe', 'iso'],
            'Programming': ['py', 'cpp', 'h']}


def createDirectories(destination_list, base_path):
    """
    Create directories in the specified base path if they do not exist.

    Parameters:
    - destination_list (list): List of directory names to be created.
    - base_path (str): Base path where the directories will be created.

    Returns:
    None
    """
    for dest_dir in destination_list:
        dir_path = os.path.join(base_path, dest_dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            print(f"Created a directory for '{dest_dir}'")


def mapFileExtensions(source_path):
    """
    Map files in a folder based on their file extension.

    Parameters:
    - source_path (str): The path of the folder to be analyzed.

    Returns:
    files_mapping (defaultdict): A dictionary with file extensions as keys
                                 and lists of corresponding file names as values.
    """
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(source_path)

    # Splitting file name from extension
    for file_name in files_list:
        # Ignore hidden files
        if file_name[0] != ".":
            # Extract file extension
            file_ext = file_name.split(".")[-1]
            files_mapping[file_ext].append(file_name)
    return files_mapping


def moveFiles(source_path, base_path, map):
    """
    Move files to their respective folders based on file extension.

    Parameters:
    - source_path (str): The base path where the files are located.
    - base_path (str): The base path where the files will be moved.
    - map (defaultdict): Dictionary with file extensions and corresponding file names.

    Returns:
    None
    """
    for f_ext, f_list in map.items():
        for key in ext_dict.keys():
            if f_ext in ext_dict[key]:
                for file in f_list:
                    os.rename(os.path.join(source_path, file), os.path.join(base_path, key, file))
