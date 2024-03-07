import requests
import json


base_url="https://fakestoreapi.com"


# Q1 écrivez une fonction appelée request_from qui aura 2 paramètres optionnels
#    le type d'objets que vous voulez aller chercher et le nombre d'objets de ce type

# faites une validation pour le type d'objets, car fakestoreapi.com ne vous permet d'aller chercher que des 
#       products, carts et des user

# Si le nombre d'objets désirés n'est pas entré, envoyez 1 objet du type demandé

# La fonction retournera le nombre d'objets du type désirés pourvu que le type soit products, carts ou user




         

# Q2 ajouter une section qui permettra d'utiliser ce fichier en tant que script ou que module

# Lorsqu'il est exécuté en tant que script, ce fichier devrait faire une requête pour 1 seul produit de votre choix.
# Puis il devrait imprimer un message dans le terminal indiquant si la requête a été un succès ou nom. 

# Pour qu'on script se comporte différemment lorsqu'il est utilisé comme un script ou comme un module,
#   vous devez comparer la valeur de la variable "__name__" et voir si elle correspond au programme principale en cours d'exécution ( le "__main__")










print(__name__) # laisser cette ligne intouchée pour l'exercice 2