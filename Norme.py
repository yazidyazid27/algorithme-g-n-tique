# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from math import sqrt
import numpy as np
from Evaluation import *
from Individu import *

class Norme:
    def __init__(self,cordonnees):
        self.cordonnees=cordonnees

    def calcule_norme(cordonnees):
        norme=0
        s=0
        for i in range(len(cordonnees)):
            s += cordonnees[i]**2
            norme += sqrt(s)
        return "la norme est"  +  str(norme)
    