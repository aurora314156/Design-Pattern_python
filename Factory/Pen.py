from abc import ABCMeta, abstractmethod


class Pen(metaclass=ABCMeta):
    """ 畫筆 """
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
            
    @abstractmethod
    def getType(self):
        pass
