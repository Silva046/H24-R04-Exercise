from Reservoir import *
from Moteur import *
class Voiture :
    def __init__(self, pPrix:int, pMoteur:Moteur, pReservoir:Reservoir) -> None:
        self.pPrix = pPrix
        self.pMoteur = pMoteur
        self.pReservoir = pReservoir 