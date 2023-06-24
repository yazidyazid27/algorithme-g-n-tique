# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:54:06 2021

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

class CrossOverMultiPoints(CrossOver) :
    def __init__(self):
        pass 
    
    def BrassageMultiPoints(self,parents,gestionPopulation,nbPoints):
        
#=============================INITIALISATION============================================
        
        # Les Enfants (individu)
        Enfant1 = []
        Enfant2 = []
        
        # La definition de la genetique des parents (tableau de tableaux de chaines)
        parent1 = parents[0].genetique
        parent2 = parents[1].genetique
        # print('parent1 : ', parent1)
        # print('parent2 : ', parent2)
        
        # Le code des enfants issues du cross over du code des parents (tableau de tableaux de chaines)
        CodeEnfant1=[]  
        CodeEnfant2=[]
        
        
#====================Boucle de parcours des coordonnées des parents===================
        for i in range(gestionPopulation.dimensionIndividu):
            CodeCoordonnee_i_Enfant1 = []
            CodeCoordonnee_i_Enfant2 = []
            #print('i = ', i,'\n')
#===============Boucle de parcours des tableaux du codage de chaque coordonnees des parents=======
            for k in range(len(parent1[0])):
                # print('k = ', k,'\n')
                #Definition de la liste des indices du croisement 
                ListeIndicesCrossOver = [0,len(parent1[i][k])]
                nombreMaxPointsBrassages = min(nbPoints,len(parent1[i][k])//2) # pour gerer la difference de taille (ex: mantisse, exposant)
                # print('La longueur de la mantisse exposant = ', len(parent1[i][k]))
                ListeIndicesCrossOver+=rd.sample(range(1,len(parent1[i][k])-1),nombreMaxPointsBrassages) #generation aleatoire des indices de croisement
                ListeIndicesCrossOver = sorted(ListeIndicesCrossOver)  # tri des indices ordre croissant
                print('La longueur de la sequence de genes est : ', str(len(parent1[i][k])),'\n')
                print('La liste des indices de croisement tirés aléatoirement est : ',ListeIndicesCrossOver ,'\n')
                CodeCoordonnee_i_Emplacement_k_Enfant1 =''
                CodeCoordonnee_i_Emplacement_k_Enfant2 =''
                
                
#============Boucle de parcours de la chaine du codage de la i eme Coordonnee Emplacement k des parents=== 
                for j in range((len(ListeIndicesCrossOver))-1):
                    # print('j = ', j,'\n')
                    # Gestion du remplissage en quinconce du code des enfants  
                    # print('indice croisement = ', ListeIndicesCrossOver[j+1])
                    
#                    print('\n)
                    print('Le codeP1 correspond au code du parent1 entre les indices '+str(ListeIndicesCrossOver[j])+' et '+str(ListeIndicesCrossOver[j+1])+' de la séquence de genes.')
                    
                    print('La sequence de genes des parents valent : \nParent1 :', parent1[i][k],'\nParent2 :',parent2[i][k])
                    
                    if j%2!=0: 
#                        print('\n','codeE1 = codeE1+codeP2','codeE2 = codeE2+codeP1','\n')
                        CodeCoordonnee_i_Emplacement_k_Enfant2+=parent1[i][k][ListeIndicesCrossOver[j]:ListeIndicesCrossOver[j+1]]
                        CodeCoordonnee_i_Emplacement_k_Enfant1+=parent2[i][k][ListeIndicesCrossOver[j]:ListeIndicesCrossOver[j+1]]
                    elif j%2==0 :
#                        print('\n','codeE1 = codeE1+codeP1','codeE2+codeP2','\n')
                        CodeCoordonnee_i_Emplacement_k_Enfant2+=parent2[i][k][ListeIndicesCrossOver[j]:ListeIndicesCrossOver[j+1]]
                        CodeCoordonnee_i_Emplacement_k_Enfant1+=parent1[i][k][ListeIndicesCrossOver[j]:ListeIndicesCrossOver[j+1]]
                        
                        
                        
                    print('Le codeP1 = ',parent1[i][k][ListeIndicesCrossOver[j]:ListeIndicesCrossOver[j+1]])
                    print('Le codeP2 = ',parent2[i][k][ListeIndicesCrossOver[j]:ListeIndicesCrossOver[j+1]])
                    print('\n')
                    print('Le codeEnfant1 vaut : ', CodeCoordonnee_i_Emplacement_k_Enfant1)
                    print('Le codeEnfant2 vaut : ', CodeCoordonnee_i_Emplacement_k_Enfant2)
                # Concatenation du code de la coordonnee i  
                CodeCoordonnee_i_Enfant1.append(CodeCoordonnee_i_Emplacement_k_Enfant1)
                CodeCoordonnee_i_Enfant2.append(CodeCoordonnee_i_Emplacement_k_Enfant2)
                
            # Concatenation du code de l'individu entier
            CodeEnfant1.append(CodeCoordonnee_i_Enfant1)
            CodeEnfant2.append(CodeCoordonnee_i_Enfant2)
            
         
        # print("Le code de l'enfant 1 issue du cross over est :",CodeEnfant2)
        # print("Le code de l'enfant 2 issue du cross over est :",CodeEnfant1)
            
            
#============================Creation des individus Enfants==================================================            
        CoordonneeEnfant1=gestionPopulation.codage.decode(CodeEnfant1)
        CoordonneeEnfant2=gestionPopulation.codage.decode(CodeEnfant2)
        
        Enfant1 = Individu(gestionPopulation,CoordonneeEnfant1)
        Enfant2 = Individu(gestionPopulation,CoordonneeEnfant2)
        return[Enfant1,Enfant2]
        
                    
if __name__ == '__main__':      
    
    monCodage=CodageMantisse(32,6)
    NbIndividuDansPopulation=2
    zone=[{"min":-100,"max":-10},{"min":10,"max":100},{"min":10,"max":100},{"min":10,"max":100},{"min":10,"max":100}]

    monCrossOver=CrossOverMultiPoints()
    monEvaluation=EvaluationF1SumSquare()
    maSelection=SelectionRoueDeLaFortune()          
    
    
    gestionPopulation=GestionPopulation(monCodage,zone,monCrossOver,monEvaluation,0)  
    maPopulation=Population(NbIndividuDansPopulation,gestionPopulation)  
  
    # maPopulation.AffichePopulation()
   
    parentsIndex=maSelection.tirageIndex(maPopulation.population)
    parents=[]
    parents
    parents.append(maPopulation.population[parentsIndex[0]])
    parents.append(maPopulation.population[parentsIndex[1]])
    nbPoints = 3
  
    enfants = CrossOverMultiPoints.BrassageMultiPoints(parents,parents, gestionPopulation, nbPoints)
    # print('parent1 base = :',parents[0].genetique)
    # print('parent2 base = :',parents[1].genetique)
    
    # print('\n')
    # print("Le code de l'enfant 1 individu est :",enfants[0].genetique )
   
    # print("Le code de l'enfant 2 individu est :",enfants[1].genetique )
    
    
    print('\n','La performance des parents  sont : ',maPopulation.population[0].performance,'et',maPopulation.population[1].performance)
    
    print('\n')
    print('Les performances des enfants sont : ',enfants[0].performance, 'et ', enfants[1].performance )
    print('\n')
    maPopulation.RemplacerIndividu(parents,enfants)
    print('La performance des individus de la nouvelle population après RemplacerIndividu sont : ',maPopulation.population[0].performance,'et',maPopulation.population[1].performance)
    # maPopulation.AffichePopulation()
    print('\n')
    # print('les parents sont : ',parents)
    # print('les enfants sont : ',enfants)
    # print('\n')
    
    
    # print('Le code de la 1ere coordonnee du parent 1 est :',maPopulation.population[parentsIndex[0]].genetique[0])
    # print('Le code de la 1ere coordonnee du parent 2 est :',maPopulation.population[parentsIndex[1]].genetique[0])

    print("Les coordonnées de l'Enfant1 sont : ",enfants[0].coordonnees)