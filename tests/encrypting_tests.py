import pytest
from encrypter import Encrypter
import string


@pytest.mark.parametrize("shift", [2])
@pytest.mark.parametrize("original_sentence", ["abcdefg"])
def test_should_pass_for_single_word(shift, original_sentence):
    expected = "CDEFGHI"
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [2])
@pytest.mark.parametrize("original_sentence", ["abcd efgh ijklmn"])
def test_should_pass_for_long_sentence(shift, original_sentence):
    expected = "CDEF GHIJ KLMNOP"
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", ["xyz"])
def test_should_pass_for_letters_from_end_of_alphabet(shift, original_sentence):
    expected = "BCD"
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", ["123"])
def test_should_pass_for_numbers(shift, original_sentence):
    expected = "123"
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", [string.punctuation])
def test_should_pass_for_punctuation_marks(shift, original_sentence):
    expected = string.punctuation
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", [string.whitespace])
def test_should_pass_for_whitespaces(shift, original_sentence):
    expected = string.whitespace
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [-3])
@pytest.mark.parametrize("original_sentence", ["cdef"])
def test_should_failed_for_negative_shift(shift, original_sentence):
    expected = "ZABC"
    result = Encrypter.encrypting(original_sentence, shift)

    assert expected != result

