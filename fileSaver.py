import time
import json
import utilities
from utilities import buffer


class FileSaver:
    """Represents a class used to save results to file"""

    @staticmethod
    def create_file_name() -> str:
        """Create and return file name in json format"""
        time_of_creating = time.strftime("%H-%M_%d-%m-%Y", time.localtime())
        return f"Results_{time_of_creating}.json"

    @staticmethod
    def create_content() -> str:
        """Create and return the content to save"""
        content = ""

        if not utilities.if_buffer_empty():
            for result in buffer:
                for key, value in zip(result.items()):
                    content += f"{key}: {value}    "

                content += "\n"

        return content

    @staticmethod
    def save_to_file(file_name: str, content: str) -> None:
        """Save content to file in json format and ask user about cleaning buffer"""
        with open(file_name, "w", encoding="utf-8") as outfile:
            json.dump(content, outfile)

        utilities.buffer_cleaning()

    @staticmethod
    def show_message(file_name: str) -> None:
        """Print the message after saving to file"""
        print(f"Datas has been saved to file {file_name}")
