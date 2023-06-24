# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


from CodageMantisse import *
from Population import *
from GestionPopulation import *
from CrossOverUnPoint import *
from Individu import *
from Evaluation import *
from Selection import *
from SelectionRoueDeLaFortune import *



from CrossOver import *

#from Codage import *

from GestionPopulation import *

from Individu import *
import random as rd
from CodageMantisse import *
from Mute import *

class Mutation(Mute):
    
    def __init__(self):
        pass
    
    
    def inverse(enfants,taux,gestionPopulation):
        NewEnfant1 = []
        NewEnfant2 = []
        
        MantisseExposantNewEnfant1 = []
        MantisseExposantNewEnfant2 = []
        
        CoordonneeNewEnfant1 = []
        CoordonneeNewEnfant2 = []
        
        enfant1 = enfants[0]
        enfant2 = enfants[1]
        
        if taux == 0.5: #round(np.random.uniform(0,1),2):
            for i in range(gestionPopulation.dimensionIndividu):
                tailleMantisse = len(enfant1.genetique[i][0])-1
                tailleExposant = len(enfant1.genetique[i][1])-1
                
                CropMantisse = rd.randint(1,tailleMantisse)
                CropExposant = rd.randint(1,tailleExposant)
                
                codeNewEnfant1 = [enfant1.genetique[i][0][0:tailleMantisse-1]+enfant1.genetique[i][0][-1:-(tailleMantisse-1):-1],enfant1.genetique[i][1]]
                codeNewEnfant2 = [enfant2.genetique[i][0][0:tailleMantisse-1]+enfant2.genetique[i][0][-1:-(tailleMantisse-1):-1],enfant2.genetique[i][1]]
                
                MantisseExposantNewEnfant1.append(codeNewEnfant1)
                MantisseExposantNewEnfant2.append(codeNewEnfant2)
                
            CoordonneeNewEnfant1=gestionPopulation.codage.decode(MantisseExposantNewEnfant1)
            CoordonneeNewEnfant2=gestionPopulation.codage.decode(MantisseExposantNewEnfant2)    
            
            NewEnfant1 = Individu(gestionPopulation,CoordonneeNewEnfant1)
            NewEnfant2 = Individu(gestionPopulation,CoordonneeNewEnfant2)
            
            return [NewEnfant1,NewEnfant2]
            
       
        
        
#class CrossOverUnPoint(CrossOver) :        
    