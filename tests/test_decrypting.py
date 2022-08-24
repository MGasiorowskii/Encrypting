import pytest
from decrypter import Decrypter
import string


@pytest.mark.parametrize("shift", [1])
@pytest.mark.parametrize("original_sentence", ["abcdefg"])
def test_should_pass_for_single_word(shift, original_sentence):
    expected = "ZABCDEF"
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [2])
@pytest.mark.parametrize("original_sentence", ["abcd efgh ijklmn"])
def test_should_pass_for_long_sentence(shift, original_sentence):
    expected = "YZAB CDEF GHIJKL"
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", ["xyz"])
def test_should_pass_for_letters_from_end_of_alphabet(shift, original_sentence):
    expected = "TUV"
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", ["123"])
def test_should_pass_for_numbers(shift, original_sentence):
    expected = "123"
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", [string.punctuation])
def test_should_pass_for_punctuation_marks(shift, original_sentence):
    expected = string.punctuation
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [4])
@pytest.mark.parametrize("original_sentence", [string.whitespace])
def test_should_pass_for_whitespaces(shift, original_sentence):
    expected = string.whitespace
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected == result


@pytest.mark.parametrize("shift", [-3])
@pytest.mark.parametrize("original_sentence", ["xyz"])
def test_should_failed_for_negative_shift(shift, original_sentence):
    expected = "ABC"
    result = Decrypter.decrypting(original_sentence, shift)

    assert expected != result
