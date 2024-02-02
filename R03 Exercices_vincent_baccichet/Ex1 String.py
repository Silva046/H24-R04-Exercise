#Q1
#  Voici une chaine de caractères qui ressemble à une ligne de données que vous auriez extraite d'un fichier text
ligne_donnees = " AMD Ryzen 9 5900X ;  AMD Ryzen 7 5800X3 ;  Intel Core i9 12900 K    " 
#  Vous devez dans un premier temps séparer les données sur le caractère qui les séparent ( le ';' ici ) avec la méthode .split
#  Vous voulez ensuite avoir nouvelle une liste contennant chacun des processeurs MAIS sans les espaces avant et après chaque processeur
#  Imprimez cette nouvelle liste
print(f"Q1{'_'*60}")
donnee = ligne_donnees.split(";")

autre_donnee = []


for data in donnee :
    autre_donnee.append(data.strip())
print(autre_donnee)








# Q2
# Voici un nom de fichier dont chaque partie est séparée par un _
nom_fichier_et_extension = "Python_Rencontre 3_Approfondissement str.docx"
# Séparez nom_fichier_et_extension sur le '.' et gardez les parties dans des sous-chaines séparées
# Séparez le nom de fichier de façon à récupérer le nom du cours, la rencontre et le sujet de la rencontre
# Imprimez le nom du cours, la rencontre et le sujet de la rencontre 
print(f"Q2{'_'*60}")
separation = nom_fichier_et_extension.split(".")
print(separation)
fichier = separation[0]
extension = separation[1]
fichier_split = fichier.split("_")
nom_du_cours = fichier_split[0]
rencontre = fichier_split[1]
sujet = fichier_split[2]

print(nom_du_cours)
print(rencontre)
print(sujet)







#Q3
# Remplir un string pour qu'il fasse 2 caractères de long avec .zfill()
# Au départ, vous avez une chaine qui contient des nombres
str_nombres = "1,5,10,15,20,25"
# transformez cette chaine en une liste de str mettez la en ordre avec .sort()
# Imprimez la liste. Qu'est-ce qui est étonnant? (Cela devrait vous donnez ['1', '10', '15', '20', '25', '5'] )

# Pour pouvoir avoir la liste de string dans un ordre croissant numérique il faut remplacer les valeurs pour qu'ils soient tous 2 charactères de long
# faites une boucle sur les valeurs de la liste et utilisez la méthode zfill()
print(f"Q3{'_'*60}")
nombres_string = sorted(str_nombres.split(","))
print(nombres_string)

nombre_fill = []

for i in nombres_string :
    nombre_fill.append(i.zfill(2))

nombre_fill.sort()
print(nombre_fill)
