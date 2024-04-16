#TP2 par ........
#
from abc import ABC,abstractmethod
import subprocess as sb
if __name__ == '__main__' : from AdresseIP import *
else :                      from .AdresseIP import *

class Composante(ABC):
    pass

class Poste(Composante):
    def __init__():pass
        
    def ouvrir(self):
        # assumez qu'on envoie un signal de s'allumer.... à implanter une autre session.
        if self.est_allume : print("Station déjà ouvert.")
        self.est_allume = True
        
    def fermer(self):
        # assumez qu'on envoie un signal de se fermer.... à implanter une autre session.
        if self.est_allume == False: print ("Station déjà éteinte.")
        self.est_allume = False

class Routeur(Composante):
    def __init__(): pass
    
    def fermer(self):
        print("Cette instruction va fermer le courant vers le routeur.")
        reponse = input("Continuer ? (Y/N)")
        # instructions pour fermer le courant hors du cadre du TP2
    

