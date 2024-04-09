class Reservoir:
    def __init__(self, volume) -> None:
        self.volume = volume

    def __str__(self):
        return f"Le réservoir est de : {self.volume}"
    
    def __remplir(self, nbr):
        self.volume += nbr