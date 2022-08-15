class Manager:
    """Representing a menu which is used to chose and execute other functions"""

    def __init__(self) -> None:
        self.choices = {
            5: self.quit
        }
        self.initialize()

    def initialize(self):
        """Initialize loop"""
        self.show_menu()
        self.get_and_execute_choice()

    def show_menu(self) -> None:
        """Print menu of potential options"""

        menu = """
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


def main():
    Manager()


if __name__ == "__main__":
    main()
