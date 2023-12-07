class Publication:
    def __init__(self, authors, title, year):
        self.__authors = list(authors)  # Make a copy to ensure immutability
        self.__title = title
        self.__year = year

    def __repr__(self):
        return f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"

    __str__ = __repr__

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) == (other.__authors, other.__title, other.__year)

    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) < (other.__authors, other.__title, other.__year)

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) <= (other.__authors, other.__title, other.__year)

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) > (other.__authors, other.__title, other.__year)

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) >= (other.__authors, other.__title, other.__year)

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) != (other.__authors, other.__title, other.__year)

    def get_authors(self):
        return list(self.__authors)  # Return a copy

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year


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
        p2: 398,}
