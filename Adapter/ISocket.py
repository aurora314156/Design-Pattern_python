
from abc import ABCMeta, abstractmethod

class ISocket(metaclass=ABCMeta):
    """ Socket type """
    def getName(self):
        """ Socket name """
        pass

    def getSocket(self):
        """ Get socket """
        pass

