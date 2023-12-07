#!/usr/bin/env python3

# The signatures of this class and its task methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce grading/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        if not isinstance(authors, list) or not all(isinstance(author, str) for author in authors):
            raise TypeError("Authors must be a list of strings")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_title(self):
        return self.__title

    def get_authors(self):
        return self.__authors.copy()

    def get_year(self):
        return self.__year

    def __repr__(self):
        return f"Publication({self.__authors}, {self.__title}, {self.__year})"

    def __str__(self):
        authors_str = ', '.join(f'\"{author}\"' for author in self.__authors)
        return f"Publication([{authors_str}], \"{self.__title}\", {self.__year})"

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors == other.__authors and self.__title == other.__title and self.__year == other.__year:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors < other.__authors:
            return True
        if len(self.__authors) < len(other.__authors):
            return True
        if self.__authors == other.__authors:
            if self.__title < other.__title:
                return True
            elif self.__year < other.__year:
                return True
        else:
            return False

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if __eq__(self, other) or __lt__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if __eq__(self, other):
            return False
        else:
            return True

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if __lt__(self, other) or __eq__(self, other):
            return False
        else:
            return True

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if __lt__(self, other):
            return False
        else:
            return True

    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

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
