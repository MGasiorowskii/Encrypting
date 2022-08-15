class Encrypter:
    """Represents a class used to encrypt a file using the Caesar cipher  mod47 or mod13"""
    def __init__(self) -> None:
        self.translated_sentence = ""
        self.sentence = self.get_string_to_encrypt().upper()

    def get_string_to_encrypt(self) -> str:
        """Get form user string to encrypting"""
        return input("Input sentence to encrypting: ")

