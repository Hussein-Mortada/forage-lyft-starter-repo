from battery.battery import Battery
from battery.utilities import addYears


class NubbinBattery(Battery):
    def __init__(self,currentDate, lastServiceDate):
        self.currentDate = currentDate
        self.lastServiceDate = lastServiceDate

        def needsService(self):
            shouldBeServicedBy = addYears(self.lastServiceDate, 4)
            return shouldBeServicedBy < self.currentDate

