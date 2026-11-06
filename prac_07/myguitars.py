from prac_07.guitar import Guitar


def main():
    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)


def load_guitars():
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


main()
