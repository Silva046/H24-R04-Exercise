import datetime
import random


class inscription :
    def __init__(self, alias, role):
        self.date_inscription = datetime.date.today()
        self.cout = 45
        self.no_confirmation = 0
        self.role = role
        self.alias = alias

    def confirmer(self):
        self.no_confirmation = random.randint(1,10000)
        print(f"Nous avons bien confirmer votre inscription, voici votre numero d'inscription : {self.no_confirmation}")

    def canceller(self):
        self.no_confirmation = 0
        print("Votre inscription a bel et bien été canceller")


gandalf = inscription("Gandalf the grey", "magicien")

aragorn = inscription("King of Gondor and Arnor", "King/Warrior")

gandalf.confirmer()
aragorn.confirmer()

gandalf.canceller()
aragorn.canceller()

print(gandalf.no_confirmation)
print(aragorn.no_confirmation)

