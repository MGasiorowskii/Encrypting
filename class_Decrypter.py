FIRST_LETTER = 65
OFFSET = 26


class Decrypter:
    """Represents a class used to decrypt a file using the Caesar cipher"""
    def __init__(self) -> None:
        self.translated_sentence = self.get_string_to_decrypt().upper()
        self.key = self.get_key()
        self.original_sentence = self.decrypting_text()
        print(self.original_sentence)

    def get_string_to_decrypt(self) -> str:
        """Get form user string to decrypting"""
        return input("Input sentence to decrypting: ")

    def get_key(self) -> int:
        """Get from user key to decrypting"""
        return int(input("Input key to decrypting: "))

    def decrypting_text(self) -> str:
        decrypted_txt = ""

        for letter in self.translated_sentence:
            if ord(letter) - self.key >= FIRST_LETTER:
                decrypted_txt += chr(ord(letter) - self.key)
            else:
                decrypted_txt += chr(ord(letter) - self.key + OFFSET)

        return decrypted_txt

    def get_last_result(self) -> dict[str, str or int]:
        """Return result of last operation"""
        last_result = {
            "Operation": "Encrypting",
            "Key": self.key,
            "Original_txt": self.original_sentence,
            "Encrypted_txt": self.decrypted_sentence
        }

        return last_result
