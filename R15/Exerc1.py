class Personne:
    def __init__(self,nom,prenom,date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

class Joueur(Personne):
    def __init__(self, nom, prenom, date_naissance,no_chandail,position) -> None:
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position

class Équipes:
    nb_joueur_dans_ligue = 0
    def __init__(self,nom,liste_joueurs:list=[]) -> None:
        Équipes.nb_joueur_dans_ligue += len(liste_joueurs)
        self.nom = nom
        self.liste_joueurs = liste_joueurs

    def engager_joueur(self,joueur):
        self.liste_joueurs.append(joueur)
        Équipes.nb_joueur_dans_ligue += 1

    def éjecter_joueur(self,joueur):
        self.liste_joueurs.remove(joueur)
        Équipes.nb_joueur_dans_ligue -= 1

class Attaquant(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail,nb_tirs_au_but,nb_assistance) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, "Attaquant")
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistance = nb_assistance

    def compter_but(self):
        self.nb_tirs_au_but += 1

class Defenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail,nb_interceptions,nb_passes) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, "Defenseur")
        self.nb_interceptions = nb_interceptions
        self.nb_passes = nb_passes

class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail,nb_arrets,nb_tirs_essuyes) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail,"gardien")
        self.nb_arrets = nb_arrets
        self.nb_tirs_essuyes = nb_tirs_essuyes

    def arreter_tir(self):
        self.nb_arrets += 1

#joueur
gardien_Logan_Ketterer = Gardien("Ketterer","Logan","9 Novembre 1993",1,128,208)

defenseur_Zachary_Brault_Guillard = Defenseur("Brault-Guillard","Zachary","5 Mars 1991",15,32,44)

attaquant_Sunusi_Ibrahim = Attaquant("Ibrahim","Sunusi","1 Octobre 2002",14,23,44)

#équipe
equipe_CF_Montreal = Équipes("CF_Montreal",[gardien_Logan_Ketterer,defenseur_Zachary_Brault_Guillard])
equipe_CF_Montreal.engager_joueur([attaquant_Sunusi_Ibrahim])

print(gardien_Logan_Ketterer.date_naissance)
print(defenseur_Zachary_Brault_Guillard.date_naissance)
print(attaquant_Sunusi_Ibrahim.date_naissance)