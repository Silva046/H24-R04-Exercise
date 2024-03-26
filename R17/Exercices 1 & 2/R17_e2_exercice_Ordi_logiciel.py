#-	Les postes de travail ont une propriété ‘utilisation’ qui est une indication pour savoir quels logiciels doivent être installés sur ce poste. Pour cet exercice, nous allons avoir les valeurs : ‘info’, ‘info_réseau’ et ‘info_prog’
#       o	Les logiciels ‘info’ sont installés dans tous les postes de travail.
#       o	Les logiciels ‘info-réseau’ seront installés sur les postes de travail ayant cette utilisation…
#-	Le poste de travail d’un professeur aura tous les logiciels, d’où son utilisation ‘*’.

#-	Vous trouverez ci-joint une liste de logiciels  « logiciels2022_2023.csv » qui comprends les logiciels à  installer sur les postes de travail du département informatique, avec une indication si chaque logiciel est installé pour les 2 voies de sortie du département ou pour une voie de sortie spécifique.
#-	Chacun des postes de travail n’a aucun logiciel d’installés pour le moment.

# Tous les ordniateurs ont le même processeur et la même mémoire vive.
# Certain poste de travail PEUVENT avoir des valeurs différentes de processeur ou de mémoire_vive.
#       un attribut self.processeur est crée uniquement si une valeur autre que None est passé au constructeur.


class Ordinateur:
    processeur=None
    memoire_vive=None
    def __init__(self,ID, adresseIP) -> None:
        pass
    
    def __str__(self) -> str:
        pass
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        pass
    
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        pass
    
   
class Poste_de_travail(Ordinateur):
    def __init__(self,ID, adresseIP, utilisation,processeur=None, memoire_vive=None) -> None:
        super.__init__(ID, adresseIP)
        self.liste_logiciels = []
        pass
    
    # ajoute un str ou list de str à logiciels
    def installer_logiciel(self,logiciel,version) -> None:
        pass 
    
    def desinstaller_logiciel(self,logiciel,version) -> None:
        pass 
    
    def imprimer_liste_logiciels(self) -> None:
        pass
    

