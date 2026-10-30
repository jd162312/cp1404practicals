"""
For total guitar exercises
Estimate: 30 min
Actual: 38 min
"""
import datetime


class Guitar:
    """Represent guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar object as string."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the guitar,"""
        return datetime.datetime.now().year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage based on age."""
        return self.get_age() >= 50
