#-	Les postes de travail ont une propriété ‘utilisation’ qui est une indication pour savoir quels logiciels doivent être installés sur ce poste. Pour cet exercice, nous allons avoir les valeurs : ‘info’, ‘info_réseau’ et ‘info_prog’
#       o	Les logiciels ‘info’ sont installés dans tous les postes de travail.
#       o	Les logiciels ‘info-réseau’ seront installés sur les postes de travail ayant cette utilisation…
#-	Le poste de travail d’un professeur aura tous les logiciels, d’où son utilisation ‘*’.

#-	Vous trouverez ci-joint une liste de logiciels  « logiciels2022_2023.csv » qui comprends les logiciels à  installer sur les postes de travail du département informatique, avec une indication si chaque logiciel est installé pour les 2 voies de sortie du département ou pour une voie de sortie spécifique.
#-	Chacun des postes de travail n’a aucun logiciel d’installés pour le moment.

# Tous les ordniateurs ont le même processeur et la même mémoire vive.
# Certain poste de travail PEUVENT avoir des valeurs différentes de processeur ou de mémoire_vive.
#       un attribut self.processeur est crée uniquement si une valeur autre que None est passé au constructeur.
import os
import csv
os.chdir(os.path.dirname(__file__))
class Ordinateur:
    processeur="Ryzen 3600"
    memoire_vive="16Go"
    def __init__(self,ID, adresseIP) -> None:
        self.ID = ID
        self.adresseIP = adresseIP
    
    def __str__(self) -> str:
        pass
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        cls.processeur = nouveau_processeur
    
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        cls.memoire_vive = nouvelle_norme
    
   
class Poste_de_travail(Ordinateur):
    def __init__(self,ID, adresseIP, utilisation,processeur="Ryzen 3600", memoire_vive="16Go") -> None:
        super().__init__(ID, adresseIP)
        self.liste_logiciels = []
        self.utilisation = utilisation
        self.__ajout_logiciel()
        self.processeur = processeur
        self.memoire_vive = memoire_vive

    def __ajout_logiciel(self):
            with open("logiciels2022_2023.csv", "r",encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file,delimiter=";")
                next(csv_reader)
                for donnee in csv_reader:
                    utils = donnee[2]
                    if self.utilisation == utils:
                        self.liste_logiciels.append(utils)
    
    # ajoute un str ou list de str à logiciels
    def installer_logiciel(self,logiciel,version) -> None:
        if logiciel and version not in self.liste_logiciels:
            self.liste_logiciels.append(logiciel + version)
    
    def desinstaller_logiciel(self,logiciel,version) -> None:
        if logiciel and version in self.liste_logiciels:
            self.liste_logiciels.remove(logiciel + version)
    
    def imprimer_liste_logiciels(self) -> None:
        print (self.liste_logiciels)
    

professeur1 = Poste_de_travail('LPFINFOPORT001','192.168.221.21','*',None,"32Go")

réseau = Poste_de_travail('LLBINFO060208','192.168.219.21','info-réseau')

prog = Poste_de_travail('LLBINFO060505','192.168.220.17','info-prog')