import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Q0 : importez le module json

import json

print(f"Q1{'_'*60}")
# Q1
# Lisez le contenue du fichiers "clients.json"
# Ce fichier contient 3 dictionnaires.
# storer le contenu du fichier lue dans une variable consistant en une liste de dictionnaires
#       utiliser le module json
with open("clients.json" , "r") as json_file :
    clients = json.loads(json_file.read())
    #Boucle qui passe à travers la liste clients (Clients est une liste de dictionnaire) et va chercher les noms. Si je ne fais pas une boucle je vais devoir absolument mettre [x] sinon il 
    #ne comprendras pas.
    for names in clients :
        print(names['name'])


print(f"Q2{'_'*60}")
# Q2
# passez à travers la liste obtenue à la q1 et imprimer les noms et prénoms de chaque clients

