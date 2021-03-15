import unittest
from Water import Water

class StateTest(unittest.TestCase):
    def test_create_water(self):
        print('----- new test -----')
        water = Water()
        self.assertEqual('Liquid', water.behavior())
    
    def test_create_solid_water(self):
        print('----- new test -----')
        water = Water()
        water.setTemperature(-4)
        self.assertEqual('Solid', water.behavior())
    
    def test_create_liquid_water(self):
        print('----- new test -----')
        water = Water()
        water.riseTemperature(18)
        self.assertEqual('Liquid', water.behavior())
    
    def test_create_gaseous_water(self):
        print('----- new test -----')
        water = Water()
        water.riseTemperature(110)
        self.assertEqual('Gaseous', water.behavior())

if __name__ == '__main__':
    unittest.main()