from typing import Union


buffer = []


def get_string(operation_name: str) -> str:
    """Get from user string"""
    return input(f"Input sentence to {operation_name}: ").upper()


def get_shift(operation_name: str) -> int:
    """Get from user value of shift"""

    while True:
        shift = int(input(f"Input shift to {operation_name}: "))
        if not if_shift_negative(shift):
            return shift


def create_result_structure(operation_name: str, shift: int, original_sentence: str, new_sentence: str)\
        -> dict[str, Union[str, int]]:
    """Return structure with datas"""
    result = {
        "Operation": operation_name,
        "Shift": shift,
        "Original_sentence": original_sentence,
        "New_sentence": new_sentence
    }

    return result


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
    else:
        return False


def if_shift_negative(shift: int) -> bool:
    """Check if shift is negative and print message"""

    if shift < 0:
        print("Shift can't be negative - try again")
        return True
    else:
        return False
