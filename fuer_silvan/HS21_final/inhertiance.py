from abc import ABC, abstractmethod

class Actor(ABC):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def monthly_pay(self):
        pass

class Lead(Actor):
    ident = 0
    def __init__(self, name, yearly_pay):
        super().__init__(name)
        self.__yearly_pay = yearly_pay
        self.__ID = self.ident
        self.__monthly_pay = yearly_pay/12
        self.ident += 1

    def get_ID(self):
        return self.__ID

    def monthly_pay(self):
        return self.__monthly_pay

    def __repr__(self):
        return "Salary: " + str(self.__monthly_pay) + " (" + str(self.__ID) + ")"

    def __str__(self):
        return "Salary: " + str(self.__monthly_pay) + " (" + str(self.__ID) + ")"

class Extra(Actor):

    def __init__(self, name, minimum_pay, hours):
        if minimum_pay < 9.4:
            raise ValueError
        super().__init__(name)
        self.__monthly_pay = minimum_pay*hours
        self.__hours = hours

    def monthly_pay(self):
        return self.__monthly_pay

    def __repr__(self):
        return "Salary: " + str(self.__monthly_pay) + " (temp)"



class Studio:

    def __init__(self, name):
        self.name = name
        self.__actors = []

    def add_actor(self, actor):
        self.__actors.append(actor)

    def get_monthly_staff_cost(self):
        cost = 0
        for actor in self.__actors:
            cost += actor.monthly_pay()
        return cost

    pass

# DO NOT SUBMIT THE LINES BELOW!
#e = Studio("Warmer Sisters")
#i1 = Lead("Bob", 60000) # yearly salary
#i2 = Lead("Alice", 75000) # yearly salary
#i3 = Extra("Taylor", 21.50, 15) # hourly salary, hours per month
#assert i1.get_name() == "Bob"
#assert i3.get_name() == "Taylor"
#assert i1.get_id() == 0
#assert i2.get_id() == 1
#assert i1.get_monthly_salary() > 4000
#assert i3.get_monthly_salary() == 322.50
#e.add_actor(i1)
#e.add_actor(i2)
#e.add_actor(i3)
#assert e.get_monthly_staff_cost() > 9000