import pytest
import time
import json

import fileSaver
from fileSaver import FileSaver


@pytest.mark.create_file_name
def test_should_return_name_with_actual_time():
    time_of_creating = time.strftime("%H-%M_%d-%m-%Y", time.localtime())

    expected = f"Results_{time_of_creating}.json"
    result = FileSaver.create_file_name()

    assert expected == result


@pytest.mark.create_content
def test_should_pass_for_empty_buffer(mocker):
    buffer = []
    mocker.patch.object(fileSaver, 'buffer', buffer)

    expected = {"Results": []}
    result = FileSaver.create_content()

    assert expected == result


@pytest.mark.create_content
def test_should_pass_for_buffer_with_data_and_all_information(mocker):
    def mock_if_save_all_information():
        return True

    def mock_if_buffer_empty():
        return False

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(fileSaver, 'buffer', buffer)
    mocker.patch("utilities.if_buffer_empty", mock_if_buffer_empty)
    mocker.patch("fileSaver.FileSaver.if_save_all_information", mock_if_save_all_information)

    expected = {"Results": [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]}
    result = FileSaver.create_content()

    assert expected == result


@pytest.mark.create_content
def test_should_pass_for_buffer_with_data_and_limited_information(mocker):
    def mock_if_save_all_information():
        return False

    def mock_if_buffer_empty():
        return False

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(fileSaver, 'buffer', buffer)
    mocker.patch("utilities.if_buffer_empty", mock_if_buffer_empty)
    mocker.patch("fileSaver.FileSaver.if_save_all_information", mock_if_save_all_information)

    expected = {"Results": ["ABCD"]}
    result = FileSaver.create_content()

    assert expected == result


@pytest.mark.save_to_file
def test_should_pass_for_normal_input():
    content = {"Result": [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]}
    file_name = "test.json"

    FileSaver.save_to_file(file_name, content)
    with open(file_name, "r", encoding="utf-8") as outfile:
        result = json.load(outfile)
    expected = content

    assert expected == result


@pytest.mark.show_message
@pytest.mark.parametrize("file_name", ["example"])
def test_should_pass_for_string_value(capfd, file_name):
    FileSaver.show_message(file_name)

    result, err = capfd.readouterr()
    expected = f"Datas has been saved to file {file_name}\n"

    assert expected == result


@pytest.mark.show_message
@pytest.mark.parametrize("file_name", [5])
def test_should_pass_for_int_value(capfd, file_name):
    FileSaver.show_message(file_name)

    result, err = capfd.readouterr()
    expected = f"Datas has been saved to file {file_name}\n"

    assert expected == result


@pytest.mark.show_message
@pytest.mark.parametrize("file_name", [4.13])
def test_should_pass_for_float_value(capfd, file_name):
    FileSaver.show_message(file_name)

    result, err = capfd.readouterr()
    expected = f"Datas has been saved to file {file_name}\n"

    assert expected == result


@pytest.mark.show_message
@pytest.mark.parametrize("file_name", [True])
def test_should_pass_for_bool_value(capfd, file_name):
    FileSaver.show_message(file_name)

    result, err = capfd.readouterr()
    expected = f"Datas has been saved to file {file_name}\n"

    assert expected == result


@pytest.mark.if_save_all_information
@pytest.mark.parametrize("user_choice", ['y'])
def test_should_return_True_for_small_letter_yes(monkeypatch, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    result = FileSaver.if_save_all_information()
    expected = True

    assert expected == result


@pytest.mark.if_save_all_information
@pytest.mark.parametrize("user_choice", ['Y'])
def test_should_return_True_for_big_letter_yes(monkeypatch, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    result = FileSaver.if_save_all_information()
    expected = True

    assert expected == result


@pytest.mark.if_save_all_information
@pytest.mark.parametrize("user_choice", ['n'])
def test_should_return_False_for_small_letter_no(monkeypatch, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    result = FileSaver.if_save_all_information()
    expected = False

    assert expected == result


@pytest.mark.if_save_all_information
@pytest.mark.parametrize("user_choice", ['N'])
def test_should_return_False_for_big_letter_no(monkeypatch, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    result = FileSaver.if_save_all_information()
    expected = False

    assert expected == result
