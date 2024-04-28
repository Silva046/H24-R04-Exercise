from ressources import *

#Test 1 : instanciations d'objets
print("\nTests 1, instanciation d'objets ")
# Créez 3 instances de la classe Poste. Chaque Poste doit avoir un nom unique et significatif.
# Leurs adresses IP doivent être : "208.67.222.222","255.67.223.223", et "255.67.223.223"
# Les valeurs de masque_sous_reseau et adresse_passerelle ne sont pas vérifiées dans ce TP

poste1 = Poste("poste1","208.67.222.222","255.255.255.0","192.168.21.1","quebec")
poste2 = Poste("poste2","255.67.223.223","255.255.255.0","192.168.21.1","quebec")
poste3 = Poste("poste3","255.67.223.223","255.255.255.0","192.168.21.1","quebec")


# Créez 1 instance de la classe Routeur avec l'adresse IP "8.8.8.8" et un nb_port de 8
routeur1 = Routeur("routeur1", "8.8.8.8","255.255.255.0","192.168.21.1","quebec",8)
# Créez 1 instance de la classe Routeur avec l'adresse IP "8.8.8.8" et un nb_port de 2
routeur2 = Routeur("routeur2", "8.8.8.8","255.255.255.0","192.168.21.1","quebec",2)


# Créez 1 instance de la classe SousReseau. 
# Elle doit contenir deux des composantes : le poste1, et une le routeur1 que vous venez de créer.
reseau1 = SousReseau("reseau1",[poste1,routeur1])

# Créez 1 instance de la classe Gestionnaire.
# Le nom de la classe Gestion doit suivre le format "gestion_nom-de-famille_prenom". Avec bien sûr, vôtre nom et prénom.
# L'attribut nom de cette instance doit être "Gestionnaire_XXXXXX" où les X correspondent à votre code permanent.
gestion_baccichet_vincent = Gestionnaire("gestion_baccichet_vincent",reseau1)


#Test 2 : Postes
print("\nTests 2, Postes : ")
#Test 2a : Testez que la première instance Poste est bien initialisée au stade fermé.
print("T2a - ",end="")
if poste1.est_allume == False:
    print(f"SUCCÈS - La station {poste1.nom} est éteinte.")
else:
    print(f"ÉCHEC {'*'*10}")

print("T2b - ",end="")
#Test 2b : Utiliser la méthode ouvrir() et vérifiez que l'attribut "est_allume" à bien changer.
poste1.ouvrir()
if poste1.est_allume == True:
    print(f"SUCCÈS - La station {poste1.nom} est allumé.")
else:
    print("Échec")
print("T2c - ",end="")
#Test 2c - Fermez cette même station et vérifiez qu'elle est fermée.
poste1.fermer()
if poste1.est_allume == False:
    print(f"SUCCÈS - La station {poste1.nom} est éteinte.")
else:
    print("Échec")

print("T2d - ",end="")
#Test 2d - Vérifiez que la première station répond bien aux pings.
if poste1.ping() == True:
    print(f"SUCCÈS - La station {poste1.nom} répond au ping.")
else:
    print("Échec")

#T3 : Commutateur. 
print("\nTests 3, routeurs : ")
print("T3a - ",end="")
#Test 3a : Ajouter les deux premiers postes au routeur 1.
#Vérifiez qu'elles ont bien été ajoutées.
routeur1.ajouter_connexions(poste1)
routeur1.ajouter_connexions(poste2)
if poste1 and poste2 in routeur1.ls_connexions:
    print(f"SUCCÈS - le poste 1 et 2 ont étés ajoutés au routeur1")
else: print("ÉCHEC")

print("T3b - ",end="")
#Test 3b : Supprimer la connexion vers la première station.
# Vérifiez que la station ne fait plus partie des connexions
routeur1.ajouter_connexions(poste1)
if poste1 in routeur1.ls_connexions:
    print("ÉCHEC - la station 1 ce retrouve toujours dans les connexions du routeur1")
else:print("SUCCÈS - le poste2 a bien été enlevé")

print("T3c - ",end="")
#Test 3c : Vérifiez que le deuxième poste station fait encore partie des connexions

print(f"Le sous-réseau routeur1 contient les connexions suivantes : \n{routeur1.ls_connexions}")

#Test 3d - Vérifiez que le routeur répond aux pings.
if routeur1.ping() == True:
    print("SUCCÈS - Le router routeur1 répond aux pings.")
else: ("ÉCHEC")

#test 3e - Ajouter le routeur 2 à la liste des connexions de routeur 1.
#          vérifier si le routeur 1 fait maintenant partie de la liste des connexions du routeur 2.
#           (Ce test est un peu plus difficile, revenez à la fin du TP s'il pose problème)
routeur1.ajouter_connexions(routeur2)

# Tests de la classe SousRéseau
print("\nTests 4, réseau : ")
# Test 4a : Au réseau 1 : ajoutez la composante poste2 et la composante routeur2.
# Vérifiez que ces composantes ont bien été ajoutées.
print("T4a - ",end="")
#mon if indique que le poste2 et le routeur2 ne sont pas dans la liste mais lorsqu'il rentre
#dans le code il voit que les deux sont déjà a l'intérieur
if poste2 and routeur2 not in reseau1._ls_composantes:
    reseau1.ajouter_composante(poste2)
    reseau1.ajouter_composante(routeur2)
if poste2 and routeur2 in reseau1.ls_composantes:
    print(" SUCCÈS - Les composantes ORDI_02, et routeur2 ont bien été ajoutés.")
else:print("ÉCHEC")
# Test 4b : retirer le poste1 (le poste1 devrait être ajouté lors de l'instanciation du SousReseau)
# Vérifiez qu'elle a bien été retirée.
print("T4b - ",end="")
reseau1.supprimer_composante(poste1)
if poste1 not in reseau1.ls_composantes:
    print("SUCCÈS - La station ORDI_01 à été retiré avec succès.")
else:print("ÉCHEC")

# Test 4c - vérifiez que vous pouvez bien ping la station routeur1 avec la méthode ping du réseau
print("T4c - ",end="")
if reseau1.ping(routeur1) == True:
    print("Le réseau reseau INFO est capable de demander à routeur1 de répondre aux pings.")
else:print("ÉCHEC")

# Test 4d - obtenez la composante dont l'adresse ip est "255.67.223.223" en utilisant la méthode "get_composante_par_ip()"
#           Vérifier que la composante obtenue correspond bien au poste 2
print("T4d - ",end="")
reseau1.get_composante_par_ip("255.67.223.223")
#dans le gestionnaire la fonction ne semble pas fonction à cause de la variable adresse_ip qui appartient a composant que 
#je ne sais pas comment appelé

# Test 4e - listez toutes les composantes dans le réseau
print("T4e - ",end="")
comp:Composante
for comp in reseau1.ls_composantes:
    print(comp.nom)


#Test 5 : gestionnaire
#   tester_connexion d'une composante en ligne (poste 1)
#   test_connexion d'une composante hors ligne (poste 2)
#   tester toutes les connexions (avec la méthode "tester_toutes_les_connexions()")
# Imprimez le nom de votre gestionnaire
print(f"\nTests 5, gestionnaire {'Gestionnaire_Vincent_Baccichet'} : ")
print("T5a - ",end="")
# Test 5a - testez la connexion du commutateur 1 qui devrait fonctionner
poste1.ouvrir()
poste2.fermer()
print("est ce que le poste 1 répond? :")
gestion_baccichet_vincent.tester_connexion(poste1)

print("T5b - ",end="")
# test 5b : Testez la connexion de la deuxième station, qui ne devrait pas fonctionner
print("est ce que le poste 2 répond? :")
gestion_baccichet_vincent.tester_connexion(poste2)

# test 5c : Tester toutes les connexions
print("Test de toutes les connexions :")
Gestionnaire.tester_toutes_les_connexions(gestion_baccichet_vincent)



print()
