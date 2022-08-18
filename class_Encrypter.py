from typing import Union
LAST_LETTER = 90
OFFSET = 26


class Encrypter:
    """Represents a class used to encrypt a file using the Caesar cipher"""

    @staticmethod
    def get_string_to_encrypt() -> str:
        """Get form user string to encrypting"""
        return input("Input sentence to encrypting: ")

    @staticmethod
    def get_key() -> int:
        """Get from user key to encrypting"""
        return int(input("Input key to encrypting: "))

    @staticmethod
    def encrypting_text(original_sentence, key) -> str:
        encrypted_txt = ""

        for letter in original_sentence:
            if ord(letter) + key <= LAST_LETTER:
                encrypted_txt += chr(ord(letter) + key)
            else:
                encrypted_txt += chr(ord(letter) + key - OFFSET)

        return encrypted_txt

    @staticmethod
    def encrypt():
        original_sentence = Encrypter.get_string_to_encrypt().upper()
        key = Encrypter.get_key()
        encrypted_sentence = Encrypter.encrypting_text(original_sentence, key)
        result = Encrypter.get_last_result(key, original_sentence, encrypted_sentence)
        print(f"Encrypted sentence: {encrypted_sentence}")
        return result

    @staticmethod
    def get_last_result(key, original, encrypted) -> dict[str, Union[str, int]]:
        """Return result of last operation"""
        last_result = {
            "Operation": "Encrypting",
            "Key": key,
            "Original_txt": original,
            "Encrypted_txt": encrypted
        }

        return last_result
