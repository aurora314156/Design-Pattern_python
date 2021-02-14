
from LinePen import LinePen
from RectanglePen import RectanglePen
from EllipsePen import EllipsePen
from PenType import PenType

class PenFactory:
    """ 畫筆工廠 """
    def __init__(self):
        self.__pens = {}
        self.__penList = {
            PenType.PenTypeLine: LinePen("直線畫筆"),
            PenType.PenTypeRect: RectanglePen("矩形畫筆"),
            PenType.PenTypeEllipse: EllipsePen("橢圓畫筆")
        }
    
    def createPen(self, PenType):
        if PenType not in self.__pens:
            pen = self.__penList.get(PenType, "")
            self.__pens[PenType] = pen
        return self.__pens[PenType]
