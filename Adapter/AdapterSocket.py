from ISocket import ISocket

class AdapterSocket(ISocket):
    """ Socket adapter"""
    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return self.__britishSocket.name() + "轉換器"

    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("八字扁型")
        return socket