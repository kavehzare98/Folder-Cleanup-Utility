import download_functions as df
import os
from pprint import pprint as visualize

def main():
    
    user_input = int(input("Would you like to cleanup the Downloads (1) or the Documents (2) folder:\t"))

    while (user_input != 1 and user_input != 2):
        user_input = int(input("Invalid Input! Please choose Downloads (1) or Documents (2):\t"))

    if user_input == 1:
        # Create directories where we want to store the files
        BASE_PATH = os.path.expanduser('~')
        DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Executables', 'Other', 'Programming']

        # Directories are created only if directory does not exist
        df.createDirectories(DEST_DIRS, BASE_PATH)

        # Map files from Downloads folder based on their file extension
        DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')

        # Map files from folder based on their file extension
        files_map = df.mapFileExtensions(DOWNLOADS_PATH)

        df.visualize(files_map)

        df.moveFiles(DOWNLOADS_PATH, BASE_PATH, files_map)
        
    elif user_input == 2:
        return

main()