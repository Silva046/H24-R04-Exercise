from datetime import date


class Patient:
    def __init__(self, id:int, nom:str="inconnue", NAS:int|str="inconnue") -> None:
        self.id = id
        self.nom = nom
        self.NAS = NAS
        self.date_admission = None
class Departement:
    liste_departement = []
    def __init__(self, nom:str):
        self.nom = nom
        self._liste_patients = []
        Departement.liste_departement.append(self)

    @property
    def liste_patients(self):
        return self._liste_patients

    def ajouter_patient(self, patient:Patient):
        patient.date_admission = date.today()
        self._liste_patients.append(patient)
        if patient.nom == "inconnue":
            return print(f"le patient {patient.id} a bien été ajouté")
        else: return print(f"le patient {patient.nom} a bien été ajouté")

    @classmethod
    def imprimer_liste_des_patients(cls): 
        dep:Departement
        for dep in cls.liste_departement:
            print(f"Voici la liste des départements {dep.nom}")
            pat:Patient
            for pat in dep._liste_patients:
                print(f"\t{pat.id} {pat.nom} {pat.date_admission}")


if __name__ == "__main__" :
    p1, p2, p3 = Patient(1123,"Ana Tremblay",6431297), Patient(2345,"Johnatan Fitzbald"), Patient(3355)

    d1 = Departement("Oncologie")
    d1.ajouter_patient(p1)
    d2 = Departement("Urgence")
    d2.ajouter_patient(p2)
    d2.ajouter_patient(p3)

    Departement.imprimer_liste_des_patients()