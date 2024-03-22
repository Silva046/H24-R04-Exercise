import os
os.chdir(os.path.dirname(__file__))

print(f"Q01{80*'_'}")
# Q1 importez le module "Ex1_FakeStore_util" que vous avez fait dans l'exercice 1
#       imprimez ensuite le nom du fichier courant (la variable __main__ )
#       constatez : le nom du script précédant de l'exercice 1 change selon s'il s'agit d'un module ou d'un script

print("Nom d'un fichier importer lors de l'exécution : ")
import Ex1_FakeStore_util as ex1
print("Nom du fichier exécuter : ")
print(__name__)




print(f"Q02{80*'_'}")
# Q2 Utilisez la méthode request_from de votre module pour obtenir 3 produits
#           Commencez par imprimer la liste des trois produits 
#                   puis voyez la clé qui vous permettra d'obtenir le nom du produit

produits = ex1.request_from("products",3)
print(produits)

print(f"Q03{80*'_'}")
# Q3 N'Imprimez QUE les noms de ces trois produits. On veut extraire uniquement les noms de ces produits.

for produit in produits:
    print(produit['title'])




print(f"Q04{80*'_'}")
# Q2 A Utilisez la méthode request_from de votre module pour obtenir 4 cart 
#           Commencez par imprimer la liste du cart obtenu
#                   puis voyez la clé qui vous permettra d'obtenir la liste des produits dans le cart
# Q2 B N'Imprimez QUE l'ID et le nombre de produits dans chaque cart
carts = ex1.request_from("carts",4)
list_produit = []
print(carts)
for cart in carts:
    qte = 0
    products = cart['products']
    for product in products:
        qte += int(product['quantity'])
    print(f"le chariot {cart['']}")
    pass





print(f"Q05{80*'_'}")
# Q3 finalement, essayez d'utilisez la fonction request_from de votre module pour obtenir une ressource  du type bonbon
#       vous devriez obtenir un message d'erreur de votre fonction AVANT de faire la requête au site web 

