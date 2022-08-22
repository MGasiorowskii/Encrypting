FIRST_LETTER = 65
LAST_LETTER = 90
OFFSET = 26


class Decrypter:
    """Represents a class used to decrypt a file using the Caesar cipher"""

    @staticmethod
    def decrypting(original_sentence: str, shift: int) -> str:
        """Return decrypted sentence with shift according to Cesar cipher"""
        decrypted_sentence = ""

        for letter in original_sentence.upper():

            if FIRST_LETTER <= ord(letter) - shift <= LAST_LETTER:
                decrypted_sentence += chr(ord(letter) - shift)
            elif ord(letter) - shift + OFFSET <= LAST_LETTER:
                decrypted_sentence += chr(ord(letter) - shift + OFFSET)
            else:
                decrypted_sentence += letter

        return decrypted_sentence
