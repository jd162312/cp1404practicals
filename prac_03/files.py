# 1
name = input("Enter name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    print(number1 + number2)

# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for lines in in_file:
        number = int(lines)
        total += number
    print(total)
