COLOUR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "amber": "#ffbf00",
                  "aqua": "#00ffff", "black": "#000000", "blond": "#faf0be", "bone": "#e3dac9"}
colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
