from os import chdir
from os.path import dirname
from csv import reader
from .Terrain import Terrain

class Banque:
    _existe_deja = False    # Le '_' au début de la variable indique qu'il s'agit d'une variable privé.
    def __init__(self) -> None:
        if Banque._existe_deja == True :
            print("ERREUR, une instance de Banque existe déjà.")
        else :
            # Dans cette section, nous allons initialiser l'instance de banque.
            # Vous devez crée les attributs d'instances et leurs donnée une valeur
            self.terrains = []
            self._charger_terrains(self)
            Banque._existe_deja = True
    
    def _charger_terrains(self, path) :
        chdir(dirname(__file__))
        with open("../Data/terrains.csv") as f_lu :
            csv_reader = reader(f_lu)
            next(csv_reader)
            for l in csv_reader:
                new_terrain = Terrain(l[0],l[1],l[2],"","","","")
                self.terrains.append(new_terrain)



    def __repr__(self) -> str:
        return "oaweijroiwerj"