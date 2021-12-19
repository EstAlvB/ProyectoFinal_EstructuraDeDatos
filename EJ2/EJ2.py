#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
 
 
class RandomizedSet:

    def __init__(self):
        self.index_map = {} #this one has {[index, value]}
        self.values_map = {} ##this one has {[value,index]}
        
        self.item_count = 0 


    def insert(self,   val : int ):
        
        if val in self.values_map:
            return False
        
        
        self.values_map[val] = self.item_count
        self.index_map[self.item_count] = val
        
        self.item_count += 1
        
        return True


    def remove(self,  val : int): 
        
        if val not in self.values_map:
            return False
        
        temp = self.values_map[val]
        
        self.index_map.pop(temp)
        self.index_map[temp] = self.index_map[self.item_count - 1]
        self.values_map[self.index_map[self.item_count - 1]] = temp
        self.index_map.pop(self.item_count - 1)
        self.item_count -= 1
        return True
        
        

    def getRandom(self):
        
        index = random.randrange(0,self.item_count)
        return self.index_map(index)
        
        return
