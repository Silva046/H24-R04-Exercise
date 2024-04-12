class Employe: 
    def __init__(self, id:int, nom:str, prenom:str, role:int, salaire:int) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.role = role
        self.salaire = salaire

class Programmeur(Employe):
    def __init__(self, id: int, nom: str, prenom: str, role: int, salaire: int, _langages:list[str]) -> None:
        super().__init__(id, nom, prenom, role, salaire)
        self._langages = _langages
    @property
    def langages_connus(self):
        return self._langages
    @langages_connus.setter
    def langages(self, nvx_langage):
        self._langages.append(nvx_langage)


class Designer(Employe):
    def __init__(self, id: int, nom: str, prenom: str, role: int, salaire: int, liste_artefacts:list) -> None:
        super().__init__(id, nom, prenom, role, salaire)
        self.liste_artefacts = []

    def __dessiner():
        pass

class Tech_Reseau(Employe):
    def __init__(self, id: int, nom: str, prenom: str, role: int, salaire: int, liste_interventions:list[str]) -> None:
        super().__init__(id, nom, prenom, role, salaire)
        self.liste_interventions = []

    def __intervenir():
        pass