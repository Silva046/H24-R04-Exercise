class ErreurFormatIP : pass


class AdresseIP :
    def __init__(self, pAdresse_ip) -> None: pass


    def __str__(self) -> str :
        return self.valeur
    # Permet de faire des comparaissons d'égalité entre deux adresses IP
    def __eq__(self, autre_adresse:"AdresseIP") -> bool:
        return self._valeur == autre_adresse._valeur



if __name__ == '__main__' :
    # Ici une série de tests vous sont déjà donnés
    # Création de 3 adresses IP
    ad1 = AdresseIP("255.255.10.10")
    ad2 = AdresseIP("255.255.10.20")
    ad3 = AdresseIP("255.255.10.20")

    if ad1 == ad2 : raise Exception("Oops ! Les addresses ad1 et ad2 ne devrait pas êtres équivalentes")
    if ad2 != ad3 : raise Exception("Oops ! Les addresses ad2 et ad3 devrait ÊTRES équivalentes")
    
    adresse_invalides = ["255.255.255","256.255.10.10","255.255.255.10.10","255.255.10.-1"]
    for ip in adresse_invalides:
        try : new_ip = AdresseIP(ip)
        except ErreurFormatIP : continue
        except: raise Exception("Mauvais type d'exception est levé.")
    
    for ip in adresse_invalides:
        try : ad1.valeur = ip
        except ErreurFormatIP : continue
        except: raise Exception("Mauvais type d'exception est levé.")
