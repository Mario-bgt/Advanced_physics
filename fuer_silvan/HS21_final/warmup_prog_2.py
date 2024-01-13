"""Implementieren Sie eine rekursive Funktion count, die eine Liste l annimmt, welche beliebige Elemente enthalten kann,
 einschliesslich verschachtelte Listen. Die Funktion soll die Anzahl Elemente in l zählen, wobei jede verschachtelte
 Liste besonders behandelt werden soll: anstatt sie einfach als einzelnes Element zu zählen, soll sie in einem rekursiven
  Aufruf an count übergeben werden, damit auch die Elemente in der verschachtelten Liste einzeln mitgezählt werden.
  Die Liste selbst soll dabei nicht mitgezählt werden. Beachten Sie die Assertions als Beispiele für die Anwendung
   von calc. Falls Ihre Lösung nicht rekursiv ist, erhalten Sie höchstens die Hälfte der erreichbaren Punkte."""


def count(l):
    res = 0
    for i in l:
        if type(l) == list:
            res += count(l)
        else:
            res += 1
    return res


# DO NOT SUBMIT THE LINES BELOW!
assert count([]) == 0
assert count([[], []]) == 0
assert count([1, "", [{}], [[True], 4]]) == 5
