# Faites la classe Employe telle que décrite dans l'énoncé.

class Employe : 
    def __init__(self, nom:str, taux:float, temps_plein:bool=True) -> None:
        self.nom = nom
        self.taux = taux
        self.temps_plein = temps_plein


    def calculer_salaire(self):
        if self.temps_plein == True:
            return round(self.taux * 2000,2)
        else: return round(self.taux * 1200,2)


if __name__ == '__main__' :
    e1, e2, e3 = Employe("Steve", 18.55), Employe("Ana", 17.98, True), Employe("Bob", 21.58, temps_plein=False)
    for employe in [e1,e2,e3] : 
        print(f"{employe.nom} à un salaire annuel de {employe.calculer_salaire()}$")