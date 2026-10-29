"""
Word Occurrences
Estimate: 20 min
Actual: 30 min
"""


def main():
    """Get email from user to determine name."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_status = input(f"Is your name {name}? (Y/n) ")
        if name_status != "" and name_status.upper() != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email."""
    email_name = email.split("@")[0]
    parts = email_name.split(".")
    actual_name = " ".join(parts).title()
    return actual_name


main()
