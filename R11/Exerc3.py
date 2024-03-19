class Voiture:
    def __init__(self, marque, modele, annee, kilo, couleur, prix, etat="neuf"):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilo = kilo
        self.couleur = couleur
        self.prix = prix
        self.etat = etat

    def imprimer_infos(self):
        print(f"{self.marque} {self.modele} {self.annee} de couleur {self.couleur}, avec seulement {self.kilo} km. Pour un prix raisonnable de {self.prix}$ dans un état {self.etat}.")


toyota = Voiture("Toyota", "Tercel", "1972", "1288888", "rouge", "123", "superbe")

print(toyota.imprimer_infos())