class compte:
    def __init__(self, no_compte, type_compte, nip_compte):
        self.no_compte = no_compte
        self.type_compte = type_compte
        self.nip_compte = nip_compte
        self.solde = 0

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant_enlever):
        if montant_enlever > self.solde:
            print(f"{self.solde} est plus petit que {montant_enlever} que vous voulez retirer")
        self.solde -= montant_enlever
        
compte1 = compte(12345678,"chèque",8888)
compte2 = compte(23456789,"épargne",8888)

compte1.deposer(1000)
compte1.deposer(2000)

compte2.deposer(5000)

print(compte1.solde)
print(compte2.solde)