"""File size program."""


def main():
    """Get filename and print number of lines."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            total = determine_file_size(filename)
            print(f"{filename} has {total} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def determine_file_size(filename):
    """Determine the number of lines in the chosen file."""
    with open(filename, "r") as in_file:
        total = 0
        for lines in in_file:
            total += 1
    return total


main()
