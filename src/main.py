# main.py
import download_functions as down_funcs
import documents_functions as docs_funcs
import os
from pprint import pprint as visualize

# Main function to execute the file cleanup process
def main():
    # Prompt user to choose between cleaning up Downloads or Documents folder
    user_input = int(input("Would you like to cleanup the Downloads (1) or the Documents (2) folder:\t"))

    # Validate user input
    while (user_input != 1 and user_input != 2):
        user_input = int(input("Invalid Input! Please choose Downloads (1) or Documents (2):\t"))

    # Cleanup Downloads Folder
    if user_input == 1:
        # Create directories where we want to store the files
        BASE_PATH = os.path.expanduser('~')

        # Create directories where we want to store the files
        DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Executables', 'Other', 'Programming', 'Compressed Files']
        down_funcs.createDirectories(DEST_DIRS, BASE_PATH)

        # Map files from Downloads folder based on their file extension
        DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
        files_map = down_funcs.mapFileExtensions(DOWNLOADS_PATH)

        print('\n')
        visualize(files_map)

        down_funcs.moveFiles(DOWNLOADS_PATH, BASE_PATH, files_map)

        print("Success\n")

    # Cleanup Documents Folder
    else:
        # Base path where our files are currently located - Documents
        BASE_PATH = os.path.expanduser('~/Documents')

        # Create directories where we want to store the files
        DEST_DIRS = ['Text', 'PDF', 'Spreadsheet', 'Docs', 'Presentations', 'Compressed Files']
        docs_funcs.createDirectories(DEST_DIRS, BASE_PATH)

        # Map files from Documents folder based on their file extension
        files_map = docs_funcs.mapFileExtensions(BASE_PATH)

        print("\n")
        visualize(files_map)

        docs_funcs.moveFiles(files_map, BASE_PATH)
        
        print("Success\n")
        
# Execute the main function
main()