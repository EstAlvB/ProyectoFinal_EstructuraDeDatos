import unittest
from ejercicio12 import vertical_traverse_tree

class test_num_odd_sum(unittest.TestCase):
    def test_basic1(self):
        self.assertEqual(vertical_traverse_tree([3,9,8,4,0,1,7]), [[4],[9],[3,0,1],[8],[7]])
    def test_basic2(self):
        self.assertEqual(vertical_traverse_tree([3,9,20,None,None,15,7]), [[9],[3,15],[20],[7]])
    def test_length(self):
        self.assertRaises(ValueError, vertical_traverse_tree, [1, 2])
    def test_empty(self):
        self.assertRaises(ValueError, vertical_traverse_tree, [])
    def test_theRootNode(self):
        self.assertEqual(vertical_traverse_tree([0]), [[0]])

if __name__ == "__main__":
    unittest.main()