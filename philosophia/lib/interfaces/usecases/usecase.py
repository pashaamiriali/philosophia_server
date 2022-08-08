from abc import ABC, abstractmethod


class Usecase(ABC):
    
    @abstractmethod
    def handle(self, request):
        pass