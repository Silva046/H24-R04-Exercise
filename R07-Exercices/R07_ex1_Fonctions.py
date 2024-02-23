# Cet exercice est un retour sur les fonctions (notion vue en programmation 1)


# Q1 A:  Définir une fonction sans paramètre                                    #
#        Faites une fonction qui va imprimer "Bonjour" 
#        
def Bonjour():
    print("Bonjour!")

print(f"Q1{'_'*60}")
# Q1 B:   Appellez cette fonction  
Bonjour()



print(f"Q2{'_'*60}")
# Q2 A:   Définir une fonction avec paramètre
#         Faites une fonction qui va imprimer "Bonjour XXXXXX" où XXXXXX est le nom passé en paramètre lors de l'appel de cette fonction
#         Appelez-la bonjour_toi

def Bonjour_toi(nom_personne):
    print(f"Bonjour {nom_personne}")
 

# Q2 B:  Appel de la fonction bonjour_toi avec en paramètre le nom de mon ami Pierre
Bonjour_toi("Pierre")


# Q2 C:  Appel de la fonction bonjour_toi avec en paramètre le nom de mon amie Sylvie

Bonjour_toi("Sylvie")


print(f"Q3{'_'*60}")
# Q3 A:  Définir une fonction sans paramètre mais qui va retourner une valeur de retour      #
#        Faites une fonction qui va imprimer "Bonjour" et qui va retourner le message "Cela va?"
#        Appelez-la cela_va

def cela_va():
    print("Bonjour")
    return print("Cela va?")


# Q3 B:   Appel de la fonction et capture de la réponse

cela_va()


print(f"Q4{'_'*60}")
# Q4 A:  Définir une fonction avec paramètre et avec une valeur de retour      #
#        Faites une fonction qui va imprimer "Bonjour XXXXXX" où XXXXXX est le nom passé en paramètre lors de l'appel de cette fonction"
# 		 et qui va retourner le message "Je suis libre ce soir, et toi?"
#        Appelez-la cela_va_bien

def cela_va_bien(nom_personne):
    print(f"Bonjour {nom_personne}")
    return print("Je suis libre ce soir, et toi")



# Q4 B:   Appel de la fonction et capture de la réponse

cela_va_bien("Vincent")


