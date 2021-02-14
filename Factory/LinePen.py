from PenType import PenType
from Pen import Pen

class LinePen(Pen):
    def __init__(self, name):
        self.name = name
    
    def getType(self):
        return PenType.PenTypeLine