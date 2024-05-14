# Faites la classe Employe telle que décrite dans l'énoncé.

class Employe : pass


if __name__ == '__main__' :
    e1, e2, e3 = Employe("Steve", 18.55), Employe("Ana", 17.98, True), Employe("Bob", 21.58, temps_plein=False)
    for employe in [e1,e2,e3] : 
        print(f"{employe.nom} à un salaire annuel de {employe.calculer_salaire()}$")