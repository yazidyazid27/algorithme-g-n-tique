# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:19:25 2021

@author: kwarg
"""

from Selection import *
from CrossOver import *

class Mute :
    def __init__(self,enfants,taux):
        self.taux = taux
        self.enfant1 = enfants[0]
        self.enfant2 = enfants[1]
        self.NewEnfant1 = []
        self.NewEnfant2 = []
    