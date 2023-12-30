import os
import collections

# Define file extensions for different categories
ext_dict = {'Text': ['txt'], 
            'PDF': ['pdf'],
            'Spreadsheet': ['csv', 'xls', 'xlsx'],
            'Docs' : ['doc', 'docx'],
            'Presentations': ['ppt', 'pptx'],
            'Compressed Files': ['zip', 'z', 'tar', 'pkg', 'deb']}

# Create directories where we want to store the files
def createDirectories(destination_directories, base_path):
    for dir in destination_directories:
        dir_path = os.path.join(base_path, dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            print(f"Created a directory for '{dir}'")

# Map files from Documents folder based on their file extension
def mapFileExtensions(base_path):
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(base_path)

    # Splitting file name from extension and populating files_mapping
    for file_name in files_list:
        # Ignore hidden files (starting with dot)
        if file_name[0] != ".":
            file_ext = file_name.split('.')[-1]
            files_mapping[file_ext].append(file_name)

    return files_mapping

# Move files to their respective folders based on file extension
def moveFiles(map, base_path):
    for f_ext, f_list in map.items():
        for key in ext_dict.keys():
            if f_ext in ext_dict[key]:
                for file in f_list:
                    os.rename(os.path.join(base_path, file), os.path.join(base_path, key, file))
