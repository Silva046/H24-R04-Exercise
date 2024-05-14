# Voici une classe simple
from .constant import *

class Thermostat:
    
    def __init__(self):
        self._temperature = TEMPERATURE_INITIALE
        
    @classmethod
    def from_temperature(cls, nouvelle_temperature):
        nouveau_Thermostat = cls()
        nouveau_Thermostat.temperature = nouvelle_temperature
        return nouveau_Thermostat

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, valeur):
        if (valeur < MIN_TEMPERATURE) or (valeur > MAX_TEMPERATURE):
            raise ValueError("La valeur soit être entre 5 et 35 deg. celsius")
        self._temperature=valeur
     
    def augmenter_1_degre(self):
        if (self._temperature == MAX_TEMPERATURE):
            raise ValueError("Le thermostat est déjà au max de 35 deg. celsius")
        self._temperature += 1
        
    def diminuer_1_degre(self):
        if (self._temperature == MIN_TEMPERATURE):
            raise ValueError("Le thermostat est déjà au min de 5 deg. celsius")
        self._temperature -= 1          
    