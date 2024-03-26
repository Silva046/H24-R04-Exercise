class Personne:
    def __init__(self,nom,prenom,date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

class Employe(Personne):
    def __init__(self, nom, prenom, date_naissance,NAS,poste,salaire) -> None:
        super().__init__(nom, prenom, date_naissance)
        self.NAS = NAS
        self.poste = poste
        self.salaire = salaire
    def __str__(self) -> str:
        return f"{self.prenom}, {self.nom}"
    def __repr__(self) -> str:
        return f"class:{type(self)}" + str(self)

class Realisateur(Employe):
    def __init__(self, nom, prenom, date_naissance, NAS, salaire,bonus) -> None:
        super().__init__(nom, prenom, date_naissance, NAS, "Realisateur", salaire)
        self.bonus = bonus

class Acteur(Employe):
    def __init__(self, nom, prenom, date_naissance, NAS, salaire,role) -> None:
        super().__init__(nom, prenom, date_naissance, NAS, "Acteur", salaire)
        self.role = role

class film:
    def __init__(self,nom,date_sortie,liste_employe:list=[]) -> None:
        self.nom = nom
        self.liste_employe = liste_employe
        self.date_sortie = date_sortie

james_cameron = Realisateur("Cameron","James","16 Août 1954",2444,"120 000 000$","200 000$")

richter_adolf = Acteur("Richter","Adolf","20 Avril 1889","6666","200 000$","principal")
neuil_brasfort = Acteur("brasfort","neuil","9 Septembre 1946",5836,"34365423675$","Principal")
mere_ta = Acteur("mère","ta","2000 BC",6385,"452435375441663452$","principal")

employé1 = Employe("employé","1","2 juin 3008",9876,"employé","363826$")
employé2 = Employe("employé","2","2 juin 3009",9876,"employé","35682$")
employé3 = Employe("employé","3","2 juin 3010",9876,"employé","3682$")

titanic = film("Titanic","19 Décembre 1997",[james_cameron,employé1,richter_adolf])
abyss = film("Abyss","9 Août 1989",[james_cameron,employé2,neuil_brasfort])
avatar = film("Avatar","18 Décembre 2009",[james_cameron,employé3,mere_ta])

print(james_cameron.__dict__)
print(richter_adolf.__dict__)
print(neuil_brasfort.__dict__)
print(mere_ta.__dict__)
print(avatar.liste_employe)