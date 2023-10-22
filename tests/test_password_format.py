import pytest
from src.authentication.helper_functions import password_format


def test_can_check_for_invalid_format():
    # assert either passes or fails a test case
    assert password_format("HelloWorld") == False


def test_can_check_for_valid_format():
    assert password_format("HelloWorld12$") == True
