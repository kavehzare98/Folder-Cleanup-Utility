# File Cleanup Script Documentation

This documentation provides a detailed explanation of the file cleanup script, which is split across three Python files: `documents_functions.py`, `downloads_functions.py`, and `main.py`.

## A. `documents_functions.py`

    1. `ext_dict`

        - A dictionary that defines file extensions for different categories in the Downloads folder.

    2. `createDirectories(destination_directories, base_path)`

        - Creates directories in the specified `base_path` for the given list of `destination_directories` if they do not exist.

    3. `mapFileExtensions(base_path)`

        - Maps files in the Documents folder based on their file extensions.
        - Returns a dictionary (`files_mapping`) with file extensions as keys and lists of corresponding file names.

    4. `moveFiles(map, base_path)`

        - Moves files to their respective folders based on file extension using the provided mapping (`map`) and the `ext_dict`.

## B. `download_functions.py`

    1. `ext_dict`

        - A dictionary that defines file extensions for different categories, such as music, movies, pictures, documents, compressed files, executables, and programming files.

    2. `createDirectories(destination_list, base_path)`

        - Creates directories in the specified `base_path` for the given list of `destination_list` if they do not exist.

    3. `mapFileExtensions(source_path)`

        - Maps files in a folder (`source_path`) based on their file extensions.
        - Returns a dictionary (`files_mapping`) with file extensions as keys and lists of corresponding file names.

    4. `moveFiles(source_path, base_path, map)`

        - Moves files to their respective folders based on file extension using the provided mapping (`map`) and the `ext_dict`.

## C. `main.py`

    - The main function that executes the file cleanup process.
    - Prompts the user to choose between cleaning up the Downloads or Documents folder.
    - Validates user input and performs the cleanup accordingly using functions from `download_functions` and `documents_functions`.

## D. Usage

To use the script:

    1. Run `main.py`.
    2. Enter `1` to cleanup the Downloads folder or `2` to cleanup the Documents folder.
    3. The script will create directories and move files based on their types.

## E. Notes

    - Hidden files (those starting with a dot) are ignored during file mapping.
    - Directories are created only if they do not already exist.

Feel free to modify the script or its documentation based on your specific requirements or coding conventions.

<center> 🌈 **Happy Coding!** 🌟 </center>
