import requests
import json


base_url="https://fakestoreapi.com"

# Q1 Écrivez une fonction appelée request_carts qui aura 1 paramètre
#   soit le nombre de carts que vous voulez aller chercher
#   Le nombre de cart doit être donné lors de l'appel de la fonction :
#           - Si le nombre de cart n'est pas donné lors de l'appel le nbr de carts par défaut est de 1 
#           - Vérifiez que le nombre donné lors de l'appel est entre 1 et 10
#           - Si ce n'est pas le cas, donnez un message comme quoi il faut demander entre 1 et 10 carts, 
#             en précisant le nombre de carts qui avait été demandé

#   La fonction doit retourner les carts obtenu avec la requête get du site webs. Mais seulement si le nombre de carts demandés est entre 1 et 10

def request_carts(nombre:int=1):
    if 1 <= nombre <= 10:
        res = requests.get(f"{base_url}/carts?limit={nombre}")
        return res.json()
    else:
        print(f"Il faut demander entre 1 et 10 carts et non {nombre} carts!")


print(request_carts(2))


# Q2 Écrivez une fonction appelée request_products qui aura 1 paramètre
#   soit le nombre de produits que vous voulez aller chercher
#   Le nombre de produit doit soit être donné lors de l'appel de la fonction
#                             soit être demandé à l'usager s'il n'est pas donné ( utilisé la fonction input() )
#   Vérifiez que le nombre demandé est entre 1 et 10
#   Limitez cette valeur à 10 si l'usager en demande plus et donnez un message comme quoi vous avez cette limite
#   Si le nombre demandé est moins de 1, obtenez 1 produit tout simplement

#   La fonction doit retourner le nombre de produits demandés, si le nombre est entre 1 et 10

def valider_nombre(nombre:int):
    if nombre == None:
        print(int(input("Entré un nombre entre 1 et 10 : ")))
    elif nombre < 1:
        nombre = 1
    elif nombre > 10:
        nombre = 10
    return nombre


def request_products(nombre:int=None):
    nombre = valider_nombre(nombre)
    res = requests.get(f"{base_url}/products?limit={nombre}")
    return res.json()


print(json.dumps(request_products(),indent=4))





