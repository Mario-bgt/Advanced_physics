"""Read the example calls and provided output below. Then implement the necessary class(es) such that
they will produce the same output given the example calls.Use the following template:
"""


class Airplane():




passengers = Airplane.parse_manifest(("Montgomery,Rich,1;Tim,Merchant,2;Sally,Sale,2;Peter,Poor,3"))
a = Airplane("A388", "G-XLEK")
a.board(passengers)
print(a.get_passengers())
p = a.get_passengers(2)
print(type(p[1]))
print(p[1])
