import nouvelles_donnees as nd


# cette variable consiste en une liste de 500 dictionnaires, chacun correspondant à 1 client d'une agence d'aviation.
# ( voir le fichier nouvelles_donnees.py pour regarder à quoi ces données ressemblent )
donnees_voyage = nd.donnees_voyage



# Regarde cette liste de dictionnaires
# On veut obtenir des données sur les voyages effectués par les clients
# Obtenez   - Le nombre de personnes ayant fait un voyage en "Chine"
#           - Le nombre de personnes ayant fait un voyage au "Japon"
#           - Le nombre total de personnes ayant fait un voyage en "Chine" et/ou au "Japon"...
#                       - ... et le pourcentage des tous les voyageurs ayant visité la Chine ou le Japon
# Imprimez les résultats obtenus
cpt_chine = 0
cpt_japon = 0
cpt_asie = 0

for voyageur in donnees_voyage:
    if "chine" in voyageur['pays_visite']:
        cpt_chine += 1
    if "Japon" in voyageur["pays_visite"]:
        cpt_japon += 1
    if "Asie" in voyageur["pays_visite"] or "Japon" in voyageur["pays_visite"]:
        cpt_asie += 1

print(f"nbr voyage chine : {cpt_chine}")
print(f"nbr voyage japon : {cpt_japon}")
print(f"nbr voyage asie : {cpt_asie}")
print(f"{cpt_asie/len(donnees_voyage)*100}% en Asie")



# Question Bonus : 
# Obtenez et imprimez une liste de tous les pays visités par des voyageurs.
# Cette liste ne devrait pas contenir de duplicatas ( chaque pays apparait une seule fois )
liste_pays_disponible = []

for voyageur in donnees_voyage:
    for pays in voyageur["pays_visite"]:
        if pays not in liste_pays_disponible:
            liste_pays_disponible.append(pays)

print("voici les pays disponibles aux voyageurs :\n", liste_pays_disponible)