import time


class FileReader:
    """Represents a class used to save results to file"""
    def __init__(self, results: list) -> None:
        self.results = results
        self.time = time.strftime("%H-%M_%d-%m-%Y", time.localtime())
        self.file_name = self.create_file_name()

    def create_file_name(self) -> str:
        """Create and return file name"""
        return f"Results_{self.time}"



