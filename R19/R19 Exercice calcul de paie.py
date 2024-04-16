#Voyez l'énoncé R20 Exercice 2 Calculer_paie.docx

#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    pass
            
class Employe(ABC):
    pass
    
class Employe_salarie(Employe):
    pass
 
class Employe_heure(Employe):  
   pass
    
class Employe_Commission(Employe_salarie):  
    pass
 


#instanciation des objets 
if __name__ == "__main__": pass
    