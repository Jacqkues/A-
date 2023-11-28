from abc import ABC, abstractmethod
class Heuristic(ABC):
    @abstractmethod
    def calculer_heuristic(self,a,b):
        pass