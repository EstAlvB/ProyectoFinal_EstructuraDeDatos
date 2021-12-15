#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from EJ11 import findStr

class test_strobo_nums(unittest.TestCase):
    def test_basic1(self):
        self.assertEqual(findStr(2), ['00', '11', '69', '88', '96'])
        
    def test_basic2(self):
        self.assertEquals(findStr(5), ['00000',
 '01010',
 '06090',
 '08080',
 '09060',
 '10001',
 '11011',
 '16091',
 '18081',
 '19061',
 '60009',
 '61019',
 '66099',
 '68089',
 '69069',
 '80008',
 '81018',
 '86098',
 '88088',
 '89068',
 '90006',
 '91016',
 '96096',
 '98086',
 '99066',
 '00100',
 '01110',
 '06190',
 '08180',
 '09160',
 '10101',
 '11111',
 '16191',
 '18181',
 '19161',
 '60109',
 '61119',
 '66199',
 '68189',
 '69169',
 '80108',
 '81118',
 '86198',
 '88188',
 '89168',
 '90106',
 '91116',
 '96196',
 '98186',
 '99166',
 '00800',
 '01810',
 '06890',
 '08880',
 '09860',
 '10801',
 '11811',
 '16891',
 '18881',
 '19861',
 '60809',
 '61819',
 '66899',
 '68889',
 '69869',
 '80808',
 '81818',
 '86898',
 '88888',
 '89868',
 '90806',
 '91816',
 '96896',
 '98886',
 '99866']) #se copio asi pero no quiero tener que poner en linea un po uno
        
    def test_exeption1(self):
        self.assertRaises(ValueError, findStr, -2)
        
    def test_exeption2(self):
        self.assertRaises(TypeError , findStr , 9.21)
        
    def test_cero1(self):
        self.assertEqual(findStr(0), [''])
        
        
        
if __name__ == "__main__":
    unittest.main()