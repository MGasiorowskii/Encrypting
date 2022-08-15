LAST_LETTER = 90
OFFSET = 26


class Encrypter:
    """Represents a class used to encrypt a file using the Caesar cipher  mod47 or mod13"""
    def __init__(self) -> None:
        self.sentence = self.get_string_to_encrypt().upper()
        self.key = self.get_key()
        self.translated_sentence = self.encytping_text()
        print(self.translated_sentence)

    def get_string_to_encrypt(self) -> str:
        """Get form user string to encrypting"""
        return input("Input sentence to encrypting: ")

    def get_key(self) -> int:
        """Get from user key to encrypting"""
        return int(input("Input key to encrypting: "))

    def encytping_text(self) -> str:
        encrypted_txt = ""

        for letter in self.sentence:
            if ord(letter) + self.key <= LAST_LETTER:
                encrypted_txt += chr(ord(letter) + self.key)
            else:
                encrypted_txt += chr(ord(letter) + self.key - OFFSET)

        return encrypted_txt
