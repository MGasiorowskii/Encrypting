import json
from typing import Union


class FileReader:
    """Represents a class used to read encrypted sentence from file"""

    @staticmethod
    def get_file_name() -> str:
        """Get from user file name to decrypt"""
        return input("Input the file name: ")

    @staticmethod
    def show_error(file_name: str) -> None:
        """Print the error message if file doesn't exist"""
        print(f"File {file_name} doesn't exist - Try again")

    @staticmethod
    def read_file(file_name: str) -> Union[dict, int]:
        """Read data from json file and return content of file

        If file doesn't exist show error_message
        """
        try:
            with open(file_name) as file:
                content = json.load(file)

        except FileNotFoundError:
            FileReader.show_error(file_name)
            return -1

        return content
