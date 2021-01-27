from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class SocketEntity:
    """ Type definition"""

    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin

