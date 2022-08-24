import json
import pytest
import manager
import utilities

from manager import Manager


class TestingManager(Manager):
    def __init__(self):
        self.__is_running = True
        self.choices = {
            1: self.encrypt_sentence,
            2: self.decrypt_sentence,
            3: self.print_results,
            4: self.save_buffer_to_file,
            5: self.decrypt_data_from_file,
            6: self.quit
        }


@pytest.fixture
def testing_manager():
    return TestingManager()


@pytest.mark.show_menu
def test_function_should_print_menu_after_calling(capfd, testing_manager):
    expected = """
    1. Encrypt the sentence
    2. Decrypt the sentence
    3. Show results of operations
    4. Save results to file
    5. Decrypt data from json file
    6. Exit
        \n"""
    mngr = testing_manager
    mngr.show_menu()

    result, err = capfd.readouterr()

    assert expected == result


@pytest.mark.get_and_execute_choice
@pytest.mark.parametrize("user_choice", [0])
def test_should_pass_for_value_from_out_of_scope(capfd, monkeypatch, user_choice, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    expected = "Incorrect choice - Try again\n"
    mngr = testing_manager
    mngr.get_and_execute_choice()

    result, err = capfd.readouterr()

    assert expected == result



@pytest.mark.quit
@pytest.mark.parametrize("user_choice", ["N"])
def test_should_pass_for_big_letter_no(capfd, monkeypatch, user_choice, testing_manager):

    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    expected = "No data in memory\n\nHave a nice day!\n"
    mngr = testing_manager
    mngr.quit()

    result, err = capfd.readouterr()

    assert expected == result


@pytest.mark.quit
@pytest.mark.parametrize("user_choice", ["n"])
def test_should_pass_for_small_letter_no(capfd, monkeypatch, user_choice, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    expected = "No data in memory\n\nHave a nice day!\n"
    mngr = testing_manager
    mngr.quit()

    result, err = capfd.readouterr()

    assert expected == result


@pytest.mark.quit
@pytest.mark.parametrize("user_choice", ["Y"])
def test_should_pass_for_big_letter_yes(mocker, monkeypatch, user_choice, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    mngr = testing_manager
    mngr.quit()


@pytest.mark.quit
@pytest.mark.parametrize("user_choice", ["y"])
def test_should_pass_for_small_letter_yes(mocker, monkeypatch, user_choice, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "CDEF",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)

    mngr = testing_manager
    mngr.quit()


@pytest.mark.encrypt_sentence
@pytest.mark.parametrize("user_choice", ["n"])
@pytest.mark.parametrize("original_sentence", ["abcd"])
@pytest.mark.parametrize("shift", [2])
def test_should_pass_if_buffer_has_data(capfd, mocker, monkeypatch, user_choice, original_sentence, shift, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    def mock_get_shift(operation_name: str):
        return shift

    def mock_get_string(operation_name: str):
        return original_sentence

    mocker.patch('utilities.get_shift', mock_get_shift)
    mocker.patch('utilities.get_string', mock_get_string)

    expected = [{
        "Operation": "Encrypting",
        "Shift": 2,
        "Original_sentence": "abcd",
        "New_sentence": "CDEF"
    }]

    mngr = testing_manager
    mngr.encrypt_sentence()
    message, err = capfd.readouterr()

    result = utilities.buffer

    assert expected == result
    assert message == "Encrypted sentence: CDEF\n"


@pytest.mark.encrypt_sentence
@pytest.mark.parametrize("user_choice", ["y"])
@pytest.mark.parametrize("original_sentence", ["abcd"])
@pytest.mark.parametrize("shift", [2])
def test_should_pass_if_buffer_is_empty(capfd, mocker, monkeypatch, user_choice, original_sentence, shift, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    def mock_get_shift(operation_name: str):
        return shift

    def mock_get_string(operation_name: str):
        return original_sentence

    mocker.patch('utilities.get_shift', mock_get_shift)
    mocker.patch('utilities.get_string', mock_get_string)

    expected = []

    mngr = testing_manager
    mngr.encrypt_sentence()
    message, err = capfd.readouterr()

    result = utilities.buffer

    assert expected == result
    assert message == "Encrypted sentence: CDEF\n"


@pytest.mark.decrypt_sentence
@pytest.mark.parametrize("user_choice", ["n"])
@pytest.mark.parametrize("original_sentence", ["cdef"])
@pytest.mark.parametrize("shift", [2])
def test_should_pass_if_buffer_has_data(capfd, mocker, monkeypatch, user_choice, original_sentence, shift, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    def mock_get_shift(operation_name: str):
        return shift

    def mock_get_string(operation_name: str):
        return original_sentence

    mocker.patch('utilities.get_shift', mock_get_shift)
    mocker.patch('utilities.get_string', mock_get_string)

    expected = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "cdef",
        "New_sentence": "ABCD"
    }]

    mngr = testing_manager
    mngr.decrypt_sentence()
    message, err = capfd.readouterr()

    result = utilities.buffer

    assert expected == result
    assert message == "Decrypted sentence: ABCD\n"


@pytest.mark.decrypt_sentence
@pytest.mark.parametrize("user_choice", ["y"])
@pytest.mark.parametrize("original_sentence", ["cdef"])
@pytest.mark.parametrize("shift", [2])
def test_should_pass_if_buffer_is_empty(capfd, mocker, monkeypatch, user_choice, original_sentence, shift, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    def mock_get_shift(operation_name: str):
        return shift

    def mock_get_string(operation_name: str):
        return original_sentence

    mocker.patch('utilities.get_shift', mock_get_shift)
    mocker.patch('utilities.get_string', mock_get_string)

    expected = []

    mngr = testing_manager
    mngr.decrypt_sentence()
    message, err = capfd.readouterr()

    result = utilities.buffer

    assert expected == result
    assert message == "Decrypted sentence: ABCD\n"



@pytest.mark.print_results
def test_should_print_the_content_of_buffer(capfd, mocker, testing_manager):

    buffer = [{
        "Operation": "Decrypting",
        "Shift": 2,
        "Original_sentence": "cdef",
        "New_sentence": "ABCD"
    }]
    mocker.patch.object(utilities, 'buffer', buffer)
    mocker.patch.object(manager, 'buffer', buffer)

    mngr = testing_manager
    mngr.print_results()
    result, err = capfd.readouterr()

    expected = "Results of operations:\n\nOperation: Decrypting\nShift: 2\nOriginal_sentence: cdef\nNew_sentence: " \
               "ABCD\n\n"

    assert expected == result


@pytest.mark.print_results
def test_should_pass_if_buffer_is_empty(capfd, mocker, testing_manager):

    buffer = []
    mocker.patch.object(utilities, 'buffer', buffer)

    mngr = testing_manager
    mngr.print_results()
    result, err = capfd.readouterr()

    expected = "No data in memory\n"

    assert expected == result


@pytest.mark.save_buffer_to_file
def test_should_pass_if_buffer_is_empty(capfd, mocker, testing_manager):

    buffer = []
    mocker.patch.object(utilities, 'buffer', buffer)

    mngr = testing_manager
    mngr.save_buffer_to_file()
    result, err = capfd.readouterr()

    expected = "No data in memory\n"

    assert expected == result


@pytest.mark.save_buffer_to_files
@pytest.mark.parametrize("user_choice", ["n"])
def test_should_save_the_content_to_file(capfd, mocker, monkeypatch, testing_manager, user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    def mock_get_create_file_name():
        return "example_test.json"

    def mock_create_content():
        return {"Results": ["example"]}

    def mock_if_buffer_empty():
        return False

    mocker.patch('fileSaver.FileSaver.create_file_name', mock_get_create_file_name)
    mocker.patch('fileSaver.FileSaver.create_content', mock_create_content)
    mocker.patch('utilities.if_buffer_empty', mock_if_buffer_empty)

    mngr = testing_manager
    mngr.save_buffer_to_file()
    message, err = capfd.readouterr()

    with open("example_test.json", "r", encoding="utf-8") as outfile:
        result = json.load(outfile)

    expected = {"Results": ["example"]}

    assert expected == result
    assert message == "Datas has been saved to file example_test.json\n"


@pytest.mark.decrypt_data_from_file
@pytest.mark.parametrize("user_choice", ["n"])
def test_should_pass_if_decrypted_datas_from_file_are_in_buffer(capfd, mocker, monkeypatch, user_choice, testing_manager):
    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    def mock_get_file_name():
        return "text_test.json"

    mocker.patch('fileReader.FileReader.get_file_name', mock_get_file_name)

    expected = {
        "Operation": "Decrypting from file",
        "Shift": 2,
        "Original_sentence": "efgh",
        "New_sentence": "CDEF"
    }

    mngr = testing_manager
    mngr.decrypt_data_from_file()
    message, err = capfd.readouterr()

    result = utilities.buffer[-1]

    assert expected == result
    assert message == "Decrypted sentence from file: CDEF\n"

