"""Implement a class Hand, which takes one parameter in its constructor:
cards, a list of distinct integers representing card values of a simple card game
This value should be stored as.
The Hand class should implement the equality operator as follows. Two instances of Hand are equal if the sum of
card values is the same for both instances. However, in this game, the card with value 1 counts as 11 for the equality
operation. Considering the first example below, the sum of cards 1 and 2 is 13 because the 1 counts as 11. Do not
 forget to correctly handle cases where the
value being compared to is not an instance of Currency.
You may assume that Hand will only be constructed with parameters that match the description.
Use the following template:
"""

class Hand:
    def __init__(self, cards):
        self.__cards = cards

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        x = [11 if i == 1 else i for i in self.__cards]
        y = [11 if i == 1 else i for i in other.__cards]
        if sum(x) == sum(y):
            return True
        return False







print( Hand([1, 2]) == Hand([10, 3]) )
print( Hand([2, 5, 7]) == Hand([10, 4]) )
print( Hand([2, 5, 7]) != Hand([9]) )
print( Hand([2, 5, 7]) == "Flush" )
