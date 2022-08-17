from class_Encrypter import Encrypter
from class_Decrypter import Decrypter
from class_FileSaver import FileSaver


class Manager:
    """Representing a menu which is used to chose and execute other functions"""

    def __init__(self) -> None:
        self.results = []
        self.choices = {
            1: self.encrypt_txt,
            2: self.decrypt_txt,
            3: self.print_results,
            4: self.save_results,
            5: self.quit
        }
        self.initialize()

    def initialize(self) -> None:
        """Initialize loop"""
        self.show_menu()
        self.get_and_execute_choice()

    def show_menu(self) -> None:
        """Print menu of potential options"""

        menu = """
        1. Encrypt the sentence
        2. Decrypt the sentence
        3. Show results of operations
        4. Save results to file
        5. Exit
        """
        print(menu)

    def get_and_execute_choice(self) -> None:
        """Get from user information which operation he is interested and execute it

        In case of choice the value out of scope show message
        """
        user_choice = int(input("Choose what you want do: "))
        self.choices.get(user_choice, self.show_error)()

        self.initialize()

    def show_error(self) -> None:
        """Show error message"""
        print("Incorrect Value - Try again")

    def quit(self) -> None:
        """Exit from loop"""
        exit()

    def encrypt_txt(self) -> None:
        """Initialize class Encrypter and save result to list"""
        encrypter = Encrypter()
        self.results.append(encrypter.get_last_result())

    def decrypt_txt(self) -> None:
        """Initialize class Decrypter and save result to list"""
        decrypter = Decrypter()
        self.results.append(decrypter.get_last_result())

    def print_results(self) -> None:
        """Print the results of all operations"""
        if not self.results:
            print("No data in memory")
            return

        for result in self.results:
            for key, value in zip(result.keys(), result.values()):
                print(f"{key}: {value}")

            print()

    def save_results(self) -> None:
        """Initialize class FileSaver"""
        FileSaver(self.results)


def main():
    Manager()


if __name__ == "__main__":
    main()
