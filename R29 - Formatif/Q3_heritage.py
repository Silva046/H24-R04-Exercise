from abc import ABC, abstractmethod
from math import pi

class Forme(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def aire(self):
        pass
    
    @abstractmethod
    def périmètre():
        pass

class Cercle(Forme):
    def __init__(self, rayon) -> None:
        super().__init__()
        self.rayon = rayon
    
    def aire(self):
        return pi * self.rayon * self.rayon
    
    def périmètre(self):
        return 2 * pi * self.rayon
    
class Rectangle(Forme):
    def __init__(self, longueur, hauteur) -> None:
        super().__init__()
        self.longueur = longueur
        self.hauteur = hauteur
    
    def aire(self):
        return self.longueur * self.hauteur
    
    def périmètre(self):
        return (self.longueur * 2) + (self.hauteur * 2)

class Carré(Rectangle):
    def __init__(self, longueur) -> None:
        super().__init__(longueur=longueur, hauteur=longueur)

if __name__ == '__main__' :
    cercle1 , rect1, carré1 = Cercle(5), Rectangle(5,2), Carré(5)
    print(f"Cercle.  aire:{cercle1.aire()},  périmètre:{cercle1.périmètre()}")
    print(f"Rectangle.  aire:{rect1.aire()},  périmètre:{rect1.périmètre()}")
    print(f"Carré.  aire:{carré1.aire()},  périmètre:{carré1.périmètre()}")
