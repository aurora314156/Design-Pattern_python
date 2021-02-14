from Pen import Pen
from PenType import PenType

class EllipsePen(Pen):
    def __init__(self, name):
        super().__init__(name)
    
    def getType(self):
        return PenType.PenTypeEllipse