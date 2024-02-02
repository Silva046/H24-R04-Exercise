import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script
#
# Le fichier Ex2_Depenses_Janvier.txt contient les dépenses faites en janvier de 2022
#       -Janvier
#	        Passe mensuelle: 120
#	        Sortie cinéma: 60
#	        Abonnement cellulaire: 135
#	        Cafétaria: 160


# Vous devez écrire le code pour produire un nouveau fichier Ex1_Total_Janvier.txt qui contiendra les données suivantes:
#        MOIS     TOTAL 
#       -Janvier    475
#       

# Observez que le mois commence par le caractère '-' dans le fichier de départ et que chaque ligne se termine par un saut de ligne "\n"
# Vous devrez utiliser une boucle for pour calculer le total des dépenses du mois et les imprimer de façon à obtenir le résultat attendu
# Si vous êtes ok, allez-y
# Si vous en ressentez le besoin, il y a des explications plus détaillées dans le bas de ce document






























# EXPLICATIONS PLUS DÉTAILLÉES

#  Utilisez with pour ouvrir en lecture le fichier Ex2_Depenses_Janvier.txt
#  Utilisez with pour ouvrir en écriture un nouveau fichier que vous appellerez Ex2_Total_Janvier.txt
# 
#  dans ces deux with:
#       Commencez par écrire dans le fichier Ex1_Total_Janvier.txt la ligne d'entête:   "    MOIS    TOTAL" 
#       lisez le contenu de toutes les lignes du fichier de départ dans une variable

#       Créez une variable total_mensuel qui sera initialement à 0
#       Créez une variable ligne_a_imprimer qui sera initialement vide, soit ""

#       faites une boucle for pour lire chacune des lignes de ce contenu
#            Enlevez de la ligne lue les caractères de fin "\n"
#            Vérifiez le premier caractère de la ligne.
#            Si c'est '-', 
#                   ajoutez la ligne lue à la variable ligne_a_imprimer
#            Sinon,
#                   faites un split de la ligne sur le ':' pour obtenir une liste des parties de la ligne lue
#                   créez une variable montant_depense et donnez-lui la deuxième partie et castez le en un entier 
#                   ajoutez ce montant_depense à votre total_mensuel 
#       À la fin de la boucle, ajoutez ce montant à la ligne_a_imprimer
#       Écrivez la ligne_a_imprimez dans le fichier Ex1_TotalJanvier.txt         



        
