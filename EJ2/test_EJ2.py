#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest 

from EJ2 import insert, remove, getRandom

class RandomSetTest (unittest.TestCase):
    
    def test_insert1 (self):
        self.assertTrue(insert(2))
        
    def test_insert2 (self):
        self.assertFalse(remove(3))
        
    def test_type1 (self):
        self.assertEqual(type(getRandom()), int)
        
        
        
        
        
        
       
if __name__ == "__main__":
    unittest.main()