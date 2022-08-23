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







