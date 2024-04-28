from ressources import *


# Tous les tests dans cette section devront générer soit :
#       Une erreur et une interruption du programme
#        OU
#       L'affichage d'un message d'erreur dans le terminal. 


#Etape 1 : instanciations d'objets
# Créez les mêmes instances d'objets que dans TP2_test_succes.py
# Vous pouvez copier-coller les lignes d'instanciations
poste1 = Poste("poste1","208.67.222.222","255.255.255.0","192.168.21.1","quebec")
poste2 = Poste("poste2","255.67.223.223","255.255.255.0","192.168.21.1","quebec")
poste3 = Poste("poste3","255.67.223.223","255.255.255.0","192.168.21.1","quebec")
routeur1 = Routeur("routeur1", "8.8.8.8","255.255.255.0","192.168.21.1","quebec",8)
routeur2 = Routeur("routeur2", "8.8.8.8","255.255.255.0","192.168.21.1","quebec",2)
reseau1 = SousReseau("reseau1",[poste1,routeur1])
gestion_baccichet_vincent = Gestionnaire("gestion_baccichet_vincent",reseau1)

print("\nTests 1, instanciation d'un objet Composante ")
#Test 1 : Essayez de créer une instance d'un objet Composante.
try:
    Composante("comp1","192.168.21.10","255.255.255.0","192.168.21.1","Quebec")
    print("l'instance a été crée")
except TypeError:
    print("L'instance ne peut pas être crée")

print("\nTests 2, Postes : ")
# Test 2 :
# 2a - essayer d'ouvrir un Poste déjà ouvert
# 2b - essayer de fermer un Poste déjà fermé.
# 2c - vérifiez que la deuxième station ne répond PAS aux pings.
poste1.ouvrir()
poste1.ouvrir()
poste2.fermer()
poste2.ping()


print("\nTests 3, routeurs : ")
#Test 3 : routeur
print("T3a - ",end="")
#Test 3a - Essayez d'ajouter les trois instances de Poste au deuxième commutateur (qui devrait avoir un 2 connexions max).
routeur2.ajouter_connexions(poste1)
routeur2.ajouter_connexions(poste2)
routeur2.ajouter_connexions(poste3)
print("T3b - ",end="")
#Test 3b - Essayez de supprimer une connexion (vers le poste1) du routeur1
# (qui ne devrait pas avoir de connexions présentement)
routeur1.supprimer_connexion(poste1)
routeur1.supprimer_connexion(poste1)
#je le met deux fois à cause que plus haut j'ai du ajouter la connexion
print("T3c - ",end="")
#Test 3c - Essayez de changer le nb_ports du premier routeur
try:
    routeur1.nb_port = 3
except AttributeError:
    print("nb_port n'a pas de setter")

print("T3d - ",end="")
#Test 3d essayez de changez le nom du premier routeur
try:
    routeur1.nom = "nouveau_nom_router"
except AttributeError:
    print("nom n'a pas de setter")


print("\nTests 4, SousReseau : ")
# Test 4 : reseau

print("T4a - ",end="")
# Test 4a - essayez d'ajouter la même composante 2 fois
reseau1.ajouter_composante(routeur2)

print("T4b - ",end="")
# Test 4b - essayez de retirer une composante qui ne fait pas partie du réseau
reseau1.supprimer_composante(poste2)

print("\nTests 5, Gestionnaire : ")
# Test 5 : Gestionnaire
# Essayez de tester une connexion vers une composante qui ne fait pas partie du réseau
gestion_baccichet_vincent.tester_connexion(poste2)

