class Chien:
    def __init__(self,pNom,pAge,pRace) -> None:
        self.nom = pNom
        self.age = pAge
        self.race = pRace


if __name__ == '__main__' :
    # Commentez et décommentez les instanciations pour vérifier votre code

    c1 = Chien("Fido",30,"Poodle") # Doit raise ValueError avec message : "Age trop élevé"
    c2 = Chien('Fi',11,"Berger Allemand") # Doit raise ValueError avec message : "Nom trop court"
    c3 = Chien(("Fido"),12,"Poodle") # Doit raise TypeError
    c4 = Chien("Fido",30,{'race':"Poodle"}) # Doit raise TypeError
    c5 = Chien("Fido",-3,"Poodle") # Doit raise ValeurNégative
