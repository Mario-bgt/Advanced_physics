#!/usr/bin/env python3
"""Um alle Werte oben und unten gleichzumachen, sollten die gegebenen Dominosteine eine ausreichende Anzahl gleicher
 Werte haben. Wir müssen also die Häufigkeit der Werte auf der Ober- und Unterseite vergleichen. Wenn genügend, sagen
  wir 2er, auf der Unterseite vorhanden sind um die Bedingung zu erfüllen, können wir true zurückgeben. Ausserdem
   sollten wir die Dominosteine mit doppelten Werten berücksichtigen. Es ist möglich, dass eine Häufigkeit von
   irgendeinem Wert zeigt, dass wir genug geeignete Dominosteine haben, aber sie können ein Teil der Duplikaten sein.
   Wir müssen also solche Duplikate zählen. In unserem Fall erstellen wir einen eigenen Zähler für jeden Wert ohne
   Duplikate."""


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    length = len(top)
    top_counter = [0 for i in range(6)]
    bottom_counter = [0 for i in range(6)]
    total_counter = [length for i in range(6)]
    for topnum, bottomnum in zip(top, bottom):
        if topnum == bottomnum:
            total_counter[topnum-1] -= 1
        else:
            top_counter[topnum-1] += 1
            bottom_counter[bottomnum-1] += 1

    for i in range(6):
        if total_counter[i] - top_counter[i] == bottom_counter[i]:
            return min(top_counter[i], bottom_counter[i])

    return -1


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
