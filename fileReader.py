class FileReader:
    """Represents a class used to read encrypted sentence from file"""

    @staticmethod
    def get_file_name() -> str:
        """Get from user file name to encrypt"""
        return input("Input the file name: ")

    @staticmethod
    def show_error(file_name: str) -> None:
        """Print the error message if file doesn't exist"""
        print(f"File {file_name} doesn't exist")




