from Voiture import *


# Toutes ces instructions devraient fonctionner sans lancer d'erreurs
moteur1 = Moteur(800)
moteur2= Moteur_Electrique(500,300)
voiture1 = Voiture(65000, moteur1, 150)
voiture2 = Voiture(7000, moteur2, 350)
voiture3 = Voiture(68500, 500, 100)

print(voiture2.reservoir)
print(voiture3.reservoir)


