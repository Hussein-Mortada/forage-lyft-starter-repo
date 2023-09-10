from abc import ABC, abstractmethod

class Serviceable:
    @abstractmethod
    def needsService(self):
        pass