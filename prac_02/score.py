"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def main():
    """Get the users score and display its status."""
    score = float(input("Enter score: "))
    print(f"User score {score} is {determine_score_status(score)}")
    if determine_score_status(score) == "Excellent":
        print("You get a prize!")
    random_score = randint(0, 100)
    print(f"Random: {random_score} = {determine_score_status(random_score)}")


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


main()
