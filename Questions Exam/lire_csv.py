#! /bin/python
import csv
import os
os.chdir(os.path.dirname(__file__))

# Q3
# Ouvrez le ficher en lecture
# Utilisez le module csv pour lire le contenu du fichier
# Sautez la première ligne contenant les en-têtes
# Ajoutez chaque ligne à la variable list_client
# Finalement, imprimer la variable list_client

nom_fichier = "fichier_a_lire.csv"
list_client = []

with open(nom_fichier, "r", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:
        list_client.append(line)
print(list_client)

