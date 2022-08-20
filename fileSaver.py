import time

#TODO refactor FilesServer na metody statyczne, zeby nie tworzyc obiektu FileSaver, Zamiast normalnemgo pliku JSON*,
class FileSaver:
    """Represents a class used to save results to file"""
    def __init__(self, results: list) -> None:
        self.results = results
        self.time = time.strftime("%H-%M_%d-%m-%Y", time.localtime())
        self.file_name = self.create_file_name()
        self.content = self.create_content()
        self.save_to_file()
        self.show_message()

    def create_file_name(self) -> str:
        """Create and return file name"""
        return f"Results_{self.time}.txt"

    def create_content(self) -> str:
        """Create and return the content to save"""
        content = ""

        if not self.results:
            return "No data in memory"

        for result in self.results:
            for key, value in zip(result.keys(), result.values()):
                content += f"{key}: {value}    "

            content += "\n"

        return content

    def save_to_file(self) -> None:
        """Save content to file"""
        choice = input("Czy chcesz zachować buffer? (Y/n)")
        with open(self.file_name, "w", encoding="utf-8") as file:
            file.writelines(self.content)
        #TODO obsluga usuwania buffera gdy uzytkownik poprosi
        if choice.lower() == 'y':
            pass

    def show_message(self) -> None:
        """Print the message after saving to file"""
        print(f"Datas has been saved to file {self.file_name}")
