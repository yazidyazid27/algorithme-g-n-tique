# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:26:17 2021

@author: farnierl
"""

from CodageMantisse import *
from CodageGray import *
from Population import *
from GestionPopulation import *
from CrossOver import *
from CrossOverUnPoint import *
from CrossOverMultiPoints import *
from Individu import *
from EvaluationF1SumSquare import *
from Selection import *
from SelectionRoueDeLaFortune import *
import random as rd

class CrossOverUnPoint(CrossOver) :
    def __init__(self):
        pass 
    
    def BrassageUnPoint(self,parents,gestionPopulation):
        # Il s'agit d'une surcharge de la fonction CrossOverMultiPoints en forçant le nombred e points à être 1
        Enfants = CrossOverMultiPoints.BrassageMultiPoints(parents,parents,gestionPopulation,1)        
        return (enfants)
        
        
if __name__ == '__main__':      

    monCodage=CodageMantisse(32,6)
    NbIndividuDansPopulation=2
    zone=[{"min":2**31,"max":2**31},{"min":2**31,"max":2**31}]

    monCrossOver=CrossOverUnPoint()
    monEvaluation=EvaluationF1SumSquare()
    maSelection=SelectionRoueDeLaFortune()          
    
    
    gestionPopulation=GestionPopulation(monCodage,zone,monCrossOver,monEvaluation,0)  
    maPopulation=Population(NbIndividuDansPopulation,gestionPopulation)  
    print("Pop 0",'\n')
    # maPopulation.AffichePopulation()
   
    parentsIndex=maSelection.tirageIndex(maPopulation.population)
    parents=[]
    parents
    parents.append(maPopulation.population[parentsIndex[0]])
    parents.append(maPopulation.population[parentsIndex[1]])
    # nbPoints = 1
    print('parents1 genetique :', maPopulation.population[parentsIndex[0]].genetique)
    enfants = CrossOverUnPoint.BrassageUnPoint(parents,parents, gestionPopulation)
    # print('les parents sont :',parents)
    # print('les enfants sont : ',enfants)
    print('\n','La performance des individus de la population initiale sont : ',maPopulation.population[0].performance,'et',maPopulation.population[1].performance)
    maPopulation.RemplacerIndividu(parents,enfants)
    print('\n','Pop 1','\n')
    
    print('\n','La performance des individus de la nouvelle population sont : ',maPopulation.population[0].performance,'et',maPopulation.population[1].performance)
    # maPopulation.AffichePopulation()
    
    print('\n')
    
    
    # print('Le code de la 1ere coordonnee du parent 1 est :',maPopulation.population[parentsIndex[0]].genetique[0])
    # print('Le code de la 1ere coordonnee du parent 2 est :',maPopulation.population[parentsIndex[1]].genetique[0])
    print('\n')
    print("Le code  de l'enfant 1 est :",enfants[0].genetique )
    print("Le code  de l'enfant 2 est :",enfants[1].genetique )