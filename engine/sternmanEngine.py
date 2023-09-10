from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warningLightOn):
        self.warningLightOn = warningLightOn

    def needsService(self):
        return self.warningLightOn