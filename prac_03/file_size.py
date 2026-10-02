filename = input("Enter filename: ")
while filename != "":
    with open(filename, "r") as in_file:
        total = 0
        for lines in in_file:
            total += 1

    print(f"{filename} has {total} lines")
    filename = input("Enter filename: ")
