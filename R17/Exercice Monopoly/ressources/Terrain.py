
class Terrain:
    def __init__(self,nom,type_terrain,couleur,coût,cout_maison,locations=[]) -> None:
        self.nom = nom
        self.type_terrain = type_terrain
        self.couleur = couleur
        self.prix_achat = coût
        self.cout_maison = cout_maison
        self.locations = locations
        self.prix_passage_actuel = self.locations[0]


#nom,type_terrain,couleur,espace,coût,hypothèque,cout_maison,location_0,location_1,location_2,location_3,location_4,location_hotel