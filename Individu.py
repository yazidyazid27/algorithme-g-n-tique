# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:13:23 2021

@author: aissaouy
"""

import numpy as np

class Individu:

    def __init__(self,aGestionPopulation,aCoordonnees=None):
        self.gestionPopulation = aGestionPopulation
        
        if aCoordonnees != None:
            self.coordonnees=aCoordonnees
        else:
            self.coordonnees=[]
            for indexCoordonnees in range(aGestionPopulation.dimensionIndividu):
                zone=self.gestionPopulation.zone[indexCoordonnees]
                self.coordonnees.append(np.random.uniform(zone["min"],zone["max"]))

        self.performance=aGestionPopulation.evaluation.performance(self.coordonnees)
        self.indexPopulation=-1
        self.genetique=aGestionPopulation.codage.code(self.coordonnees)
       
    def __str__(self):
        chaine=""
        for indexCoordonnees in range(self.gestionPopulation.dimensionIndividu):
         ####  chaine=chaine + "================INDIVIDU[" +str(indexCoordonnees) + "]================= " +"\n"
            chaine=chaine + "coord[" + str(indexCoordonnees) + "]=" + str(self.coordonnees[indexCoordonnees])+ "   "
        
        chaine = chaine + "\n" + "performance=" + str(self.performance) + "\n" 
        chaine = chaine + "genetique=" + str(self.genetique)+ "\n"
        chaine = chaine +"#==============================================================#"
        return chaine
        
