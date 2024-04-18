#Voyez l'énoncé R20 Exercice 2 Calculer_paie.docx

#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    def afficher_paies(liste_employe:list=str):
        for employes in liste_employe:
            print(f"voici la paie de {employes} : {Employe.calculer_paie()}")

     
class Employe(ABC):
    def __init__(self, id_employe, nom) -> None:
        super().__init__()
        self.id_employe = id_employe
        self.nom = nom
    
    @abstractmethod
    def calculer_paie(self):
        pass
    
class Employe_salarie(Employe):
    def __init__(self, id_employe, nom, salaire_par_semaine:int) -> None:
        super().__init__(id_employe, nom)
        self.salaire_par_semaine = salaire_par_semaine

    def calculer_paie(self):
        return self.salaire_par_semaine
 
class Employe_heure(Employe):  
   def __init__(self, id_employe, nom, heures_travailles:int, taux_horaire:int) -> None:
       super().__init__(id_employe, nom)
       self.heures_travailles = heures_travailles
       self.taux_horaire = taux_horaire
   
   def calculer_paie(self):
       return self.heures_travailles * self.taux_horaire
    
class Employe_Commission(Employe_salarie):  
    def __init__(self, id_employe, nom, salaire_par_semaine:int, commission) -> None:
        super().__init__(id_employe, nom, salaire_par_semaine)
        self.commission = commission

    def calculer_paie(self):
        return self.salaire_par_semaine + self.commission
 

#test

employe_salaire = Employe_salarie(1,"Marc Tremblay",2100)
employe_heure = Employe_heure(2,"Pierre Jonhson",40,22)
employe_commission = Employe_Commission(3,"Luc Toupin",1400,600)
liste_des_employes = []
liste_des_employes.append(employe_salaire)
liste_des_employes.append(employe_heure)
liste_des_employes.append(employe_commission)
Systeme_de_paie.afficher_paies(liste_des_employes)
#instanciation des objets 
if __name__ == "__main__": pass
    