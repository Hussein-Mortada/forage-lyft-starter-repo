import unittest

from tires.carriganTires import CarriganTires
from tires.octoPrimeTires import OctoPrimeTires

class TestTires(unittest.TestCase):
    def testCarriganTrue(self):
        tireWear=[0.1,0.2,0.6,1.5]
        tire = CarriganTires(tireWear)
        self.assertTrue(tire.needsService())

    def testCarriganFalse(self):
        tireWear = [0.1, 0.2, 0.6, 0.5]
        tire = CarriganTires(tireWear)
        self.assertFalse(tire.needsService())

    def testOctoPrimeTrue(self):
        tireWear = [1,1,1,1]
        tire = OctoPrimeTires(tireWear)
        self.assertTrue(tire.needsService())

    def testOctoPrimeFalse(self):
        tireWear = [1,0.5,0.5,0.9]
        tire = OctoPrimeTires(tireWear)
        self.assertFalse(tire.needsService())

