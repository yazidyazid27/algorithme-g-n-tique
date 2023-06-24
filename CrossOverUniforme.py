# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:14:55 2021

@author: farnierl
"""

from CodageMantisse import *
from CodageGray import *
from Population import *
from GestionPopulation import *
from CrossOverUnPoint import *
from CrossOverMultiPoints import *
from Individu import *
from EvaluationF1SumSquare import *
from Selection import *
from SelectionRoueDeLaFortune import *
import random as rd

class CrossOverUniforme(CrossOver) :
    def __init__(self):
        pass 
    
    def BrassageUniforme(self,parents,gestionPopulation):
#=============================INITIALISATION============================================
#        print('On entre dans la fonction')
        # Les Enfants (individu)
        Enfant1 = []
        Enfant2 = []
        
        # La definition de la genetique des parents (tableau de tableaux de chaines)
        parent1 = parents[0].genetique
        parent2 = parents[1].genetique
        
        
        # Le code des enfants issues du cross over du code des parents (tableau de tableaux de chaines)
        CodeEnfant1=[]  
        CodeEnfant2=[]
        
        
#====================Boucle de parcours des coordonnées des parents===================
        for i in range(gestionPopulation.dimensionIndividu):
            CodeCoordonnee_i_Enfant1 = []
            CodeCoordonnee_i_Enfant2 = []
#            print('i = ', i,'\n')
#===============Boucle de parcours des tableaux du codage de chaque coordonnees des parents=======
            for k in range(len(parent1[0])):
##                print('k = ', k,'\n')
#                print('parent1 : ', parent1[i][k])
#                print('parent2 : ', parent2[i][k])
                CodeCoordonnee_i_Emplacement_k_Enfant1 =''
                CodeCoordonnee_i_Emplacement_k_Enfant2 =''
                
                
#============Boucle de parcours de la chaine du codage de la i eme Coordonnee Emplacement k des parents=== 
                for j in range((len(parent1[0][k]))-1):
                    
                    u = rd.uniform(0,1)
#                    print('u = ', u) 
                    if u<1/2: 
#                        print('\n','codeE1 = codeE1+codeP2','codeE2 = codeE2+codeP1','\n')
                        CodeCoordonnee_i_Emplacement_k_Enfant2+=parent1[i][k][j:j+1]
                        CodeCoordonnee_i_Emplacement_k_Enfant1+=parent2[i][k][j:j+1]
                    elif u>=1/2 :
#                        print('\n','codeE1 = codeE1+codeP1','codeE2+codeP2','\n')
                        CodeCoordonnee_i_Emplacement_k_Enfant2+=parent2[i][k][j:j+1]
                        CodeCoordonnee_i_Emplacement_k_Enfant1+=parent1[i][k][j:j+1]
                        
                        
                        
#                    print('Le codeP1 = ',parent1[i][k][j:j+1])
#                    print('Le codeP2 = ',parent2[i][k][j:j+1])
#                    print('\n')
#                    print('Le codeEnfant1 vaut : ', CodeCoordonnee_i_Emplacement_k_Enfant1)
#                    print('Le codeEnfant2 vaut : ', CodeCoordonnee_i_Emplacement_k_Enfant2)
                # Concatenation du code de la coordonnee i  
                CodeCoordonnee_i_Enfant1.append(CodeCoordonnee_i_Emplacement_k_Enfant1)
                CodeCoordonnee_i_Enfant2.append(CodeCoordonnee_i_Emplacement_k_Enfant2)
                
            # Concatenation du code de l'individu entier
            CodeEnfant1.append(CodeCoordonnee_i_Enfant1)
            CodeEnfant2.append(CodeCoordonnee_i_Enfant2)
            
#        print("Le code de l'enfant 1 issue du cross over est :",CodeEnfant2)
#        print("Le code de l'enfant 2 issue du cross over est :",CodeEnfant1)
            
            
#============================Creation des individus Enfants==================================================            
        CoordonneeEnfant1=gestionPopulation.codage.decode(CodeEnfant1)
        CoordonneeEnfant2=gestionPopulation.codage.decode(CodeEnfant2)
        
        Enfant1 = Individu(gestionPopulation,CoordonneeEnfant1)
        Enfant2 = Individu(gestionPopulation,CoordonneeEnfant2)
        return[Enfant1,Enfant2]
        
                
                
                
                
if __name__ == '__main__':      
    
    monCodage=CodageMantisse(32,6)
    NbIndividuDansPopulation=2
    zone=[{"min":-100,"max":-10},{"min":10,"max":100}]#,{"min":10,"max":100},{"min":10,"max":100},{"min":10,"max":100}]

    monCrossOver=CrossOverUniforme()
    monEvaluation=EvaluationF1SumSquare()
    maSelection=SelectionRoueDeLaFortune()          
    
    
    gestionPopulation=GestionPopulation(monCodage,zone,monCrossOver,monEvaluation,0)  
    maPopulation=Population(NbIndividuDansPopulation,gestionPopulation)  
  
#    maPopulation.AffichePopulation()
   
    parentsIndex=maSelection.tirageIndex(maPopulation.population)
    parents=[]
    parents
    parents.append(maPopulation.population[parentsIndex[0]])
    parents.append(maPopulation.population[parentsIndex[1]])
#    nbPoints = 3
  
    enfants = CrossOverUniforme.BrassageUniforme(parents,parents,gestionPopulation)          
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                