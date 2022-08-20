LAST_LETTER = 90
OFFSET = 26


class Encrypter:
    """Represents a class used to encrypt a file using the Caesar cipher"""

    @staticmethod
    def encrypting_sentence(original_sentence: str, shift: int) -> str:
        """Return encrypted sentence with shift according to Cesar cipher"""
        encrypted_sentence = ""

        for letter in original_sentence:
            if ord(letter) + shift <= LAST_LETTER:
                encrypted_sentence += chr(ord(letter) + shift)
            else:
                encrypted_sentence += chr(ord(letter) + shift - OFFSET)

        return encrypted_sentence
