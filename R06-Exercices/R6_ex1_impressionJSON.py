import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script


donnees_clients = [{'city': 'San Antonio', 'street': 'Hunters Creek Dr', 'number': 6454, 'zipcode': '98234-1734', 'name': {'firstname': 'don', 'lastname': 'romer'}},
                   {'city': 'san Antonio', 'street': 'adams St', 'number': 245, 'zipcode': '80796-1234', 'name': {'firstname': 'derek', 'lastname': 'powell'}}, 
                   {'city': 'el paso', 'street': 'prospect st', 'number': 124, 'zipcode': '12346-0456', 'name': {'firstname': 'david', 'lastname': 'russell'}}]


# Voici trois dictionnaires contenues dans une liste de donnes clients.



# Q0 : importez le module json



print(f"Q1{'_'*60}")
#Q1 : 
# Imprimez dans la console la variable donnees_clients une première fois.
# Imprimez à nouveau cette liste, mais cette fois-ci de facons à ce qu'elle soit facilement lisible par l'être humain
#       vous devez utiliser le module json, la fonction dumps, et le paramètre indent






print(f"Q2{'_'*60}")
# Q2 :
# Enregistrez le premier membre de la liste dans un fichier texte nommé "R6_ex_q2.json"
# Notez bien qu'il ne s'agit pas d'un csv. Vous devez utilisé les méthode .write() ou writelines()

with open("R6_ex_q2.json", "w", encoding="utf-8") as fichier_ecrire :
    pass


print(f"Q3{'_'*60}")
#Q3 :
# Générez une nouvelle liste de dictionnaire à partir de la liste "donnees_clients".
# Cette nouvelle liste doit encore contenir 3 dictionnaires, mais pour ces dictionnaires on veut :
#       1 - Une clef "id" correspondant à leur position dans la liste originel (1 , 2, puis 3)
#       2 - La clef "name" dans le même format que "donnees_clients".
#       3 - L'addresse complète dans une seule clef "addresse"
#               par ex le premier client serait : "addresse" : 'San Antonio, 6454 Hunters Creek Dr, 98234-1734'
#               je conseil d'utiliser un f-string ici



print(f"Q4{'_'*60}")
#Q4 : 
# Enregistrez cette nouvelle liste de dictionnaires dans un fichier nommé : "clients_simplifiés"