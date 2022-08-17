import time


class FileSaver:
    """Represents a class used to save results to file"""
    def __init__(self, results: list) -> None:
        self.results = results
        self.time = time.strftime("%H-%M_%d-%m-%Y", time.localtime())
        self.file_name = self.create_file_name()
        self.content = self.create_content()
        self.save_to_file()

    def create_file_name(self) -> str:
        """Create and return file name"""
        return f"Results_{self.time}"

    def create_content(self) -> str:
        """Create and return the content to save"""
        content = ""

        if not self.results:
            return "No data in memory"

        for result in self.results:
            for key, value in zip(result.keys(), result.values()):
                content += f"{key}: {value}\t",

            content += "\n"

        return content

    def save_to_file(self):
        pass


