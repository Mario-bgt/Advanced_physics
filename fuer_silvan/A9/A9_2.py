# The signatures of this class and its task methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce grading/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_title(self):
        return self.__title

    def get_authors(self):
        return self.__authors

    def get_year(self):
        return self.__year

    def __str__(self):
        return f"Publication({self.__authors}, {self.__title}, {self.__year})"

    def __repr__(self):
        return f"Publication({self.__authors}, {self.__title}, {self.__year})"

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.
    # We've provided a starting point for one of the operators:
    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__year < other.__year:
            return True
        elif self.__year > other.__year:
            return False
        else:
            if self.__authors < other.__authors:
                return True
            elif self.__authors > other.__authors:
                return False
            else:
                if self.__title < other.__title:
                    return True
                else:
                    return False

        # complete this implementation and add all the other necessary operators!

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors == other.__authors and self.__title == other.__title and self.__year == other.__year:
            return True
        else:
            return False
        # complete this implementation and add all the other necessary operators!


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }