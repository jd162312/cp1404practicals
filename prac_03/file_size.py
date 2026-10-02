"""File size program."""


def main():
    """Get filename and print number of lines."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            with open(filename, "r") as in_file:
                total = determine_number_lines(in_file)
            print(f"{filename} has {total} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def determine_number_lines(in_file):
    """Determine the number of lines in the chosen file."""
    total = 0
    for lines in in_file:
        total += 1
    return total


main()
