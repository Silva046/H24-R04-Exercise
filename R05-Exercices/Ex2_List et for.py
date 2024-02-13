import random

# RAPPEL
# dans l'interpréteur de python (dir(str)) #montre ce que fait chacune des méthodes de la classe str#
# dans l'interpréteur de python  dir(str.find) #montre ce que fait la méthode find de la classe str# 


# Pour chaque question ci-dessous, faites le code demandé. Laissez print(80*'_') déjà là afin de séparer les questions. 

# ICI, on a le code pour générer un entier aléatoire entre 50 et 500 inclusivement
un_chiffre_aleatoire = random.randint(50,500)

# ICI, une boucle pour générer une liste de 10 nombres aléatoires entre 50 et 500 inclusivement
# Q0                                                                                                            #
print(f"Q0{80*'_'}")
liste_chiffres = []
for index in range(10):
    liste_chiffres.append(random.randint(50,500))


# Q1                                                                                                            #
# Imprimez la liste générée ci-dessus
# Dans le terminal la réponse commence par: " Q1: Voici la liste: ...."  #
print(f"Q1{80*'_'}")




# Q2                                                                                                             #
# Affichez le premier chiffre de votre liste                                                                     #
# Dans le terminal la réponse doit être: "Q2: Premier chiffre de la liste : X."      X variant selon votre liste #
print(f"Q2{80*'_'}")



# Q3                                                                                                             #
# Faites le code pour afficher si oui ou non le premier chiffre de la liste est supérieur ou égal à 100          #
# Vous devez ABSOLUMENT FAIRE un if...else...                                                                    #
# Dans le terminal, si le premier chiffre était 50 par exemple,                                                  #
#           la réponse serait: "Q3: Le chiffre 50 n'est pas supérieur ou égal à 100"                             #
print(f"Q3{80*'_'}")



# Q4                                                                                                             #
# Faites le code pour afficher si le dernier nombre est inférieur à 300, égal à 300 ou, s'il est supérieur à 300
# Faites un message approprié selon le cas. Vous DEVEZ utiliser le if... elif... else     #
print(f"Q4{80*'_'}")




# Q5 Maintenant on va compter le nombre de chiffres inférieurs à 100 qu'il y a dans la liste
#    Avant la boucle, initialisez votre compteur à 0
#    Faites une boucle for pour passer à travers votre liste  ( n'utilisez pas les fonctions range() ou len() )
#    Dans la boucle, faites le test pour voir si le chiffre courant est inférieur à 100
#    Si oui, augmentez votre compteur de 1
#    Après la boucle, imprimez le résultat
# Dans le terminal, si vous avez 3 chiffres inférieurs à 100 par exemple,                                         #
#           la réponse serait: "Q5: Il y a dans la liste 3 chiffres inférieurs à 100"                             #  
print(f"Q5{80*'_'}")



#  Q6                                                                                                               #
#  Créez une deuxième liste de 5 chiffres entre 500 et 1000 cette fois-ci                                           #
#  Ajoutez cette deuxième liste à votre première liste  (vérifiez quelle méthode des listes permet de faire cela)   #
#  Faites le code pour imprimer le nombre de chiffres entre 300 et 800 dans votre nouvelle liste                    #
#  Dans le terminal, si vous avez 6 chiffres entre 300  et 800 par exemple,                                         #
#           la réponse serait: "Q6: Il y a dans la liste 6 chiffres entre 400 et 800"                               #
#  Si vous êtes incertain sur la facon de crée un liste de nombre aléatoire, rappelez-vous, nous avons créé une     #
#  variable avec un nombre aléatoire au début de cet exercice                                                       #
print(f"Q6{80*'_'}")



# Q7                                                                                                             #
# Copiez votre code précédent et changez-le pour ne pas juste compter le nombre de chiffres entre 300 et 800 
# MAIS AUSSI, obtenir la moyenne de ces chiffres entre 300 et 800                                                #
#         Conseils: Avant la boucle, il vous faudra avoir une variable initialisée à 0 pour le total
#                   Dans la boucle, vous ajouterez le chiffre courant à cette variable
#                   Après la boucle, vous calculez la moyenne                                                    #
#  Dans le terminal, si vous avez 6 chiffres entre 300 et 800  et que le total est 3600 par exemple,             #
#           la réponse serait: 
#                    "Q7: Il y a dans la liste 6 chiffres entre 300 et 800, pour un total de 3600.
#                         La moyenne de ces chiffres est de 300"                                                 # 
print(f"Q7{80*'_'}")

