# On peut faire une invitation générale comme cela, mais c'est un peu froid
# Nous avons ici une simple invitation, sans nom précis #
# Si on envoie cette invitation à nos amis, ils pourraient être fachés car c'est un peu impersonnel.#
print("Bonjour \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")



# Nous avons ici la même invitation lancée à plusieurs de nos amis, avec leurs noms.                       #
print("Bonjour Marc,\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Pierre,\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Lucie, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Achraf, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Claude, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Ilyan, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Maria, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Thomas, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
# Ca fonctionne mais c'est de la répétition.  Et si je voulais inviter 30 personnes....


print(f"Q1{'_'*60}")
# Q1 A:  Faites une fonction pour inviter tout le monde, sans duplication du code.
#        Cette fonction prendra une liste d'amis en paramètres                                      #
def invitation(nom_liste):
    for ami in nom_liste :
        print(f"Bonjour {ami},\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
  
  
  
  

# Q1 B:   Appellez la fonction avec la liste d'amis qu'on veut inviter. 
amis = ["Marc", "Pierre", "Lucie", "Achraf","Claude", "Ilyan", "Maria", "Thomas"]

invitation(amis)



print(f"Q2{'_'*60}")
# Q2 A:   Faites une nouvelle fonction pour inviter tout le monde, dans un lieu, un jour et une heure qui varient, sans duplication du code
#         Appelez cette fonction invitation2 (elle devrait prendre 4 paramètres)
def invitation_precise(nom_liste , lieu , jour , heure):
    for ami in nom_liste :
        print(f"Bonjour {ami},\n Je veux t'inviter à venir {lieu} {jour} vers {heure}. Cela t'intéresse?")

liste_amis = ["Sylvain" , "Nathalie" , "Paul"]

# Q2 B:  Appel de la fonction invitation2 pour inviter Sylvain et Nathalie au café étudiant, vendredi, vers 13h00
invitation_precise(liste_amis[0:2] , "au café étudiant" , "Vendredi" , "13h00")

# Q2 C:  Appel de la fonction invitation2 pour inviter Sylvain, Nathalie et Paul chez moi pour souper, samedi vers 17h00

invitation_precise(liste_amis , "chex moi" , "samedi" , "17h00")

