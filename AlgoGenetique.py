# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:19:14 2021

@author: cserr
"""

from CodageMantisse import *
from CodageGray import *
from Population import *
from GestionPopulation import *
from CrossOverUnPoint import *
from CrossOverMultiPoints import *
from CrossOverUniforme import *
from Individu import *
from EvaluationF1SumSquare import *
from Selection import *
from SelectionRoueDeLaFortune import *
from Mutation import *


#=================== Début Initialisation des paramétres ================
#monCodage=CodageMantisse(32,6)
monCodage=CodageGray(32,6) #Gray
NbIndividuDansPopulation=100
zone=[{"min":-10,"max":10},{"min":-5,"max":10}]#,{"min":-30000.5,"max":-20000.5},{"min":-300.5,"max":300.5}]
#zone=[{"min":-0.001,"max":0.001},{"min":-0.001,"max":0.001},{"min":-0.001,"max":0.001},{"min":-0.001,"max":0.001}]
#monCrossOver=CrossOverUnPoint()
#monCrossOver=CrossOverMultiPoints()
monCrossOver = CrossOverUniforme()
monEvaluation=EvaluationF1SumSquare()
maSelection=SelectionRoueDeLaFortune()
mute=Mutation()
#=================== Fin Initialisation des paramétres ================



gestionPopulation=GestionPopulation(monCodage,zone,monCrossOver,monEvaluation,0)  
#print(gestionPopulation.dimensionIndividu)
#print(gestionPopulation.zone)    
maPopulation=Population(NbIndividuDansPopulation,gestionPopulation)    
maPopulation.AffichePopulation()

print("SERRA")
nbiteration=15000
for index in range (nbiteration): 
  iteration=index+1
  parentsIndex=maSelection.tirageIndex(maPopulation.population)
  #☺print(parents)
  parents=[]
  parents
  parents.append(maPopulation.population[parentsIndex[0]])
  parents.append(maPopulation.population[parentsIndex[1]])
  #print(parents)
#  NbPoints = 5
#  enfants=monCrossOver.BrassageUnpoint(parents,gestionPopulation)
#  enfants = monCrossOver.BrassageMultiPoints(parents,gestionPopulation,NbPoints)
  enfants = monCrossOver.BrassageUniforme(parents,gestionPopulation)
  #print(enfants)
  #Newenfants = Mutation.inverse(enfants,0.5,gestionPopulation)
  #maPopulation.AffichePopulation()
  maPopulation.RemplacerIndividu(parents,enfants)
  
print("=======================FIN===================") 
maPopulation.AffichePopulation()
print("=======================Meilleur===================") 
print(maPopulation.AffichePlusFaible())
print("=======================graphique===================") 
maPopulation.TracerGraphique() 
    
   
    