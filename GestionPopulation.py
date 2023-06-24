# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from CodageMantisse import *
from CodageGray import *
from Population import *
from GestionPopulation import *
from CrossOverUnPoint import *
from Individu import *
from EvaluationF1SumSquare import *
from Selection import *
from SelectionRoueDeLaFortune import *
from Mutation import *

class GestionPopulation:
    def __init__(self,aCodage,aZone,aCrossover,aEvaluation,aTypeOptimization=0):
        self.dimensionIndividu=len(aZone)
        self.codage=aCodage
        self.zone=aZone
        self.crossover=aCrossover
        self.evaluation=aEvaluation
        self.typeOptimization=aTypeOptimization
        
        
#    def __str__(self):
#        return self.pop


    # def regeneration(self,nbIndividuGarde):
    #     self.population=self.TriListePopulation(self.population)
    #     #cut self.population pour garder nbIndividuGarde
    #     #compléte la population
        

    def regeneration_population(self,nbIndividuGarde,mapopulation):
    
        TaillePopulation=mapopulation.nTaillePopulation
        print("La taille est:",TaillePopulation)
        if nbIndividuGarde<TaillePopulation :
            PerfPop=[]
            for indice in range(TaillePopulation):
                PerfPop.append(mapopulation.population[indice])
                
            ListeTriee=Population.TriListePopulation(PerfPop,PerfPop)
            IndividuGarde=ListeTriee[0:nbIndividuGarde+1]
            for i in range(10):
#                print("Les perf non triées",PerfPop[i].performance)
                print("La liste :",ListeTriee[i].performance)
#                print("\n")
#def mini_pop(self,liste_indiv):
#    for i in range(len(liste_indiv)):
#        self.individus.append(Individu(liste_indiv[i].TriListePopulation(self.population)))
    def GenAleatoire(self,codage):
        NewPop=[]
        for index in range(self.gestionPopulation):
            NewPop.append((self.gestionPopulation[index][1]-self.gestionPopulation[index][0])+self.gestionPopulation[index][0])
        new_individu=Individu(NewPop,codage)
        self.population.append(new_individu)
        print(new_individu)
    
    
    
    
    
#    def pop_regeneree(self,mapopulation):
#        TaillePopulation=mapopulation.nTaillePopulation
#        NewPop=[]
#        NewPop=IndividuGarde
#        for index in range (11,TaillePopulation):
#            NewPop.append(Individu(self.gestionPopulation[index]))
#        for j in range(TaillePopulation):
#            print(Newpop[j])
         
#####################################################################################################     
                    
if __name__ == '__main__':      
    
    monCodage=CodageMantisse(32,6)
    NbIndividuDansPopulation=50
    zone=[{"min":-100,"max":-10},{"min":10,"max":100},{"min":10,"max":100},{"min":10,"max":100},{"min":10,"max":100}]

    monCrossOver=CrossOverMultiPoints()
    monEvaluation=EvaluationF1SumSquare()
    maSelection=SelectionRoueDeLaFortune()          
    
    
    gestionPopulation=GestionPopulation(monCodage,zone,monCrossOver,monEvaluation,0)  
    maPopulation=Population(NbIndividuDansPopulation,gestionPopulation)  
    Test=GestionPopulation.regeneration_population(10,10,maPopulation)
    # maPopulation.AffichePopulation()
   
#    parentsIndex=maSelection.tirageIndex(maPopulation.population)
#    parents=[]
#    parents
#    parents.append(maPopulation.population[parentsIndex[0]])
#    parents.append(maPopulation.population[parentsIndex[1]])
#    nbPoints = 3
#  
#    enfants = CrossOverMultiPoints.BrassageMultiPoints(parents,parents, gestionPopulation, nbPoints)
#    # print('parent1 base = :',parents[0].genetique)
#    # print('parent2 base = :',parents[1].genetique)
#    
#    # print('\n')
#    # print("Le code de l'enfant 1 individu est :",enfants[0].genetique )
#   
#    # print("Le code de l'enfant 2 individu est :",enfants[1].genetique )