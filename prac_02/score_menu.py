"""Score menu program."""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Get the user's score and display menu to choose an option."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def determine_score_status(score):
    """Determine the status of the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    """Get a valid score from the user between 0 and 100 (inclusive)."""
    score = int(input("Enter score: "))
    while determine_score_status(score) == "Invalid score":
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_result(score):
    """Print the score and its status."""
    print(f"User score {score} is {determine_score_status(score)}")


def print_stars(score):
    """Print the same number of stars as the score."""
    print("*" * score)


main()
