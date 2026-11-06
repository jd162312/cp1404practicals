from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)
    add_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")


def save_guitars(guitars):
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=out_file)


main()
