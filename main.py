class Manager:
    """Representing a menu which is used to chose and execute other functions"""

    def __init__(self) -> None:
        self.choices = {
            5: quit()
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
        self.choices.get(user_choice, "Incorrect Value - Try again")

        self.initialize()


def main():
    Manager()


if __name__ == "__main__":
    main()
