# Voici une classe simple
from .constant import *

class Etudiant:
    
    def __init__(self, matricule, nom, age):
        self.matricule = matricule
        self.nom = nom
        self.age = age
        
class Groupe:
    
    def __init__(self, ls_etudiants):
        self._ls_etudiants = ls_etudiants
        
    @property
    def ls_etudiants(self):
        return self._ls_etudiants
    
      
    def ajouter_etudiant(self, etudiant):
        if (etudiant == None):
            raise ValueError("On ne peut pas ajouter un étudiant vide")
        if (len(self.ls_etudiants) == NB_MAX_ETUDIANTS):
            raise ValueError("On ne peut pas ajouter un étudiant car le groupe a déjà 3 etudiants")
        self.ls_etudiants.append(etudiant)
        
         
    