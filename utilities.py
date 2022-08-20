from typing import Union


buffer = []


def get_string(operation_name: str) -> str:
    """Get from user string"""
    return input(f"Input sentence to {operation_name}: ")


def get_shift(operation_name: str) -> int:
    """Get from user value of shift"""
    return int(input(f"Input shift to {operation_name}: "))


def get_last_result(operation_name: str, shift: int, original_sentence: str, new_sentence: str)\
        -> dict[str, Union[str, int]]:
    """Return result of last operation"""
    last_result = {
        "Operation": operation_name,
        "Key": shift,
        "Original_sentence": original_sentence,
        "New_sentence": new_sentence
    }

    return last_result


def buffer_cleaning() -> None:
    """Ask user to execute buffer cleaning"""
    user_choice = input("Do you want clear the buffer? (Y/n): ")
    if user_choice.lower() == 'y':
        buffer.clear()


def if_buffer_empty() -> bool:
    """Return the status of buffer and print message"""
    if not buffer:
        print("No data in memory")
        return True
