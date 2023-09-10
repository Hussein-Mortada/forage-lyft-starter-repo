from battery.battery import Battery
from battery.utilities import add_years_to_date


class NubbinBattery(Battery):
    def __init__(self,currentDate, lastServiceDate):
        self.currentDate = currentDate
        self.lastServiceDate = lastServiceDate

    def needsService(self):
        shouldBeServicedBy = add_years_to_date(self.lastServiceDate, 4)
        return shouldBeServicedBy < self.currentDate

