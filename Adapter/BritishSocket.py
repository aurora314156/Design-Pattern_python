from SocketEntity import SocketEntity

class BritishSocket:
    """ 英國標準 """

    def name(self):
        return "英國標準插座"

    def socketInterface(self):
        return SocketEntity(3, "T字方型")
