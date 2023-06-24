# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:45:59 2021

@author: rouahim
"""
#import Selection
from Population import *
import random as rd
class SelectionRoueDeLaFortune():

    def __init__(self):
        pass
        
    
    def tirage(self,population):
        self.selec=[]
        a=rd.choice(population)
        self.selec.append(a)
        b=rd.choice(population)
        if b!=a:
            self.selec.append(b)
        else:
            b=rd.choice(population)
        return(self.select)
        
        
    def tirageIndex(self,population):
        self.selec=[]
        a=rd.randint(0,len(population)-1)
        self.selec.append(a)
        b=rd.randint(0,len(population)-1)
        while a==b:
            b=rd.randint(0,len(population)-1)
        self.selec.append(b)
        #print("a=",a," b=",b)
        return (self.selec)
            
