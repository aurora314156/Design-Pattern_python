import unittest
from PenFactory import PenFactory
from PenType import PenType

class FactoryTest(unittest.TestCase):
    def testCreatePen(self):
        factory = PenFactory()
        linePen = factory.createPen(PenType.PenTypeLine)
        self.assertEqual("直線畫筆", linePen.getName())
        print('創造一隻: %s, id: %s, Type: %s' % (linePen.getName(), id(linePen), linePen.getType()))
        print('Create pen successful.')

    def testPenFactory(self):
        print()
        factory = PenFactory()
        linePen = factory.createPen(PenType.PenTypeLine)
        self.assertEqual("直線畫筆", linePen.getName())
        print('創造一隻: %s, id: %s, Type: %s' % (linePen.getName(), id(linePen), linePen.getType()))
        recPen = factory.createPen(PenType.PenTypeRect)
        self.assertEqual("矩形畫筆", recPen.getName())
        print('創造一隻: %s, id: %s, Type: %s' % (recPen.getName(), id(recPen), recPen.getType()))
        recPen2 = factory.createPen(PenType.PenTypeRect)
        self.assertEqual("矩形畫筆", recPen2.getName())
        print('創造一隻: %s, id: %s, Type: %s' % (recPen2.getName(), id(recPen2), recPen2.getType()))
        ellipse = factory.createPen(PenType.PenTypeEllipse)
        self.assertEqual("橢圓畫筆", ellipse.getName())
        print('創造一隻: %s, id: %s, Type: %s' % (ellipse.getName(), id(ellipse), ellipse.getType()))
        
if __name__ == '__main__':
    unittest.main()