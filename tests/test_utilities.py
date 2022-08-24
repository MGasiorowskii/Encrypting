import pytest
import utilities


@pytest.mark.get_string
@pytest.mark.parametrize("user_input", ["example"])
@pytest.mark.parametrize("operation_name", ["Encrypting"])
def test_should_return_input_string(monkeypatch, user_input, operation_name):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    result = utilities.get_string(operation_name)
    expected = user_input.upper()

    assert expected == result


@pytest.mark.get_shift
@pytest.mark.parametrize("user_input", [5])
@pytest.mark.parametrize("operation_name", ["Encrypting"])
def test_should_pass_for_positive_int_input(monkeypatch, user_input, operation_name):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    result = utilities.get_shift(operation_name)
    expected = user_input

    assert expected == result


@pytest.mark.get_shift
@pytest.mark.parametrize("user_input", [0])
@pytest.mark.parametrize("operation_name", ["Encrypting"])
def test_should_pass_for_zero_input(monkeypatch, user_input, operation_name):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    result = utilities.get_shift(operation_name)
    expected = user_input

    assert expected == result


# How test infinity loops?


@pytest.mark.create_result_structure
@pytest.mark.parametrize("operation_name", ["Encrypting"])
@pytest.mark.parametrize("shift", [2])
@pytest.mark.parametrize("original_sentence", ["ABCD"])
@pytest.mark.parametrize("new_sentence", ["CDEF"])
def test_should_return_dict_with_value(operation_name, shift, original_sentence, new_sentence):
    expected = {
        "Operation": "Encrypting",
        "Shift": 2,
        "Original_sentence": "ABCD",
        "New_sentence": "CDEF"
    }
    result = utilities.create_result_structure(operation_name, shift, original_sentence, new_sentence)

    assert expected == result


@pytest.mark.buffer_cleaning
@pytest.mark.parametrize("user_choice", ['Y'])
def test_should_pass_for_big_letter_yes(monkeypatch, mocker, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    utilities.buffer_cleaning()
    expected = []
    result = buffer

    assert expected == result


@pytest.mark.buffer_cleaning
@pytest.mark.parametrize("user_choice", ['y'])
def test_should_pass_for_small_letter_yes(monkeypatch, mocker, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    utilities.buffer_cleaning()
    expected = []
    result = buffer

    assert expected == result


@pytest.mark.buffer_cleaning
@pytest.mark.parametrize("user_choice", ['N'])
def test_should_pass_for_big_letter_no(monkeypatch, mocker, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    expected = buffer
    utilities.buffer_cleaning()
    result = buffer

    assert expected == result


@pytest.mark.buffer_cleaning
@pytest.mark.parametrize("user_choice", ['n'])
def test_should_pass_for_small_letter_no(monkeypatch, mocker, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    expected = buffer
    utilities.buffer_cleaning()
    result = buffer

    assert expected == result


@pytest.mark.if_buffer_empty
def test_should_return_true_for_empty_buffer(capfd, mocker):
    buffer = []
    mocker.patch.object(utilities, 'buffer', buffer)

    result = utilities.if_buffer_empty()
    message, err = capfd.readouterr()
    expected = True

    assert expected == result
    assert message == "No data in memory\n"


@pytest.mark.if_buffer_empty
def test_should_return_true_for_buffer_with_data(mocker):
    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    result = utilities.if_buffer_empty()
    expected = False

    assert expected == result


@pytest.mark.if_shift_negative
@pytest.mark.parametrize("shift", [5])
def test_should_return_false_for_positive_shift(shift):

    result = utilities.if_shift_negative(shift)
    expected = False

    assert expected == result


@pytest.mark.if_shift_negative
@pytest.mark.parametrize("shift", [0])
def test_should_return_false_for_shift_equal_zero(shift):

    result = utilities.if_shift_negative(shift)
    expected = False

    assert expected == result


@pytest.mark.if_shift_negative
@pytest.mark.parametrize("shift", [-1])
def test_should_return_true_for_negative_shift(capfd, shift):

    result = utilities.if_shift_negative(shift)
    expected = True

    message, err = capfd.readouterr()

    assert expected == result
    assert message == "Shift can't be negative - try again\n"
