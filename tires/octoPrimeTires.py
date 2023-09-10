from tires.tire import Tire


class OctoPrimeTires(Tire):
    def __init__(self, tireWear):
        self.tireWear = tireWear

    def needsService(self):
        return sum(self.tireWear)>=3.0

