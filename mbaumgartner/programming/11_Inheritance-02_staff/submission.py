from abc import ABC, abstractmethod


class Restaurant:
    def __init__(self, name):
        self.name = name


class Staff(ABC):
    seq = 101

    def __init__(self, rest, base_salary):
        self.number = Staff.seq
        self.restaurant = rest.name
        self.shifts = []
        self.base_salary = base_salary
        Staff.seq += 1

    def work(self, hours):
        self.shifts.append(hours)

    def __repr__(self):
        return "Staff working for " + str(self.restaurant) + " with salary " + str(self.salary())

    @abstractmethod
    def salary(self):
        pass




class Server(Staff):
    def __init__(self, rest, base_salary, hourly_salary):
        super().__init__(rest, base_salary)
        self.hourly_salary = hourly_salary

    def salary(self):
        return self.base_salary + sum(self.shifts)*self.hourly_salary



class Dishwasher(Staff):
    def __init__(self, rest, base_salary, hourly_salary):
        super().__init__(rest, base_salary)
        self.hourly_salary = hourly_salary

    def salary(self):
        return (self.base_salary + sum(self.shifts)*self.hourly_salary)*0.9


class Cook(Staff):
    def __init__(self, rest, base_salary):
        super().__init__(rest, base_salary)

    def salary(self):
        return self.base_salary