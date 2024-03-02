# Pour installer requests
# Dans le terminal              pip install requests

# fakerapi.it/en
import requests
import json

#IMPORTANT : il s'agit d'un api différent des exercices 1 à 4. Il faut regarder la documentation en ligne pour savoir comment l'interroger

BASE_URL = 'https://fakerapi.it/api/v1/products?_seed=123'
# Cet url inclut déjà qu'il s'agit d'une demande de produit et avec un "seed" constant


#  Le but est d'obtenir le 'price' moyen des produits de moins de 100000 qui sont dans la catégorie 3.


### - Q1) Faites une demande de 25 produits 




 
##  Q2) Utilisez json.dumps() et sont paramètre indent pour imprimer 
# la réponse de facon lisible pour l'humain.




# Q3)  Obtenez la liste des produits à partir de la clé 'data' du dictionnaire obtenu en Q3



# Q4) On veut faire la moyenne des produits qui sont dans la catégorie 3
#        ET dont le prix est moins de 100 000$
#
# Pour cela: 
#      Créez vous deux variables initialisées à 0 au départ. 
#      Une pour accumuler le total des prix, l'autre pour compter le nombre de produits
#      Vous faites une boucle pour passer à travers la liste des produits obtenue en Q4
#           Dans la boucle, vous obtenez le prix du produit et castez-le en float
#           Si le produit a la catégorie 3 et que le prix est inférieur à 100000
#                   ajoutez-le au total des prix
#                   augmenter votre compteur de produit qui satisfont le test précédent
#      Après la boucle calculez la moyenne
#      Finalement imprimez le résultat, qui pourrait ressembler à ceci: 
#            "Parmi les 25 produits que j'ai obtenu, il y a 6 produits dans la catégorie 3 et leur prix moyen est de 12328.94$"





