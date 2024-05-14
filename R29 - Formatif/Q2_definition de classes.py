# Finissez ces classes :
from datetime import date
import datetime

class Personne:pass


if __name__ == "__main__" :
    p1 = Personne("Steve", "Charest", 9843,date(1982,6,19))
    p1.id = "68436"
    p2 = Personne("Anna", "Tremblay", "6842",date(1999,1,29))
    p2.id = 468432
    print(f"Employe {p1.id} : {p1.nom}")
    print(f"Employe {p2.id} : {p2.nom}")