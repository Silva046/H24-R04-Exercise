from ressources import *


# Tous les tests dans cette section devront générer soit :
#       Une erreur et une interruption du programme
#        OU
#       L'affichage d'un message d'erreur dans le terminal. 


#Etape 1 : instanciations d'objets
# Créez les mêmes instances d'objets que dans TP2_test_succes.py
# Vous pouvez copier-coller les lignes d'instanciations


print("\nTests 1, instanciation d'un objet Composante ")
#Test 1 : Essayez de créer une instance d'un objet Composante.



print("\nTests 2, Postes : ")
# Test 2 :
# 2a - essayer d'ouvrir un Poste déjà ouvert
# 2b - essayer de fermer un Poste déjà fermé.
# 2c - vérifiez que la deuxième station ne répond PAS aux pings.



print("\nTests 3, routeurs : ")
#Test 3 : routeur
print("T3a - ",end="")
#Test 3a - Essayez d'ajouter les trois instances de Poste au deuxième commutateur (qui devrait avoir un 2 connexions max).


print("T3b - ",end="")
#Test 3b - Essayez de supprimer une connexion (vers le poste1) du routeur1
# (qui ne devrait pas avoir de connexions présentement)


print("T3c - ",end="")
#Test 3c - Essayez de changer le nb_ports du premier routeur


print("T3d - ",end="")
#Test 3d essayez de changez le nom du premier routeur



print("\nTests 4, SousReseau : ")
# Test 4 : reseau

print("T4a - ",end="")
# Test 4a - essayez d'ajouter la même composante 2 fois
print("T4b - ",end="")
# Test 4b - essayez de retirer une composante qui ne fait pas partie du réseau



print("\nTests 5, Gestionnaire : ")
# Test 5 : Gestionnaire
# Essayez de tester une connexion vers une composante qui ne fait pas partie du réseau

