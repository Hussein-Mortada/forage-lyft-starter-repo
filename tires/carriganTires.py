from tires.tire import Tire

class CarriganTires(Tire):
    def __init__(self, tireWear):
        self.tireWear = tireWear

    def needsService(self):
        for tire in self.tireWear:
            if tire >= 0.9:
                return True

        return False

