import unittest
from datetime import date
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery


class TestBatteries(unittest.TestCase):
    def testNubbinBatteryTrue(self):
        currentDate = date.fromisoformat("2023-01-02")
        lastServiceDate = date.fromisoformat("2018-01-01")
        battery = NubbinBattery(currentDate, lastServiceDate)

        self.assertTrue(battery.needsService())

    def testNubbinBatteryFalse(self):
        currentDate = date.fromisoformat("2023-01-01")
        lastServiceDate = date.fromisoformat("2020-01-01")
        battery = NubbinBattery(currentDate, lastServiceDate)

        self.assertFalse(battery.needsService())

    def testSpindlerBatteryTrue(self):
        currentDate = date.fromisoformat("2023-01-02")
        lastServiceDate = date.fromisoformat("2020-01-01")
        battery = SpindlerBattery(currentDate, lastServiceDate)

        self.assertTrue(battery.needsService())

    def testSpindlerBatteryFalse(self):
        currentDate = date.fromisoformat("2023-01-01")
        lastServiceDate = date.fromisoformat("2022-01-01")
        battery = SpindlerBattery(currentDate, lastServiceDate)

        self.assertFalse(battery.needsService())
