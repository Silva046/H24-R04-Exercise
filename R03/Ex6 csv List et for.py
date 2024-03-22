import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script
os.chdir("csvs")
import csv


# Tu as toujours rêvé de travailler un jour pour le CH
# Tu as vu une job en TI, 
#           Analyste, soutien technique réseau

# Le fichier Competences.csv contient la liste des compétences qu'ils demandent, 
# #         avec le niveau et le fait que cette compétence est exigée ou plutôt un atout
# Bien que tu n'as pas encore fini tes études tu veux imprimer ici les compétences qui sont exigées 
# afin de bien développer ces compétences pour qu'éventuellement tu puisses entrer dans cette entreprise

#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas

with open("Ex6 Competences.csv" , encoding='utf-8') as csv_file :
    csv_reader = csv.reader(csv_file , delimiter='/')
    with open("Ex6 Compétences Exiges.csv" , "w", encoding='utf-8') as csv_file_writer :
        csv_writer = csv.writer(csv_file_writer , delimiter='/' , lineterminator='\n')
        csv_writer.writerow(["Compétences" , "Niveau" , "Éxigences"])
        next(csv_reader)
        for line in csv_reader :
            if line[2] in ["Exigé"] :
                csv_writer.writerow(line)


























# INSTRUCTIONS DÉTAILLÉES
#Ouvrez en lecture le fichier Ex6 Competences.csv
#avec l'encodage et le delimiter requis
#Imprimez la première ligne
#Faites une boucle pour passer à travers chacune des lignes du fichier
#Si l'exigence est  'Exigé' imprimez cette ligne

