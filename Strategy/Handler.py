from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    "Handler abstract class"
    
    @abstractmethod
    def handler(self):
        pass
