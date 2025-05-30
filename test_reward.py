import unittest
from reward import calculate_heading

class TestHeadingCalculation(unittest.TestCase):
    def test_east(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [5., 1.]), 0., places=1)
    
    def test_north_east(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [5., 5.]), 45., places=1)
    
    def test_north(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [1., 5.]), 90., places=1)
    
    def test_north_west(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [-5., 5.]), 146.3, places=1)
    
    def test_west(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [-2., 1.]), 180., places=1)
        
    def test_south_west(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [0., 0.]), 225., places=1)

    def test_south(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [1., -1.5]), 270., places=1)
    
    def test_south_east(self):
        self.assertAlmostEqual(calculate_heading([1., 1.], [5.5, -1.5]), 330.9, places=1)
    
    def test_edge_case_when_target_point_equal_to_guide_point(self):
        self.assertAlmostEqual(calculate_heading([1.25, 1.25], [2.25, 1.25]), 0., places=1)

    def test_edge_case_when_target_point_equal_to_current_point(self):
        self.assertRaises(ZeroDivisionError, calculate_heading, [1.25, 1.25], [1.25, 1.25])

if __name__ == '__main__':
    unittest.main(verbosity=2)
