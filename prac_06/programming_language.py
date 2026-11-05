"""
Estimate: 20 min
Actual: 22 min
"""


class ProgrammingLanguage:
    """Represent programming language object"""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise programing language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return programing language object as string"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed"""
        return self.typing == "Dynamic"
