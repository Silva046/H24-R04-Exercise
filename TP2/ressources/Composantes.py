#TP2 par ........
#
from abc import ABC,abstractmethod
import subprocess as sb

from ressources.AdresseIP import AdresseIP
if __name__ == '__main__' : from AdresseIP import *
else :                      from .AdresseIP import *

class Composante(ABC):
    def __init__(self, nom:str, adresse_ip:AdresseIP, masque_sous_reseau:AdresseIP, adresse_passerelle:AdresseIP, location_physique:str) -> None:
        super().__init__()
        self._nom = nom
        self._adresse_ip = adresse_ip(AdresseIP)
        self._masque_sous_reseau = masque_sous_reseau(AdresseIP)
        self._adresse_passerelle = adresse_passerelle(AdresseIP)
        self.location_physique = location_physique

    #droit de lecture pour nom
    @property
    def nom(self):
        return self._nom
    
    #droit de lecture et d'écriture pour adresse_ip
    @property
    def adresse_ip(self):
        return self._adresse_ip
    @adresse_ip.setter
    def adresse_ip(self, new_ip_addresse:str):
        self._adresse_ip = AdresseIP(new_ip_addresse)

    #droit de lecture et d'écriture pour masque_sous_reseau
    @property
    def masque_sous_reseau(self):
        return self._masque_sous_reseau
    @masque_sous_reseau.setter 
    def masque_sous_reseau(self, new_masque_sous_reseau:str):
        self._masque_sous_reseau = AdresseIP(new_masque_sous_reseau)

    #droit de lecture et écriture pour adresse_passerelle
    @property
    def adresse_passerelle(self):
        return self._adresse_passerelle
    @adresse_passerelle.setter 
    def adresse_passerelle(self, new_adresse_passerelle:str):
        self._adresse_passerelle = AdresseIP(new_adresse_passerelle)

    def ping(self):
        try: 
            sb.check_output( ['ping', '-n', '1', str(self.adresse_ip.valeur)], stderr=sb.STDOUT )
            return True
        except sb.CalledProcessError: 
            return False
        
    @abstractmethod
    def fermer(self):pass


        

class Poste(Composante):
    def __init__(self, nom:str, adresse_ip:AdresseIP, masque_sous_reseau:AdresseIP, adresse_passerelle:AdresseIP, location_physique:str) -> None:
        super().__init__(nom, adresse_ip, masque_sous_reseau, adresse_passerelle, location_physique)
        self.est_allume = False
        
    def ouvrir(self):
        # assumez qu'on envoie un signal de s'allumer.... à implanter une autre session.
        if self.est_allume : print("Station déjà ouvert.")
        self.est_allume = True
        
    def fermer(self):
        # assumez qu'on envoie un signal de se fermer.... à implanter une autre session.
        if self.est_allume == False: print ("Station déjà éteinte.")
        self.est_allume = False

class Routeur(Composante):
    def __init__(self, nom: str, adresse_ip: AdresseIP, masque_sous_reseau: AdresseIP, adresse_passerelle: AdresseIP, location_physique: str, nb_ports:int, ls_connexions:list[Composante]=[]) -> None:
        super().__init__(nom, adresse_ip, masque_sous_reseau, adresse_passerelle, location_physique)
        self._nb_ports = nb_ports
        self._ls_connexions = ls_connexions

    @property
    def nb_port(self):
        return self._nb_ports
    @property
    def ls_connexions(self):
        return self._ls_connexions
    
    def ajouter_connexions(self, composante_add:Composante):
        if composante_add not in self._ls_connexions and len(self._ls_connexions)<self._nb_ports:
            self._ls_connexions.append(composante_add)
        else: print("Le nombre de port maximal pour ce routeur ont étés atteint")
        #if isinstance(composante_add,Routeur)==True:


    def supprimer_connexion(self, composante_remove:Composante):
        if composante_remove in self._ls_connexions:
            self._ls_connexions.remove(composante_remove)

    def fermer(self):
        print("Cette instruction va fermer le courant vers le routeur.")
        reponse = input("Continuer ? (Y/N)")
        # instructions pour fermer le courant hors du cadre du TP2
    

