for i in range(1, 21, 2):
    print(i, end=' ')
print()

# part a

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# part b

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# part c

number_of_stars = int(input("How many stars? "))
for i in range(number_of_stars):
    print("*", end='')
print()

# part d

number_of_lines = int(input("Number of lines? "))
for i in range(number_of_lines):
    for j in range(i + 1):
        print("*", end='')
    print()
