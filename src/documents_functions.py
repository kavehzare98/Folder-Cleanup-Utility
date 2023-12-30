# documents_functions.py
import os
import collections

# Define file extensions for different categories in the Downloads folder
ext_dict = {'Text': ['txt'], 
            'PDF': ['pdf'],
            'Spreadsheet': ['csv', 'xls', 'xlsx'],
            'Docs' : ['doc', 'docx'],
            'Presentations': ['ppt', 'pptx'],
            'Compressed Files': ['zip', 'z', 'tar', 'pkg', 'deb']}

def createDirectories(destination_directories, base_path):
    """
    Create directories in the specified base path if they do not exist.

    Parameters:
    - destination_directories (list): List of directory names to be created.
    - base_path (str): Base path where the directories will be created.

    Returns:
    None
    """
    for dir in destination_directories:
        dir_path = os.path.join(base_path, dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            print(f"Created a directory for '{dir}'")

def mapFileExtensions(base_path):
    """
    Map files in a folder based on their file extensions.

    Parameters:
    - base_path (str): The path of the folder to be analyzed.

    Returns:
    files_mapping (defaultdict): A dictionary with file extensions as keys
                                 and lists of corresponding file names as values.
    """
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(base_path)

    # Splitting file name from extension and populating files_mapping
    for file_name in files_list:
        # Ignore hidden files (starting with dot)
        if file_name[0] != ".":
            file_ext = file_name.split('.')[-1]
            files_mapping[file_ext].append(file_name)

    return files_mapping

def moveFiles(map, base_path):
    """
    Move files to their respective folders based on file extension.

    Parameters:
    - map (defaultdict): Dictionary with file extensions and corresponding file names.
    - base_path (str): The base path where the files are located.

    Returns:
    None
    """
    for f_ext, f_list in map.items():
        for key in ext_dict.keys():
            if f_ext in ext_dict[key]:
                for file in f_list:
                    os.rename(os.path.join(base_path, file), os.path.join(base_path, key, file))