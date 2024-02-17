"""Implement a class Currency, which takes three parameters in its constructor:
name, then name of the currency
amount, the amount of currency represented
rate, a conversion rate representing the value of one unit of this currency relative to a gold standard
These three values should be stored as instance attributes.
The Currency class should implement the equality operator as follows. Two instances of Currency are equal if
multiplying the amount with the rate results in the same value for both instances. Considering the first example below,
 15 EUR are equal to 10 GBP because 15 * 0.5 equals 10 * 0.75. Do not forget to correctly handle cases where the value
 being compared to is not an
instance of Currency.
You may assume that Currency will only be constructed with parameters that match the description.
Use the following template:"""


class Currency:
    def __init__(self, name, amount, rate):
        self.__name = name
        self.__amount = amount
        self.__rate = rate


    def __eq__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        val_self = self.__amount * self.__rate
        val_other = other.__amount * other.__rate
        if val_self == val_other:
            return True
        return False






print( Currency("EUR", 15, 0.5) == Currency("GBP", 10, 0.75) )
print( Currency("EUR", 15, 0.5) != Currency("GBP", 15, 0.75) )
print( Currency("GBP", 1, 0.75) == Currency("GBP", 10, 0.75) )
print( Currency("CHF", 1.50, 0.78) == "Enough to buy a coffee" )