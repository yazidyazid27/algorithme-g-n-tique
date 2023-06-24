# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:47:20 2021

@author: choutriy
"""
import numpy as np
from Codage import Codage   
from sympy.combinatorics.graycode import gray_to_bin,bin_to_gray


class CodageGray(Codage):
    
    def __init__(self,precisionMantisse,precisionExposant,Gray=True):
        # super().__init__()
        self.precisionMantisse=precisionMantisse
        self.precisionExposant=precisionExposant
        self.Gray=Gray
    #------------------------------Codage--------------------------------
        
    def ecriture_scientifique(self,nombre):
        """
    
        Prend en argument un nombre et renvoie sa mantisse 
        et son exposant en écriture scientifique

        """
        if nombre == 0:
            #print("Nombre=",str(nombre), "Nombre_sc=", 0, "Exposant=",0)
            return 0,0
        exposant=np.floor(np.log10(np.abs(nombre)))
        nombre_sc=nombre/(10**exposant)
        #Décalage possible car 188.99/100 devient parfois 1.8899000000...01
        precision=len(str(np.abs(nombre)))
        #print("Nombre=",str(nombre), "Nombre_sc=", nombre_sc, "Exposant=",exposant)
        return round(nombre_sc,precision) , int(exposant)
        

           
    def remplissage_binaire(self,binaire,taille):
        """
        Rajoute des zéros à un nombre binaire et retire le '0b' 
        de début de chaîne
        Rajoute également un '+' en début de chaîne aux nombres positifs

        Parameters
        ----------
        binaire : 0bxxxx
            
        taille : Entier
            Taille souhaitée de la chaîne

        Returns
        -------
        binaire : 00..00xxxx

        """
        
        if binaire[0]!='-':
            binaire='+'+binaire
        
            
        binaire=binaire[0]+binaire[3:].zfill(taille)
        
        
        return binaire

          
       
    def code(self,nombres):
        """
        Prend en argument des nombres quelconques et renvoie en binaire 
        leurs mantisses et leurs exposants

        Parameters
        ----------
        nombres : Liste de nombres

        Returns
        -------
        codage : Liste de couples de binaires

        """
        codage=[]
        for i in nombres:
            nombre_sc , exposant = self.ecriture_scientifique(i)
                
                
            nombre_entier=int(nombre_sc*10**(len(str(nombre_sc))-2))
            #Décalage possible de 1 car 1.899 *1000 devient parfois 1898.99xxx
                
            while len(bin(nombre_entier)) -2 > self.precisionMantisse: 
                nombre_entier=nombre_entier//10
                    
            if len(bin(exposant)) -2 > self.precisionExposant:
                raise ValueError("Exposant trop grand (" +str(exposant)+") ou précision trop faible ("  + str(2**self.precisionExposant) +")")
            
            bin_n_ent=self.remplissage_binaire(bin(nombre_entier),self.precisionMantisse)
            bin_expo=self.remplissage_binaire(bin(exposant),self.precisionExposant)
            
            
                
            if self.Gray==True:
                
                bin_n_ent=bin_n_ent[0]+bin_to_gray(bin_n_ent[1:])
                bin_expo=bin_expo[0]+bin_to_gray(bin_expo[1:])
                
                
            codage.append([bin_n_ent,bin_expo])
            
        return codage  
    
    
    
    #------------------------------Décodage--------------------------------
    
    
    def reecriture_binaire(self,chaines):
        
        """
        Reformate les chaînes utilisées en selection en binaires
        
        Exemple:
        '+00010101'-->'0b00010101'

        """
        chaines_bin=[]
        for i in chaines:
            i=i[0]+'0b'+i[1:]
            chaines_bin.append(i)
            
        return chaines_bin
      
    
    def reecriture_decimale(self,nombre,exposant):
        
        """
        Prend un entier et un exposant et renvoie un flottant de même mantisse que l'entier
        et de même ordre de grandeur que l'exposant
        
        Exemple:
            (4523695,3)-->4523.695
            (562,-2)-->0.00562

        Parameters
        ----------
        nombre : Entier
        
        exposant : Entier
            Exposant du nombre attendu en sortie

        Returns
        -------
        nombre : Float


        """
        
        Cnombre=str(np.abs(nombre))
        
        s=np.sign(nombre)
        
        if exposant >= 0:
            
            Cnombre = Cnombre[0:exposant+1]+'.'+Cnombre[exposant+1:]
            
        
        else:
            Cnombre='0.'+Cnombre.zfill(len(Cnombre)-exposant-1)
            
        nombre=s*float(Cnombre)
        return nombre
    
    
    def decode(self,codage):
        """
        Prend en argument des couples de mantisses et exposants issus de selection
        et renvoie les nombres associés

        Parameters
        ----------
        codage : Liste de couples de 'pseudo-binaires' Ex: '+00001010'

        Returns
        -------
        nombres : Liste de flottants

        """
        nombres=[]
        
        for i in codage:
            
            
            if self.Gray==True:
                
                bin_entier=i[0]
                bin_expo=i[1]
                bin_entier=bin_entier[0]+gray_to_bin(bin_entier[1:])
                bin_expo=bin_expo[0]+gray_to_bin(bin_expo[1:])
                i=[bin_entier,bin_expo]
            
            i=self.reecriture_binaire(i)
            mantisse , exposant =int(i[0],2),int(i[1],2)
            nombres.append(self.reecriture_decimale(mantisse, exposant))
            
        return nombres

    #--------------------------------------------------------------------
    
    
    
    
if __name__ == '__main__':
    
    codageMantisse=CodageMantisse(32,6,Gray=True)
    e=[-1888.97899,3.57,1464,1899,3269.25,0,0.005642,15,85.6274276426724674657457645]   
    f=codageMantisse.code(e)
    g=codageMantisse.decode(f)
    
