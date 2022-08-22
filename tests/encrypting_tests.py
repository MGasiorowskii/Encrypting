import pytest
from encrypter import LAST_LETTER, OFFSET, Encrypter


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

