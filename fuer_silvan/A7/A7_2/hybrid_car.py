#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if not isinstance(gas_capacity, (int, float)):
            raise Warning
        if not isinstance(gas_per_100km, (int, float)):
            raise Warning
        if not isinstance(battery_size, (int, float)):
            raise Warning
        if not isinstance(battery_range_km, (int, float)):
            raise Warning
        if gas_capacity < 0 or gas_per_100km < 0 or battery_size < 0 or battery_range_km < 0:
            raise Warning
        self.gas_capacity = gas_capacity
        self.gas_per_100km = gas_per_100km
        self.battery_size = battery_size
        self.battery_range_km = battery_range_km
        self.gas = gas_capacity
        self.battery = battery_size
        self.drive_mode = 'electric'

    def switch_to_combustion(self):
        self.drive_mode = 'combustion'

    def switch_to_electric(self):
        self.drive_mode = 'electric'

    def get_remaining_range(self, ndriving=True):
        if ndriving:
            return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

        if self.drive_mode == 'electric':
            return ElectricCar.get_remaining_range(self)
        else:
            return CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, (int, float)):
            raise Warning
        if dist < 0:
            raise Warning
        if dist > self.get_remaining_range(ndriving=False):
            dist = dist - self.get_remaining_range(ndriving=False)
            if self.drive_mode == 'electric':
                self.battery = 0
                self.switch_to_combustion()
                CombustionCar.drive(self, dist)
            else:
                self.gas = 0
                self.switch_to_electric()
                ElectricCar.drive(self, dist)

        if self.drive_mode == 'electric':
            ElectricCar.drive(self, dist)
        else:
            CombustionCar.drive(self, dist)
