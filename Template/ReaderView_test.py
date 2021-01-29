import unittest
from SmoothView import SmoothView
from SimulationView import SimulationView

class Reader(unittest.TestCase):
    def testReaderSmooth(self):
        smoothview = SmoothView()
        smoothview.nextPage()
        smoothview.prevPage()
    
    def testReaderSimulation(self):
        simulation = SimulationView()
        simulation.nextPage()
        simulation.prevPage()
        
if __name__ == "__main__":
    unittest.main()