#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest 

from EJ5 import trueFibo

class RandomSetTest (unittest.TestCase):
    
    def test_basic1 (self):
        self.assertTrue(trueFibo(3))
        
    def test_basic2 (self):
        self.assertFalse(trueFibo(1))
        
    def test_general1 (self):
        self.assertEqual(trueFibo(6), True)
    
    def test_general2 (self):
        self.assertEqual(trueFibo(7), False)
        
       
if __name__ == "__main__":
    
    unittest.main()