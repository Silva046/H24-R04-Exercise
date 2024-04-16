from ressources import *

#Test 1 : instanciations d'objets
print("\nTests 1, instanciation d'objets ")
# Créez 3 instances de la classe Poste. Chaque Poste doit avoir un nom unique et significatif.
# Leurs adresses IP doivent être : "208.67.222.222","255.67.223.223", et "255.67.223.223"
# Les valeurs de masque_sous_reseau et adresse_passerelle ne sont pas vérifiées dans ce TP

poste1 = Poste()
poste2 = Poste()
poste3 = Poste()


# Créez 1 instance de la classe Routeur avec l'adresse IP "8.8.8.8" et un nb_port de 8
routeur1 = Routeur()
# Créez 1 instance de la classe Routeur avec l'adresse IP "8.8.8.8" et un nb_port de 2
routeur2 = Routeur()


# Créez 1 instance de la classe SousReseau. 
# Elle doit contenir deux des composantes : le poste1, et une le routeur1 que vous venez de créer.
reseau1 = SousReseau()

# Créez 1 instance de la classe Gestionnaire.
# Le nom de la classe Gestion doit suivre le format "gestion_nom-de-famille_prenom". Avec bien sûr, vôtre nom et prénom.
# L'attribut nom de cette instance doit être "Gestionnaire_XXXXXX" où les X correspondent à votre code permanent.
gestion_CHANGER_LE_NOM = Gestionnaire()


#Test 2 : Postes
print("\nTests 2, Postes : ")
#Test 2a : Testez que la première instance Poste est bien initialisée au stade fermé.
print("T2a - ",end="")

#print(f"SUCCÈS - La station {poste1.nom} est éteinte.")
#print(f"ÉCHEC {'*'*10}")

print("T2b - ",end="")
#Test 2b : Utiliser la méthode ouvrir() et vérifiez que l'attribut "est_allume" à bien changer.

print("T2c - ",end="")
#Test 2c - Fermez cette même station et vérifiez qu'elle est fermée.


print("T2d - ",end="")
#Test 2d - Vérifiez que la première station répond bien aux pings.




#T3 : Commutateur. 
print("\nTests 3, routeurs : ")
print("T3a - ",end="")
#Test 3a : Ajouter les deux premiers postes au routeur 1.
#Vérifiez qu'elles ont bien été ajoutées.


print("T3b - ",end="")
#Test 3b : Supprimer la connexion vers la première station.
# Vérifiez que la station ne fait plus partie des connexions


print("T3c - ",end="")
#Test 3c : Vérifiez que le deuxième poste station fait encore partie des connexions


#Test 3d - Vérifiez que le routeur répond aux pings.


#test 3e - Ajouter le routeur 2 à la liste des connexions de routeur 1.
#          vérifier si le routeur 1 fait maintenant partie de la liste des connexions du routeur 2.
#           (Ce test est un peu plus difficile, revenez à la fin du TP s'il pose problème)


# Tests de la classe SousRéseau
print("\nTests 4, réseau : ")
# Test 4a : Au réseau 1 : ajoutez la composante poste2 et la composante routeur2.
# Vérifiez que ces composantes ont bien été ajoutées.
print("T4a - ",end="")

# Test 4b : retirer le poste1 (le poste1 devrait être ajouté lors de l'instanciation du SousReseau)
# Vérifiez qu'elle a bien été retirée.
print("T4b - ",end="")

# Test 4c - vérifiez que vous pouvez bien ping la station routeur1 avec la méthode ping du réseau
print("T4c - ",end="")

# Test 4d - obtenez la composante dont l'adresse ip est "255.67.223.223" en utilisant la méthode "get_composante_par_ip()"
#           Vérifier que la composante obtenue correspond bien au poste 2
print("T4d - ",end="")

# Test 4e - listez toutes les composantes dans le réseau
print("T4e - ",end="")

#Test 5 : gestionnaire
#   tester_connexion d'une composante en ligne (poste 1)
#   test_connexion d'une composante hors ligne (poste 2)
#   tester toutes les connexions (avec la méthode "tester_toutes_les_connexions()")
# Imprimez le nom de votre gestionnaire
print(f"\nTests 5, gestionnaire {'NOM DU GESTIONNAIRE'} : ")
print("T5a - ",end="")
# Test 5a - testez la connexion du commutateur 1 qui devrait fonctionner


print("T5b - ",end="")
# test 5b : Testez la connexion de la deuxième station, qui ne devrait pas fonctionner


# test 5c : Tester toutes les connexions
print("T5c - Test des connexions :")



print()
