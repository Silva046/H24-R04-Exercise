from .Equipe import *


class Departement:
    def __init__(self, nom:str, equipes:list[Equipe]) -> None:
        self.nom = nom
        self.equipes = []

    def ajouter_equipe(self):
        self.equipes.append(Equipe)