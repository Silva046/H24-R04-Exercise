from .Employe import Employe
import datetime

class Equipe:
    def __init__(self, nom:str, employes:list[dict]) -> None:
        self.nom = nom
        self.employes = employes

    def ajouter_employe(self, nvx_employe:Employe):
        dict_employe = {"Employe": None, 
                        "date_debut" : None,
                        "date_fin": None}
        for personne in self.employes:
            if nvx_employe not in personne["Employe"]:
                personne["Employe"] = nvx_employe
                personne["date_debut"] = datetime.date.today()
        
    def enlever_employe(self,nom_employe:Employe):
        for personne in self.employes:
            if nom_employe == personne:
                personne["date_fin"] = datetime.date.today()

    def imprimer_employe(self):
        print(self.employes)

