# FileClass file
# Represents a file along with its properties and provides methods to interact with them.
class FileClass():
    def __init__(self, sizes, file_type, file_path, destinations=['Large', 'Medium', 'Small', 'Extra Small']):
        # Constructor to initialize the file properties.
        self.sizes = sizes
        self.file_type = file_type
        self.file_path = file_path
        self.destinations = destinations

    # Setters and getters for file sizes
    def setSizes(self, large, medium, small):
        self.sizes = [large, medium, small]

    def getSizes(self):
        return self.sizes

    # Setters and getters for file type
    def setFileType(self, type):
        self.file_type = type

    def getFileType(self):
        return self.file_type

    # Setters and getters for file path
    def setFilePath(self, path):
        self.file_path = path

    def getFilePath(self):
        return self.file_path

    # Setters and getters for destination directories
    def setDestinations(self, list):
        self.destinations = list

    def getDestinations(self):
        return self.destinations

    # Display file information
    def displayFileInfo(self):
        print(f"File Sizes:\t{self.sizes}\nFile Type:\t{self.file_type}\nFile Path:\t{self.file_path}")
        print(f"Destination Directories:\t{self.destinations}")