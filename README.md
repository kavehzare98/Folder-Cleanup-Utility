# Folder Cleanup Utility

## A. Problem statement

1. **Disorganization:** Over time, files in a folder can become disorganized, making it difficult for users to locate specific files quickly. This software helps maintain a tidy folder structure by categorizing files according to their types.

2. **Time-consuming manual organization:** Manually sorting files into different folders based on their types can be a time-consuming task, especially when dealing with a large number of files. The software automates this process, saving users time and effort.

## B. Solution

This program organizes files in specified folders based on their file extensions. It includes two main modules: `downloads_functions` for cleaning up the Downloads folder and `documents_functions` for cleaning up the Documents folder. The cleanup is categorized into different folders based on file types.

## C. Benefits

1. **Efficiency:** With organized folders, users can locate and access files more efficiently. This is particularly useful for individuals who work with a variety of file types and need a streamlined system for managing their data.

2. **Consistency:** The software ensures consistency in file organization, preventing the accumulation of unsorted files and maintaining a clean and structured file system.

3. **Reduced clutter:** A cluttered desktop or folder structure can lead to a less productive and more chaotic digital workspace. The software helps reduce clutter by systematically arranging files in their appropriate locations.

4. **File type recognition:** The software identifies file types based on their extensions and directs them to designated folders, promoting a systematic approach to file management.

In summary, the software streamlines the process of organizing files, saving users time, improving efficiency, and contributing to a more organized and productive digital workspace.

## D. Features

- **Automated Sorting**: The scripts automatically analyze files within a specified directory and categorize them based on their file extensions.
- **Customizable Rules**: Tailor the cleanup process to your specific needs by configuring rules for file types and destination directories.
- **Efficient Organization**: Keep your folders tidy by moving files to their designated locations, reducing clutter and making it easier to locate and manage your files.
- **Extensible**: The modular design allows for easy expansion and customization. Feel free to add new rules or modify existing ones to suit your evolving organizational requirements.

## E. Getting Started

### Usage

1. Run `main.py`.
2. Enter `1` to cleanup the Downloads folder or `2` to cleanup the Documents folder.
3. The script will create directories and move files based on their types.

### Modules

#### `downloads_functions.py`

- Defines file extensions for different categories in the Downloads folder.
- Provides functions to create directories, map files based on extensions, and move files to respective folders.

#### `documents_functions.py`

- Defines file extensions for different document categories.
- Provides functions to create directories, map files based on extensions, and move files to respective folders.

#### `main.py`

- The main script that prompts the user to choose between cleaning up the Downloads or Documents folder.
- Executes the cleanup process using functions from `downloads_functions` or `documents_functions`.

### Notes

- Hidden files (those starting with a dot) are ignored during file mapping (e.g. ".localized").
- Directories are created only if they do not already exist.

### Requirements

- Python 3.x

Feel free to customize the script or its modules based on your specific needs or coding conventions.

## H. Sources

1. [Curious Coding YouTube Video](https://www.youtube.com/watch?v=5idxowRxWW0)
2. [OS Documentation](https://docs.python.org/3/library/os.path.html#module-os.path)
3. [Collections Documentation](https://docs.python.org/3/library/collections.html)

## I. Contributing

Contributions are welcome! Whether you want to improve existing functionality, add new features, or fix bugs, please feel free to submit a pull request.

## J. License

This project is licensed under the [MIT License](notion://www.notion.so/LICENSE), making it open and accessible for personal and commercial use.

Simplify your digital life—let the Folder Cleanup Utility handle the organization, so you can focus on what matters most. Download and run the scripts today!

##
