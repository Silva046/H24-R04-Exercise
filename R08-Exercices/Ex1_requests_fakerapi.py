# Pour installer requests
# Dans le terminal              pip install requests
# Fermez et réouvrez Code si nécéssaire

# fakerapi.it/en
import requests
import json

BASE_URL = 'https://fakerapi.it/api/v1/products?_seed=123'
# Cet url inclut déjà qu'il s'agit d'une demande de produit et avec un "seed" constant

# pour avoir seulement X produits
# l'API nous offre /products?_quantity=X

# Q1) faire une demande de 1 produit1 (&_quantity=1) et conservez le résultat dans une variable




# Q2) Pour travailler avec le résultat de la réponse, il faut le convertire en objet python.
# L'objet de la classe <Respsonse> retourné par la requests.get() possède la méthode .json() pour faire cela.
# Transformé la réponse et imprimer le résultat.





# Q3) Le résultat obtenu a la question 2 n'est pas très clair.
# La fonction json.dumps() prend un objet python en paramètre et retourne une chaine de caractères.
# Cette fonction peut aussi prendre unr valeur pour l'argument "indent" qui sert a spécifier le niveau
# d'indentation de la chaine de caractères. Avec le paramètre indent, le string devient lisible pour l'être humain.
# Utilisé json.dumps() pour imprimer la réponse sous un format lisible par l'humain.




#Si on regarde le résultat obtenue à la question 3, on peut voir la structure de la réponse obtenu.
# La réponse devrait être similaire à ceci :
""" {
    "status": "OK",
    "code": 200,
    "total": 1,
    "data": [
        {
            "id": 1,
            "name": "Ut magni et voluptatem est.",
            "description": "Quaerat voluptate vel quae. Repudiandae nobis et labore vitae id id placeat.",
            "ean": "5258822017705",
            "upc": "446534029075"
        },
        {
            "id": 2,
            "name": "Hic sunt sed iusto quia.",
            "description": "Iste dolorum sed pariatur placeat amet atque. Et ex incidunt quam voluptatem voluptatibus iusto. Deserunt ducimus voluptate earum id soluta nesciunt.",
            "ean": "8151906598244",
            "upc": "238309185512"
        }
    ]
} """
# On peut constater que l'objet obtenu par la fonction .json() est dans ce cas un dictionnaire.
# Ce dictionnaire contient seulement 4 paires clefs ; "status","code","total", et "data"
# C'est la clef "data" qui contient la liste des produits en réponse à notre requête.



# Q4)  Obtenez le premier élément du dictionnaire avec la clé 'data' dans une variable et imprimez-le


#  Donc on obtient quelque chose comme
# {'id': 1, 'name': 'Blanditiis aut in quia omnis.', 'net_price': 2.15, 'taxes': 22, 'price': '2.62', 'categories': [2, 3, 5]}



#  Q5) Obtenez le prix et changez le en un float


#  Q6)  Utilisez l'instruction << in >> pour vérifier si 3 fait partie des valeurs dans la liste categories du produit


#  Q7)  Imprimez le prix et si le produit est dans la catégorie 3 ou non
#       Quelque chose comme: "Le produit a le prix de 3945.01 et on peut savoir s'il est dans la catégorie 3: False"

