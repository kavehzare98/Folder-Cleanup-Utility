## Folder Cleanup Script Documentation

### Overview:

The provided Python script is a folder cleanup utility that organizes files in the user's Downloads directory into predefined categories based on their file extensions. The script creates destination directories for various file types, such as Music, Movies, Pictures, Documents, Executables, Programming, and Other. Files are then moved from the Downloads directory to their corresponding categories.

### Dependencies:

- `os`: Provides a way to interact with the operating system, including file and directory manipulation.
- `collections`: Utilized to create a defaultdict to store files based on their extensions.
- `pprint`: Used for pretty-printing the files mapping dictionary.

### File Categories and Extensions:

- **Audio Files (`EXT_AUDIO`):** mp3, wav, wma, mid, midi
- **Video Files (`EXT_VIDEO`):** mp4, mpg, mpeg, avi, mov, flv, mkv, mwv, m4v, h264
- **Image Files (`EXT_IMGS`):** png, jpg, JPG, jpeg, gif, svg, bmp, psd, tiff, tif, HEIC
- **Document Files (`EXT_DOCS`):** txt, pdf, csv, xls, xlsx, ods, doc, docx, ppt, pptx
- **Compressed Files (`EXT_COMPR`):** zip, z, tar, pkg, deb
- **Installer Files (`EXT_INSTL`):** dmg, exe, iso
- **Programming Files (`EXT_PROG`):** py, cpp, h

### User-defined Base Path and Destination Directories:

- `BASE_PATH`: The user's base directory where the files are all located.
- `DEST_DIRS`: List of destination directories to organize files into.

### Directory Creation:

- The script creates destination directories if they do not already exist in the user's home directory.

### Files Mapping:

- Files in the Downloads directory are mapped to their respective file extensions using a defaultdict.

### Moving Files:

- Files are moved from the Downloads directory to their appropriate destination directories based on their file extensions.

### Example Usage:

1. Clone the repository and navigate to the script's directory.
2. Run the script using the Python interpreter: `python folder_cleanup.py`.

### Notes:

- The script ignores hidden files (those starting with a dot `.`) in the directory.
- File extensions are case-sensitive.

### Disclaimer:

- Make sure to review and understand the script before running it to avoid unintentional data loss. It's advisable to test the script on a small set of files or in a controlled environment first.
