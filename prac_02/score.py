"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Get the users score and display its status."""
    score = float(input("Enter score: "))
    print(determine_score_status(score))


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
