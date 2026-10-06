"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        subjects.append(data)
        # print(data)  # See if that worked
        # print("----------")
    input_file.close()
    return subjects


def display_subjects(subjects):
    """Display subject data."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
