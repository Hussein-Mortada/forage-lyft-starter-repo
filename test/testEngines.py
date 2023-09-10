import unittest


from engine.capuletEngine import CapuletEngine
from engine.sternmanEngine import SternmanEngine
from engine.wiloughbyEngine import WilloughByEngine


class TestEngines(unittest.TestCase):
    def testCapuletEngineTrue(self):
        currentMileage = 50000
        lastServiceMileage = 0
        engine = CapuletEngine(currentMileage, lastServiceMileage)

        self.assertTrue(engine.needsService())

    def testCapuletEngineFalse(self):
        currentMileage = 30000
        lastServiceMileage = 0
        engine = CapuletEngine(currentMileage, lastServiceMileage)

        self.assertFalse(engine.needsService())

    def testSternmanEngineTrue(self):
        warningLightOn = True
        engine = SternmanEngine(warningLightOn)

        self.assertTrue(engine.needsService())


    def testSternmanEngineFalse(self):
        warningLightOn = False
        engine = SternmanEngine(warningLightOn)

        self.assertFalse(engine.needsService())

    def testWilloughByEngineTrue(self):
        currentMileage = 80000
        lastServiceMileage = 0
        engine = WilloughByEngine(currentMileage, lastServiceMileage)

        self.assertTrue(engine.needsService())
        

    def testWilloughByEngineFalse(self):
        currentMileage = 50000
        lastServiceMileage = 0
        engine = WilloughByEngine(currentMileage, lastServiceMileage)

        self.assertFalse(engine.needsService())


