# Import necessary modules
import os
import collections
from pprint import pprint as visualize
from funcs import *

# Create directories where we want to store the files
BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Executables', 'Other', 'Programming']

# Directories are created only if directory does not exist
createDirectories(DEST_DIRS, BASE_PATH)

# Map files from Downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')

# Map files from folder based on their file extension
files_map = mapFileExntensions(DOWNLOADS_PATH)

visualize(files_map)

moveFiles(DOWNLOADS_PATH, BASE_PATH, files_map)