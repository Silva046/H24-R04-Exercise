from abc import ABC, abstractmethod
from math import pi

class Forme: pass

class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
    
    def aire(self):
        return pi * self.rayon * self.rayon
    
    def périmètre(self):
        return 2 * pi * self.rayon
    
class Rectangle:
    def __init__(self,longueur,hauteur):
        self.longueur =longueur
        self.hauteur = hauteur
    
    def aire(self):
        return self.longueur * self.hauteur
    
    def périmètre(self):
        return (self.longueur * 2) + (self.hauteur * 2)

class Carré(Rectangle): pass


if __name__ == '__main__' :
    cercle1 , rect1, carré1 = Cercle(5), Rectangle(5,2), Carré(5)
    print(f"Cercle.  aire:{cercle1.aire()},  périmètre:{cercle1.périmètre()}")
    print(f"Rectangle.  aire:{rect1.aire()},  périmètre:{rect1.périmètre()}")
    print(f"Carré.  aire:{carré1.aire()},  périmètre:{carré1.périmètre()}")
