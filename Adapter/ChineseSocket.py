from ISocket import ISocket
from SocketEntity import SocketEntity

class ChineseSocket(ISocket):
    """ 國際標準插座"""
    def getName(self):
        return "國際標準插座"

    def getSocket(self):
        return SocketEntity(3, "八字扁型")

