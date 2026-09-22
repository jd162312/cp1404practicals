MIN_LENGTH = 5
password = input("Enter password: ")
while len(password) < MIN_LENGTH:
    print("Invalid password")
    password = input("Enter password: ")
print("*" * len(password))
