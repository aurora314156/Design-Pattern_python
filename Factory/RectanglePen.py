from Pen import Pen
from PenType import PenType

class RectanglePen(Pen):
    def __init__(self, name):
        self.name = name
    
    def getType(self):
        return PenType.PenTypeRect