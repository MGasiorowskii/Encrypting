FIRST_LETTER = 65
LAST_LETTER = 90
OFFSET = 26


class Encrypter:
    """Represents a class used to encrypt a file using the Caesar cipher"""

    @staticmethod
    def encrypting(original_sentence: str, shift: int) -> str:
        """Return encrypted sentence with shift according to Cesar cipher"""
        encrypted_sentence = ""

        for letter in original_sentence.upper():
            if letter.isalpha():
                if FIRST_LETTER <= ord(letter) + shift <= LAST_LETTER:
                    encrypted_sentence += chr(ord(letter) + shift)
                else :
                    encrypted_sentence += chr(ord(letter) + shift - OFFSET)
            else:
                encrypted_sentence += letter

        return encrypted_sentence
