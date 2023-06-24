# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:16:20 2021

@author: farnierl
"""
from Selection import *

class CrossOver :
    def __init__(self,parents):
        self.parent1 = parents[0]
        self.parent2 = parents[1]
        self.enfant1 = []
        self.enfant2 = []
    