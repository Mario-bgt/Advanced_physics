#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not isinstance(gas_capacity, (int, float)):
            raise Warning
        if not isinstance(gas_per_100km, (int, float)):
            raise Warning
        if gas_capacity < 0 or gas_per_100km <0:
            raise Warning
        self.gas_capacity = gas_capacity
        self.gas_per_100km = gas_per_100km
        self.gas = gas_capacity
        super(CombustionCar, self).__init__()

    def fuel(self, f):
        if not isinstance(f, (int, float)):
            raise Warning
        if f < 0:
            raise Warning
        if f + self.gas > self.gas_capacity:
            self.gas = 0
            raise Warning("Too much fuel")
        else:
            self.gas += f

    def get_gas_tank_status(self):
        return self.gas, self.gas_capacity

    def get_remaining_range(self):
        return self.gas / self.gas_per_100km * 100

    def drive(self, dist):
        if not isinstance(dist, (int, float)):
            raise Warning
        if dist < 0:
            raise Warning
        if dist > self.get_remaining_range():
            self.gas = 0
            raise Warning("Not enough fuel")
        else:
            self.gas -= dist / 100 * self.gas_per_100km
