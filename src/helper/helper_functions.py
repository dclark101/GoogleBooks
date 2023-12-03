# list of required characters for user password
special_char = "~!@#$%^&*()_+-=[]{\}|;':\",></?"
numbers = "0123456789"

# minimum character length for password
PASSWORD_LEN = 8


# maximum character length for the left side of @ symbol
MAX_LOCAL_PART = 64


# password formatter function
def password_format(passwd: str) -> bool:
    """
    function that takes in user password and checks if its in a proper format
    """

    is_valid = True

    if not any(char.isdigit() for char in passwd):
        print("minimum numbers required is 1!")
        is_valid = False

    if not any(char in special_char for char in passwd):
        print("minimum number of special characters is 1!")
        is_valid = False

    if len(passwd) < PASSWORD_LEN:
        print("minimum character length required is 8!")
        is_valid = False

    return is_valid


def email_format(email: str) -> bool:
    split_email = email.split("@")

    is_valid_email = True
    if "@" not in email:
        print("invalid email format: no @ symbol")

    if len(split_email[0]) > MAX_LOCAL_PART:
        print(f"left side of email exceeds character count of ${MAX_LOCAL_PART}")

    return is_valid_email
