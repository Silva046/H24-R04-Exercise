import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script


# Vous avez mis des vidéos sur youtube et vous avez noté, pour chaque vidéo, le nombre de likes des 7 premiers jours de chacun des vidéos
# Ces données sont dans le fichier Ex1_youtube_Nb_Likes.txt


# Vous voulez calculez le total des likes de tous vos vidéos (le dernier de chaque ligne)
# Et imprimer dans le terminal le résultat ainsi "J'ai eu un total de 788502 likes pour mes 3 vidéos"
# Naturellement, le nombre de likes total et le nombre de vidéos sont des données calculées


# Observez le contenu du fichier txt et notez le caractère spécial qui sépare les données
# Si vous êtes fort en programmation, faites le code maintenant
# Si vous avez besoin de plus d'explications, vous pourrez les trouver plus bas dans cet exercice






















# EXPLICATIONS SUPPLÉMENTAIRES
# Créez des variables:
#           pour additionner le dernier nb de likes de chaque vidéo (total_likes) et initialisez-la à 0
#           pour le nombre de vidéos que vous avez (nb_videos) et initialez-la à 0

# Pour y arriver, utlisant with, ouvrez en lecture le fichier Ex1_youtub_Nb_Likes.txt

# Vous devez ensuite crée un objet lecteur csv qui considère '|' comme étant le caractère de séparation
# Faites une boucle pour lire chacune des lignes de ce lecteur csv'
#       Prenez le dernier élément de la liste obtenue, transformez le en un entier et ajoutez ce nombre à votre total_likes
#       Augmenter aussi de 1 votre variable nb_videos
# Après la boucle, imprimez le résultat demandé dans le terminal 


