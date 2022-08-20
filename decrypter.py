FIRST_LETTER = 65
OFFSET = 26


class Decrypter:
    """Represents a class used to decrypt a file using the Caesar cipher"""

    @staticmethod
    def decrypting(original_sentence: str, shift: int) -> str:
        """Return decrypted sentence with shift according to Cesar cipher"""
        decrypted_sentence = ""

        for letter in original_sentence.upper():
            if ord(letter) - shift >= FIRST_LETTER:
                decrypted_sentence += chr(ord(letter) - shift)
            else:
                decrypted_sentence += chr(ord(letter) - shift + OFFSET)

        return decrypted_sentence
