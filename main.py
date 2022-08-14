class Manager:
    def __init__(self) -> None:
        self.show_menu()
        self.get_and_execute_choice()

    def show_menu(self) -> None:
        """ Function print menu of potential options"""

        menu = """
        5. Exit
        """
        print(menu)

    def get_and_execute_choice(self) -> None:
        """Function get from user information which operation he is interested and execute it

        In case of choice the value out of scope show message

        Work in loop until user chose option exit()
        """
        user_choice = int(input("Choose what you want do: "))
        choices = {
            5: exit()
        }
        if user_choice in choices:
            choices.get(user_choice)
        else:
            print("Inccorect Value - Try again")

        self.start()


def main():
    Manager()


if __name__ == "__main__":
    main()
