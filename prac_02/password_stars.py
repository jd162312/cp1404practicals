"""Convert password into *'s"""

MIN_LENGTH = 5


def main():
    password = get_password()
    print_password(password)


def print_password(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password


main()
