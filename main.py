class Manager:
    def __init__(self):
        self.show_menu()
        self.get_choice_from_user()

    def show_menu(self):
        menu = """
        1. Encrypt word
        5. Exit
        """
        print(menu)

    def get_choice_from_user(self):
        return int(input("Choose what you want do: "))


def main():
    init = Manager()


if __name__ == "__main__":
    main()
