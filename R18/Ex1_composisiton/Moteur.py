class Moteur:
    def __init__(self, puissance) -> None:
        self.puissance = puissance

    def demarrer(self):
        pass

class Moteur_Essence(Moteur):
    def __init__(self, puissance, nbr_cylindre:int) -> None:
        super().__init__(puissance)
        self.nbr_cylindre = nbr_cylindre

class Moteur_Electrique(Moteur):
    def __init__(self, puissance, amperrage) -> None:
        super().__init__(puissance)
        self.amperrage = amperrage
