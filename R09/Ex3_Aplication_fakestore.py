import os
os.chdir(os.path.dirname(__file__))



# OBJECTIF : on veut pouvoir calculer la valeur de chaque cart lorsqu'on fait une requête

print(f"Q01{80*'_'}")
# Q1 importez le module "Ex1_FakeStore_util" que vous avez fait dans l'exercice 1



print(f"Q02{80*'_'}")
# Q2. Faites une nouvelle fonction appellez req_product_by_id qui prend un paramètre id,
#       qui fait une requête au fakestoreapi pour ce produit uniquement et qui retourne le produit
#       sous forme de dictionnaire.

def req_product_by_id(id:int|str):
    id = int(id)        # permet à la fonction de recevoir la valeur 3 (un int) ou "3" (un str) et de la traité de la même manière
    pass



print(f"Q03{80*'_'}")
# Q3. Faites une nouvelle fonction get_products_from_cart 
#       qui prend un dictionnaire correspondant à un cart en paramètre
#       et qui fait appel à la fonction req_product_by_id pour chacun des produits.
#       et qui retourne une liste de ces produits
#           Extra : ajoutez une nouvelle clef à chaque produit correspondant à quantité



print(f"Q04{80*'_'}")
# Q4. Testez vos fonctions. Faites appel à la fonction get_product_from de l'Exercice 1 pour obtenir 1 cart.
#       utiliser la valeur de retour comme paramètre pour la fonction get_products_from_cart.




print(f"Q04{80*'_'}")
# Q5. Vous devriez maintenant avoir une liste contenant les objets dans le cart ainsi que leur quantité
#           Quel la valeur total du cart ?
#           Quel produit est le plus chère ? (son nom et id)
#           Quel produit est commandé en plus grand nombre ? (son nom et id)
#           Quel est la valeur moyenne des produits dans le cart ?