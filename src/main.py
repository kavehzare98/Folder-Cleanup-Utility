import download_functions as down_funcs
import documents_functions as docs_funcs
import os
from pprint import pprint as visualize

def main():
    
    user_input = int(input("Would you like to cleanup the Downloads (1) or the Documents (2) folder:\t"))

    while (user_input != 1 and user_input != 2):
        user_input = int(input("Invalid Input! Please choose Downloads (1) or Documents (2):\t"))

    # Cleanup Downloads Folder
    if user_input == 1:
        # Create directories where we want to store the files
        BASE_PATH = os.path.expanduser('~')

        # Create directories where we want to store the files
        DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Executables', 'Other', 'Programming', 'Compressed Files']

        # Directories are created only if directory does not exist
        down_funcs.createDirectories(DEST_DIRS, BASE_PATH)

        # Map files from Downloads folder based on their file extension
        DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')

        # Map files from folder based on their file extension
        files_map = down_funcs.mapFileExtensions(DOWNLOADS_PATH)

        visualize(files_map)

        down_funcs.moveFiles(DOWNLOADS_PATH, BASE_PATH, files_map)

    # Cleanup Documents Folder
    elif user_input == 2:
        # Base path where our files are currently located - Documents
        BASE_PATH = os.path.expanduser('~/Documents')

        # Create directories where we want to store the files
        DEST_DIRS = ['Text', 'PDF', 'Spreadsheet', 'Docs', 'Presentations', 'Compressed Files']

        # Directories are created only if directory does not exist
        docs_funcs.createDirectories(DEST_DIRS, BASE_PATH)

        # Map files from Documents folder based on their file extension
        files_map = docs_funcs.mapFileExtensions(BASE_PATH)

        # Print the initial mapping for visual inspection
        visualize(files_map)

        # Move files to their respective folders based on file extension
        docs_funcs.moveFiles(files_map, BASE_PATH)

    else:
        print("ERROR! Unable to perform requested task.")

main()