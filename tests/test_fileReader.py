import pytest

from fileReader import FileReader


@pytest.mark.get_file_name
@pytest.mark.parametrize("user_input", ["file_name"])
def test_should_return_input_string(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    result = FileReader.get_file_name()
    expected = user_input

    assert expected == result


@pytest.mark.get_file_name
@pytest.mark.parametrize("user_input", [5])
def test_should_return_input_int(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    result = FileReader.get_file_name()
    expected = user_input

    assert expected == result


@pytest.mark.show_error
@pytest.mark.parametrize("file_name", ["example"])
def test_should_return_string_for_string_value(capfd, file_name):
    FileReader.show_error(file_name)

    result, err = capfd.readouterr()
    expected = f"File {file_name} doesn't exist - Try again\n"

    assert expected == result


@pytest.mark.show_error
@pytest.mark.parametrize("file_name", [5])
def test_should_return_string_for_int_value(capfd, file_name):
    FileReader.show_error(file_name)

    result, err = capfd.readouterr()
    expected = f"File {file_name} doesn't exist - Try again\n"

    assert expected == result


@pytest.mark.read_file
@pytest.mark.parametrize("file_name", ["example.json"])
def test_should_return_exception_for_name_file_that_not_exist(file_name):

    result = FileReader.read_file(file_name)
    expected = -1

    assert expected == result


@pytest.mark.read_file
@pytest.mark.parametrize("file_name", ["example.json"])
def test_should_print_error_for_name_file_that_not_exist(capfd, file_name):

    FileReader.read_file(file_name)
    result, err = capfd.readouterr()
    expected = f"File {file_name} doesn't exist - Try again\n"

    assert expected == result


@pytest.mark.read_file
@pytest.mark.parametrize("file_name", ["test.json"])
def test_should_pass_for_name_file_that_exist(file_name):

    result = FileReader.read_file(file_name)
    expected = {"Result": [{"Operation": "Decrypting", "Shift": 2, "Original_sentence": "CDEF", "New_sentence": "ABCD"}]}

    assert expected == result
