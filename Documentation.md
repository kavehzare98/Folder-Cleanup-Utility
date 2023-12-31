# File Cleanup Script Documentation

This documentation provides a detailed explanation of the file cleanup script, which is split across three Python files: `documents_functions.py`, `downloads_functions.py`, and `main.py`.

## A. `documents_functions.py`

&nbsp;&nbsp;&nbsp;&nbsp; 1. `ext_dict`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- A dictionary that defines file extensions for different categories in the Downloads folder.

&nbsp;&nbsp;&nbsp;&nbsp;2. `createDirectories(destination_directories, base_path)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Creates directories in the specified `base_path` for the given list of `destination_directories` if they do not exist.

&nbsp;&nbsp;&nbsp;&nbsp;3. `mapFileExtensions(base_path)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Maps files in the Documents folder based on their file extensions. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Returns a dictionary (`files_mapping`) with file extensions as keys and lists of corresponding file names.

&nbsp;&nbsp;&nbsp;&nbsp;4. `moveFiles(map, base_path)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Moves files to their respective folders based on file extension using the provided mapping (`map`) and the `ext_dict`.

## B. `download_functions.py`

&nbsp;&nbsp;&nbsp;&nbsp;1. `ext_dict`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- A dictionary that defines file extensions for different categories, such as music, movies, pictures, documents, compressed files, executables, and programming files.

&nbsp;&nbsp;&nbsp;&nbsp;2. `createDirectories(destination_list, base_path)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Creates directories in the specified `base_path` for the given list of `destination_list` if they do not exist.

&nbsp;&nbsp;&nbsp;&nbsp;3. `mapFileExtensions(source_path)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maps files in a folder (`source_path`) based on their file extensions. Returns a dictionary (`files_mapping`) with file extensions as keys and lists of corresponding file names.

&nbsp;&nbsp;&nbsp;&nbsp;4. `moveFiles(source_path, base_path, map)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Moves files to their respective folders based on file extension using the provided mapping (`map`) and the `ext_dict`.

## C. `main.py`

&nbsp;&nbsp;&nbsp;&nbsp;- The main function that executes the file cleanup process.
&nbsp;&nbsp;&nbsp;&nbsp;- Prompts the user to choose between cleaning up the Downloads or Documents folder.
&nbsp;&nbsp;&nbsp;&nbsp;- Validates user input and performs the cleanup accordingly using functions from `download_functions` and `documents_functions`.

## D. Usage

To use the script:

&nbsp;&nbsp;&nbsp;&nbsp;1. Run `main.py`.
&nbsp;&nbsp;&nbsp;&nbsp;2. Enter `1` to cleanup the Downloads folder or `2` to cleanup the Documents folder.
&nbsp;&nbsp;&nbsp;&nbsp;3. The script will create directories and move files based on their types.

## E. Notes

&nbsp;&nbsp;&nbsp;&nbsp;- Hidden files (those starting with a dot) are ignored during file mapping.
&nbsp;&nbsp;&nbsp;&nbsp;- Directories are created only if they do not already exist.

Feel free to modify the script or its documentation based on your specific requirements or coding conventions.

<center> 🌈 **Happy Coding!** 🌟 </center>
