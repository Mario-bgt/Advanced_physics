#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not isinstance(battery_size, (int, float)):
            raise Warning
        if not isinstance(battery_range_km, (int, float)):
            raise Warning
        if battery_size < 0 or battery_range_km < 0:
            raise Warning
        self.battery_size = battery_size
        self.battery_range_km = battery_range_km
        self.battery = battery_size
        super(ElectricCar, self).__init__()

    def charge(self, kwh):
        if not isinstance(kwh, (int, float)):
            raise Warning
        if kwh < 0:
            raise Warning
        if kwh + self.battery > self.battery_size:
            self.battery = 0
            raise Warning("Too much charge")
        else:
            self.battery += kwh

    def get_battery_status(self):
        return self.battery, self.battery_size

    def get_remaining_range(self):
        return (self.battery / self.battery_size) * self.battery_range_km

    def drive(self, dist):
        if not isinstance(dist, (int, float)):
            raise Warning
        if dist < 0:
            raise Warning
        if dist > self.get_remaining_range():
            self.battery = 0
            raise Warning("Not enough charge")
        else:
            self.battery -= (dist / self.battery_range_km) * self.battery_size
