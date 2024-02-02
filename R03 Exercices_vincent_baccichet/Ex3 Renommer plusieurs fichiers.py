# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

import os
os.chdir(os.path.dirname(__file__))
#Déplacement
user = os.environ.get("USERPROFILE")
chemin = os.chdir(f"{user}/Documents\programmation 2\R03 Exercices_vincent_baccichet\Ex3 Videos")
#Boucle pour chercher dans tout les fichiers de EX3 videos
for filename in os.listdir(chemin) : 
    #séparation du path et de l'extension
    nom_fichier , extension = os.path.splitext(filename)
    #On sépare le fichier en 3 catégories différentes
    titre , cours , numero_cours , extension = nom_fichier.split("_")
    #on enlève les espaces dans le titre et dans le numéro de cours
    titre = titre.strip()
    numero_cours = numero_cours.strip()
    numero_cours = numero_cours.zfill(2)
    #recréation du nouveau fichier
    new_filename = f"{titre}_{cours}_{numero_cours}_{extension}"
    print(new_filename)
    #renommer le fichier
    os.rename(filename , new_filename)





