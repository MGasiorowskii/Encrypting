import utilities
from utilities import buffer
from encrypter import Encrypter
from decrypter import Decrypter
from fileSaver import FileSaver
from fileReader import FileReader


class Manager:
    """Representing a menu which is used to chose and execute other functions"""

    def __init__(self) -> None:
        self.__is_running = True
        self.choices = {
            1: self.encrypt_sentence,
            2: self.decrypt_sentence,
            3: self.print_results,
            4: self.save_buffer_to_file,
            5: self.decrypt_data_from_file,
            6: self.quit
        }
        self.initialize()

    def initialize(self) -> None:
        """Initialize loop"""
        while self.__is_running:
            self.show_menu()
            self.get_and_execute_choice()

    def show_menu(self) -> None:
        """Print menu of potential options"""

        menu = """
    1. Encrypt the sentence
    2. Decrypt the sentence
    3. Show results of operations
    4. Save results to file
    5. Decrypt data from json file
    6. Exit
        """
        print(menu)

    def get_and_execute_choice(self) -> None:
        """Get from user information which operation he is interested and execute it

        In case of choice the value out of scope show message
        """
        user_choice = int(input("Choose what you want do: "))
        self.choices.get(user_choice, self.show_error)()

    def show_error(self) -> None:
        """Show error message"""
        print("Incorrect choice - Try again")

    def quit(self) -> None:
        """Exit from loop.

        If buffer isn't empty ask user about saving data before quit
        """
        if not utilities.if_buffer_empty():
            choice = input("You have not saved date in buffer do you want save it? (Y/n): ")
            if choice.lower() == 'y':
                return

        print("\nHave a nice day!")
        self.__is_running = False

    def encrypt_sentence(self) -> None:
        """Initialize encrypting and save result to buffer"""
        operation_name = "Encrypting"
        original_sentence = utilities.get_string(operation_name)
        shift = utilities.get_shift(operation_name)
        encrypted_sentence = Encrypter.encrypting(original_sentence, shift)
        print(f"Encrypted sentence: {encrypted_sentence}")

        result = utilities.create_result_structure(operation_name, shift, original_sentence, encrypted_sentence)
        buffer.append(result)
        utilities.buffer_cleaning()

    def decrypt_sentence(self) -> None:
        """Initialize decrypting and save result to buffer"""
        operation_name = "Decrypting"
        original_sentence = utilities.get_string(operation_name)
        shift = utilities.get_shift(operation_name)
        decrypted_sentence = Decrypter.decrypting(original_sentence, shift)

        print(f"Decrypted sentence: {decrypted_sentence}")

        result = utilities.create_result_structure(operation_name, shift, original_sentence, decrypted_sentence)
        buffer.append(result)
        utilities.buffer_cleaning()

    def print_results(self) -> None:
        """Print the results of all operations"""
        if utilities.if_buffer_empty():
            return

        print("Results of operations:\n")

        for result in buffer:
            for key, value in result.items():
                print(f"{key}: {value}")

            print()

    def save_buffer_to_file(self) -> None:
        """Initialize saving the results of operations from buffer"""
        if utilities.if_buffer_empty():
            return

        file_name = FileSaver.create_file_name()
        content = FileSaver.create_content()
        FileSaver.save_to_file(file_name, content)
        FileSaver.show_message(file_name)
        utilities.buffer_cleaning()

    def decrypt_data_from_file(self) -> None:
        """Initialize reading data from json file and save the result to buffer"""
        operation_name = "Decrypting from file"
        file_name = FileReader.get_file_name()
        content_from_file = FileReader.read_file(file_name)
        if content_from_file == -1:
            return

        shift, encrypted_sentence = content_from_file.values()
        if utilities.if_shift_negative():
            return

        decrypted_sentence = Decrypter.decrypting(encrypted_sentence, shift)
        print(f"Decrypted sentence from file: {decrypted_sentence}")

        result = utilities.create_result_structure(operation_name, shift, encrypted_sentence, decrypted_sentence)
        buffer.append(result)
        utilities.buffer_cleaning()
