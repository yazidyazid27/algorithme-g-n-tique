# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from Individu import *
from Evaluation import *
import matplotlib.pyplot as plt 
import numpy as np
import math

class Population():
#    ListeIndividu=[]   faire operateur qui remplace 
    
    """ propriete"""
    
   
    
    
    def __init__(self,nTaillePopulation,aGestionPopulation):
        self.gestionPopulation=aGestionPopulation
        self.nTaillePopulation=nTaillePopulation
        self.population=[]
        self.MaxPopulation=[]
        self.MinPopulation=[]
        self.AxexMax=[]
        self.AxeyMax=[]
        self.AxexMin=[]
        self.AxeyMin=[]
        self.initPopulation()
        

    def initPopulation(self):
        for indexPopulation in range (self.nTaillePopulation):
            self.population.append(Individu(self.gestionPopulation))
#SERRA        self.population.append(Individu(self.gestionPopulation,[0,1,2,3]))
   
    def AffichePopulation(self):
        for individu in self.population:
            print (individu)
        
        
    def TaillePopulation(self):
        return "LA TAILLE DE LA POPULATION EST : " + str(len(self.population))
    
    def TriListePopulation(self,ListeAtrier):
        L = list(ListeAtrier) # copie de la liste
        N = len(L)
        for n in range(1,N):
            cle = L[n]
            j = n-1
            while j>=0 and L[j].performance > cle.performance:
                L[j+1] = L[j] # decalage
                j = j-1
                L[j+1] = cle
        #print("L=",L)
        return L
    
    def AffichePlusFaible(self):
        populationTriee=self.TriListePopulation(self.population)
        return(populationTriee[0])
        
    
    
    def RemplacerIndividu(self,ListeParents,ListeFils):
        
        if len(ListeFils)!=0:
            ListeIndividusTotales=[]
            parent1=ListeParents[0]
            parent2=ListeParents[1]
            indiceParent1=self.population.index(parent1)
            indiceParent2=self.population.index(parent2)
            ListeIndividusTotales=[]
            ListeIndividusTotales.append(ListeParents[0])
            ListeIndividusTotales.append(ListeParents[1])
            ListeIndividusTotales.append(ListeFils[0])
            ListeIndividusTotales.append(ListeFils[1])
            # print("________________population parentFils__________________________")
            # for indice in range(0,len(ListeIndividusTotales)):
            #     print(indice)
            #     print(ListeIndividusTotales[indice].performance)
            
            #print(ListeIndividusTotales)
            
            ListeIndividusTotales=self.TriListePopulation(ListeIndividusTotales)
            # print("________________population triée__________________________")
            # for indice in range(0,len(ListeIndividusTotales)):
            #     print(indice)
            #     print(ListeIndividusTotales[indice].performance)
                
            
            # print("-------------------------type d'optimisation---------------")
            # print(self.gestionPopulation.typeOptimization)
            if self.gestionPopulation.typeOptimization==0:
                
                PerfMax1=ListeIndividusTotales[0]
                PerfMax2=ListeIndividusTotales[1]
                # print(PerfMax1)
                # print(PerfMax2)
                
            else:
                PerfMax1=ListeIndividusTotales[len(ListeIndividusTotales)-1]
                PerfMax2=ListeIndividusTotales[len(ListeIndividusTotales)-2]
                
                
            ListeParents=[]
            ListeParents.append(PerfMax1)
            ListeParents.append(PerfMax2)
            for j in range (0,len(ListeParents)):
                if ListeParents[j]==parent1:
                    self.population[indiceParent1]=ListeParents[j]
                elif ListeParents[j]==parent2:
                    self.population[indiceParent2]=ListeParents[j]
                else:
                    self.population[indiceParent1]=PerfMax1
                    self.population[indiceParent2]=PerfMax2
            ListeIndividusTotales=self.TriListePopulation(self.population)
            # self.MinPopulation.append(math.log(ListeIndividusTotales[0].performance))
            # self.MaxPopulation.append(math.log(ListeIndividusTotales[len(ListeIndividusTotales)-1].performance))   
            self.MinPopulation.append(ListeIndividusTotales[0].performance)
            self.MaxPopulation.append(ListeIndividusTotales[len(ListeIndividusTotales)-1].performance)
            
            return(ListeParents)
            
                
    def TracerGraphique(self):
            
            for p in range(0,len(self.MaxPopulation)-1):
                self.AxexMax.append(p)
                self.AxeyMax.append(self.MaxPopulation[p])
            for i in range(0,len(self.MinPopulation)-1):
                self.AxexMin.append(i)
                self.AxeyMin.append(self.MinPopulation[i])   
                
            # print(self.MaxPopulation)
            # print(self.MinPopulation)
            
            plt.plot(self.AxexMax,self.AxeyMax,label="performance max")
            plt.plot(self.AxexMin,self.AxeyMin,label="performance min")
            plt.legend()
            
            plt.yscale("log")
            plt.xlabel("Iterations")
            plt.ylabel("Performance")
            plt.title("CONVERGENCE DE L'ALGO GENETIQUE",fontsize=25)
           
            
            plt.show()
            

            
            
        
        
    
#    def SupprimeIndividu(nIndex):
#        ListeIndividu.remove(nIndex)
    