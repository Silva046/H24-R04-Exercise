from datetime import date


class Patient: pass

class Departement:
    def __init__(self): pass


    def ajouter_patient(self): pass


    def imprimer_liste_des_patients(cls): pass


if __name__ == "__main__" :
    p1, p2, p3 = Patient(1123,"Ana Tremblay",6431297), Patient(2345,"Johnatan Fitzbald"), Patient(3355)

    d1 = Departement("Oncologie")
    d1.ajouter_patient(p1)
    d2 = Departement("Urgence")
    d2.ajouter_patient(p2)
    d2.ajouter_patient(p3)

    Departement.imprimer_liste_des_patients()