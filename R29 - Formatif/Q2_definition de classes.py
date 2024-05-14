# Finissez ces classes :
from datetime import date
import datetime

class Personne:
    def __init__(self, nom:str, prenom:str, id:int, date_de_naissance:datetime) -> None:
        self._nom = nom
        self._prenom = prenom
        self._id = id
        self.date_de_naissance = date_de_naissance

    @property
    def nom(self):
        return f"{self._nom} {self._prenom}"
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,new_id):
        self._id = int(new_id)


if __name__ == "__main__" :
    p1 = Personne("Steve", "Charest", 9843,date(1982,6,19))
    p1.id = "68436"
    p2 = Personne("Anna", "Tremblay", "6842",date(1999,1,29))
    p2.id = 468432
    print(f"Employe {p1.id} : {p1.nom}")
    print(f"Employe {p2.id} : {p2.nom}")