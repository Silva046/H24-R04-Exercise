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
        #print(f"{self.marque} {self.modele} {self.annee} de couleur {self.couleur}, avec seulement {self.kilo} km. Pour un prix raisonnable de {self.prix}$ dans un état {self.etat}.")
        print(self.__dict__)

class Voiture_electrique(Voiture):
    def __init__(self, marque, modele, annee, kilo, couleur, prix, autonomie_max, autonomie_actuelle, type_recharge, etat="neuf"):
        super().__init__(marque, modele, annee, kilo, couleur, prix, etat)
        self.autonomie_max = autonomie_max
        self.autonomie_actuelle = autonomie_actuelle
        self.type_recharge = type_recharge
    
    def recharger(self,type_de_recharge,nb_temps_sur_charge):
        if self.autonomie_actuelle < self.autonomie_max:
            if type_de_recharge == "Niveau 2":
                self.autonomie_actuelle += ((nb_temps_sur_charge / 120)* 40)
            elif type_de_recharge == "Rapide(100kw)":
                self.autonomie_actuelle += ((nb_temps_sur_charge / 8)* 40)
            elif type_de_recharge == "Rapide(300kw)":
                self.autonomie_actuelle += ((nb_temps_sur_charge / 2)* 40)
        elif self.autonomie_actuelle >= self.autonomie_max:
            self.autonomie_actuelle == self.autonomie_max
            
        

toyota = Voiture("Toyota", "Tercel", "1972", "1288888", "rouge", "123", "superbe")

print(toyota.imprimer_infos())