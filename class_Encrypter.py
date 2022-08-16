from typing import Union


LAST_LETTER = 90
OFFSET = 26


class Encrypter:
    """Represents a class used to encrypt a file using the Caesar cipher"""
    def __init__(self) -> None:
        self.last_result = {
            "Operation": None,
            "Key": None,
            "Original_txt": None,
            "Encrypted_txt": None
        }

        self.original_sentence = self.get_string_to_encrypt().upper()
        self.key = self.get_key()
        self.encrypted_sentence = self.encrypting_text()
        print(self.encrypted_sentence)

    def get_string_to_encrypt(self) -> str:
        """Get form user string to encrypting"""
        return input("Input sentence to encrypting: ")

    def get_key(self) -> int:
        """Get from user key to encrypting"""
        return int(input("Input key to encrypting: "))

    def encrypting_text(self) -> str:
        encrypted_txt = ""

        for letter in self.original_sentence:
            if ord(letter) + self.key <= LAST_LETTER:
                encrypted_txt += chr(ord(letter) + self.key)
            else:
                encrypted_txt += chr(ord(letter) + self.key - OFFSET)

        return encrypted_txt

    def get_last_result(self) -> dict[str, str or int]:
        """Return result of last operation"""
        self.last_result = {
            "Operation": "Encrypting",
            "Key": self.key,
            "Original_txt": self.original_sentence,
            "Encrypted_txt": self.encrypted_sentence
        }

        return self.last_result


