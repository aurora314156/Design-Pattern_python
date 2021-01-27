import unittest
from SocketEntity import SocketEntity
from ChineseSocket import ChineseSocket
from BritishSocket import BritishSocket
from AdapterSocket import AdapterSocket

def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "八字扁型":
        isStandard = "符合"
        canCharge = "可以"
    else:
        isStandard = "不符合"
        canCharge = "不能"

    print("[%s]：\n接腳数量：%d，接腳類型：%s； %s台灣標準，%s给台灣的電子設備充電！"
        % (name, socket.getNumOfPin(), socket.getTypeOfPin(), isStandard, canCharge))
    return isStandard

class Socket(unittest.TestCase):
    def testChineseSocket(self):
        chineseSocket = ChineseSocket()
        isMatch = canChargeforDigtalDevice(chineseSocket.getName(), chineseSocket.getSocket())
        self.assertEqual("符合", isMatch)
    
    def testBritishSocket(self):  
        britishSocket = BritishSocket()
        isMatch = canChargeforDigtalDevice(britishSocket.name(), britishSocket.socketInterface())
        self.assertEqual("不符合", isMatch)
    
    def testAdapterSocket(self):
        britishSocket = BritishSocket()
        adapterSocket = AdapterSocket(britishSocket)
        isMatch = canChargeforDigtalDevice(adapterSocket.getName(), adapterSocket.getSocket())
        self.assertEqual("符合", isMatch)


if __name__ == '__main__':
    unittest.main()