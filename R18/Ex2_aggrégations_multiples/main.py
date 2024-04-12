from ressources import * 
import datetime

if __name__ == "__main__" :
    #On peut appeler les classes contenue dans le répertoir ressources à partir d'ici.
    ex1_equipe = Equipe("Équipe 1", None)
    print(ex1_equipe.__dict__)


RYZE = Departement("RYZE", None)

print(RYZE.__dict__)