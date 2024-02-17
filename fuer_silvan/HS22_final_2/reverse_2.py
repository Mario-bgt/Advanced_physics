"""Read the example calls and provided output below. Then implement the necessary class(es) such that they will
 produce the same output given the example calls.
Use the following template:"""
# Your implementation of the necessary class(es)
class Train:
    def __init__(self, line, name):
        self.__line = line
        self.__name = name
        self.__passagers = []

    def board(self, lyst):
        for passenger in lyst:
            self.__passagers.append(passenger)

    def get_riders(self, ticket="no"):
        if ticket == "no":
            return self.__passagers
        if ticket == "GA":
            res = []
            for p in self.__passagers:
                t = p.split(", ")[1]
                if t == "general ticket":
                    res.append(p)
            return res

        if ticket == "D":
            res = []
            for p in self.__passagers:
                t = p.split(", ")[1]
                if t == "day ticket":
                    res.append(p)
            return res

        if ticket == "M":
            res = []
            for p in self.__passagers:
                t = p.split(", ")[1]
                if t == "monthly ticket":
                    res.append(p)
            return res

    @staticmethod
    def parse_reservations(string):
        res =[]
        x = string.split(";")
        for p in x:
            vals  = p.split(",")
            if vals[2] == "GA":
                ticket = "general ticket"
            elif vals[2] == "D":
                ticket = "day ticket"
            elif vals[2] == "M":
                ticket = "monthly ticket"
            else:
                ticket = "unknonw ticket"
            res.append(vals[0] + " " + vals[1] + ", " + ticket)
        return res






# The following example illustrates how the solution may be used:

riders = Train.parse_reservations(("Montgomery,Rich,GA;Tim,Merchant,GA;Sally,Sale,D;Peter,Poor,M"))
a = Train("IC17", "Columbus")
a.board(riders)
print(a.get_riders())
p = a.get_riders("GA")
print(type(p[1]))
print(p[1])
"""
The code above should produce the following output:
[Montgomery Rich, general ticket, Tim Merchant, general ticket, Sally Sale, day ticket, Peter Poor, monthly ticket]
<class '__main__.Rider'>
Tim Merchant, general ticket
"""