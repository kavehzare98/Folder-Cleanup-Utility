import os
import collections
from pprint import pprint as visualize

# Define file extensions for different categories
EXT_TXT = ['txt']
EXT_PDF = ['pdf']
EXT_SPRDS = ['csv', 'xls', 'xlsx']
EXT_DOCS = ['doc', 'docx']
EXT_PRES = ['ppt', 'pptx']
EXT_COMPR = ['zip', 'z', 'tar', 'pkg', 'deb']

# Base path where our files are currently located - Documents
BASE_PATH = os.path.expanduser('~/Documents')

# Create directories where we want to store the files
DEST_DIRS = ['Text', 'PDF', 'Spreadsheet', 'Docs', 'Presentations', 'Compressed Files']
for dir in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, dir)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map files from Documents folder based on their file extension
files_mapping = collections.defaultdict(list)
files_list = os.listdir(BASE_PATH)

# Splitting file name from extension and populating files_mapping
for file_name in files_list:
    # Ignore hidden files (starting with dot)
    if file_name[0] != ".":
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

# Print the initial mapping for visual inspection
visualize(files_mapping)

# Move files to their respective folders based on file extension
for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_PDF:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, 'PDF', file))
    elif f_ext in EXT_TXT:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, 'Text', file))
    elif f_ext in EXT_SPRDS:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, 'Spreadsheet', file))
    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, 'Docs', file))
    elif f_ext in EXT_PRES:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, 'Presentations', file))
    elif f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, 'Compressed Files', file))
