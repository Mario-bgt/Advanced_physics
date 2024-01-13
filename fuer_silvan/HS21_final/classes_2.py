class Event:
    def __init__(self, name, places):
        self.__name = name
        self.__places = places
        self.__seats = [0 for i in range(places)]

    def enter(self, place_number, person):
        if place_number < 1 or place_number > self.__places:
            return IndexError
        if self.__seats[place_number - 1] != 0:
            return NameError
        else:
            self.__seats[place_number - 1] = person

    def get(self, sitznr):
        if sitznr < 1 or sitznr > self.__places:
            return IndexError
        if self.__seats[sitznr - 1] == 0:
            return None
        else:
            return self.__seats[sitznr - 1]

    def empty(self):
        res = 0
        for i in self.__seats:
            if i == 0:
                res += 1
        return res

    def occupied(self):
        return self.__places - self.empty()

    def get_name(self):
        return self.__name

    def __lt__(self, other):
        if self.occupied() < other.occupied():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.occupied() == other.occupied():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.occupied() > other.occupied():
            return True
        else:
            return False


# DO NOT SUBMIT THE LINES BELOW!
#e1 = Event(150)
#e1.enter(45, "Alice")
#assert e1.get(45) == "Alice"
#e1.enter(42, "Bob")
#assert e1.occupied() == 2
#assert e1.empty() == 148
#e2 = Event(40)
#assert e2.get(40) == None
#e2.enter(1, "Andrea")
#e2.enter(2, "Beatrice")
#assert e2 == e1
#e2.enter(20, "Charly")
#assert e2 > e1