from engine.engine import Engine

class WilloughByEngine(Engine):
    def __init__(self, currentMileage, lastServiceMileage):
        self.currentMileage=currentMileage
        self.lastServiceMileage=lastServiceMileage

    def needsService(self):
        return self.currentMileage - self.lastServiceMileage > 60000