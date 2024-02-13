import csv
import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script


# au cours 4, nous avons fait un exercice qui devait lire une liste d'étudtants et crée un dossier pour chaque étudiant.
# On veut maintenant decouper ce script en fonctions pour le rendre plus facilement compréhensible

#script du cours 4, à découper en fonctions
full_f_name = 'Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv'
index_cours = full_f_name.find('420')
cours = full_f_name[index_cours:index_cours+6]
index_groupe = full_f_name.find('gr')
groupe = full_f_name[index_groupe:index_groupe+6]

os.makedirs(f"{cours}/{groupe}")

noms_Etudiants = []

with open('Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv','r',encoding="utf-8") as data_CSV:
    csv_data = csv.reader(data_CSV,delimiter=';')
      #sauter la première ligne #
    next(csv_data)
    for line in csv_data:
        noms_Etudiants.append(f"{line[2]} {line[3]}")

os.chdir(cours+'/'+groupe)
print(os.getcwd())
for item in noms_Etudiants:        
    os.mkdir(item)
print(os.getcwd())



#  On pourrait découper ce script en plusieurs fonctions pour que cela soit plus clair ce qui est fait 

#  une fonction qui va avoir le nom du fichier en paramètre
# 		qui va lire le nom du fichier , en extraire le cours et le groupe et qui retourne ces deux infos avec un "/"
#       donc ici "4201B3/gr1010"
#  une fonction qui va avoir le nom du fichier en paramètre
#       qui va lire les données du fichier et retourner une liste des étudiants avec leur nom prenom
#  une dernière fonction qui créera un répertoire pour chacun des étudiants.

#  Le programme principal sera d'appeler ces fonctions puis de créer les répertoires désirés
#  Votre code devrait toujours fonctionner

