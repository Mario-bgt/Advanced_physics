#!/usr/bin/env python3

class Inventory:
    def __init__(self, name="DEFAULT", balance=0, max_weight=0):
        self.__player_name = name
        self.__balance = balance
        self.__max_weight = max_weight
        self.__content = []


    def collect(self, item):
        if self.get_inv_weight() + item[2] > self.__max_weight:
            raise Warning("Item too heavy")
        if self.__proper_item(item):
            self.__content.append(item)
        else:
            raise Warning("Item is not a 3-tuple of string, int, int")

    def get_inv_weight(self):
        w = 0
        for item in self.__content:
            w += item[2]
        return w

    def get_balance(self):
        return self.__balance

    def get_player_name(self):
        return self.__player_name

    def get_inv_value(self):
        v = 0
        for item in self.__content:
            v += item[1]
        return v

    def drop(self, item):
        if item in self.__content:
            self.__content.remove(item)
            return item
        else:
            raise Warning("Item not in inventory")

    def sell(self, item):
        if item in self.__content:
            self.__balance += item[1]
            self.__content.remove(item)
            return item
        else:
            raise Warning("Item not in inventory")

    def buy(self, item):
        if self.__balance < item[1]:
            raise Warning("Not enough money")
        if self.get_inv_weight() + item[2] > self.__max_weight:
            raise Warning("Item too heavy")
        if self.__proper_item(item):
            self.__balance -= item[1]
            self.__content.append(item)
        else:
            raise Warning("Item is not a 3-tuple of string, int, int")

#implement this function to check if a given object fits the described type for an item (3-tuple of string, int, int)
#raise a Warning if it doesn't
    def __proper_item(self, item):
        if type(item) != tuple or len(item) != 3 or type(item[0]) != str or type(item[1]) != int or type(item[2]) != int:
            return False
        return True

    def __iter__(self):
        return iter(sorted(self.__content, key=lambda item: item[1], reverse=True))

    def __len__(self):
        return len(self.__content)
