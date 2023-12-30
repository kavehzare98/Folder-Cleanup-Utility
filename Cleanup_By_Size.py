# Main file
from pprint import pprint as visualize
from functions import *
from FileClass import *

def main():

    # Create a FileClass instance representing a folder of PDFs
    FOLDER = FileClass({"large": 20, "medium": 5, "small": 0.2}, ".pdf", "~/Documents/PDF")

    # Find base path where files are located via .expanduser which automatically expands path
    BASE_PATH = os.path.expanduser(FOLDER.getFilePath())

    # Create destination directories based on the provided folder instance
    createDestDirectory(FOLDER.getDestinations(), BASE_PATH)

    # Map user-defined file sizes to lists of files
    file_map = mapSizeToFile(BASE_PATH, FOLDER)

    # Print the initial mapping for visual inspection
    visualize(file_map)

    # Move files to their respective directories based on size
    moveFiles(file_map, BASE_PATH)

# Run Program
main()