from .Banque import Banque
from .Terrain import Terrain

class Joueur:
    def __init__(self,nom) -> None:
        self.nom = nom
        self.list_terrain = []
    #def acheter(self,proprietaire:Banque,terrain:Terrain): # indique que les variables passée doit êtres de types spécifiques 
    #    pass