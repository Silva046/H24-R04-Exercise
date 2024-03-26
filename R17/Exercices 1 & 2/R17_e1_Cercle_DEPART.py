#Vous avez une classe Cercle qui a un attribut privé rayon (_rayon)

#-	Ajoutez une propiété rayon qui retournera la valeur de rayon (avec le décorateur @property).
#-	Ajoutez le décorateur  @nom_de_la_propriété.setter  pour qu'un utilisateur de la classe puisse changer le rayon. 
#           Le rayon doit avoir une valeur positive plus grande que 0.
#-	Ajoutez le décorateur @nom_de_la_propriété.deleter pour qu'un utilisateur de la classe puisse supprimer le rayon.
#           Supprimer le rayon doit change la valeur de _rayon pour la mettre à 0 

#-	Instanciez un objet cercle de rayon de 45
#-	Imprimez son rayon
#-	Changez la valeur de son rayon
#-	Imprimez à nouveau son rayon.
#-	Supprimez le rayon de cet objet cercle
#-	Essayez maintenant d'obtenir son rayon. Il devrait être 0

#- supprimez l'attribut _rayon
#- essayez d'obtenir la valeur de la propriété rayon (vous devriez obtenir un msg d'erreur)

class Cercle:
    def __init__(self, rayon):
        self._rayon = rayon
    @property
    def rayon(self):
        return self._rayon
    @rayon.setter
    def rayon(self,rayon):
        if self._rayon > 0:
            self._rayon = rayon
    @rayon.deleter
    def rayon(self):
        self._rayon = 0


circle = Cercle(45)

print(circle.rayon)

circle.rayon = 50
print(circle.rayon)

del circle.rayon
print(circle.rayon)


