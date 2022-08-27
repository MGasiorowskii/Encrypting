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
    def create_content() -> dict:
        """Create and return the content to save"""
        content = {"Results": []}

        if not utilities.if_buffer_empty():
            if FileSaver.if_save_all_information():
                content["Results"] = buffer

            else:
                crypto_txt = []
                for result in buffer:
                    crypto_txt.append(result["New_sentence"])

                content["Results"] = crypto_txt

        return content

    @staticmethod
    def save_to_file(file_name: str, content: dict) -> None:
        """Save content to file in json format and ask user about cleaning buffer"""
        with open(file_name, "w", encoding="utf-8") as outfile:
            json.dump(content, outfile)

    @staticmethod
    def show_message(file_name: str) -> None:
        """Print the message after saving to file"""
        print(f"Datas has been saved to file {file_name}")

    @staticmethod
    def if_save_all_information() -> bool:
        """Ask user to save all information or only encrypted/decrypted sentence"""
        user_choice = input("Do you want save all information? (Y/n): ")
        if user_choice.lower() == 'y':
            return True
        return False
