import R28_TP3_Choix_programme as Cs
import unittest

class Test_enregistrer_choix(unittest.TestCase ):
    # Les méthodes setUpClass et tearDownClass sont appelées automatiquement au début et à la fin de chaque test.
    # vous pouvez appeler l'instance choix_programme à partir de chaque méthode test en utilisant self.choix_programme
    @classmethod
    def setUpClass(cls):
        cls.choix_programme = Cs.appChoix()
    @classmethod
    def tearDownClass(cls):
        cls.choix_programme.destroy()
    def setUp(self):
        self.choix_programme.choix_1.set("Concordia_Genie")
        self.choix_programme.choix_2.set("DEUXIÈME CHOIX")
        self.choix_programme.choix_3.set("TROISIÈME CHOIX")
        self.choix_programme.matricule.delete(0,'end')
        self.choix_programme.lbl_message.configure(text = "Fais tes choix")
    
    # Test cas où tous les choix n'ont pas été effectuer.
    # Vérifie le contenu de lbl_message
    def test_1_enregistrer_choix_pas_de_choix(self):
        # Tester ce qui ce passe lorsqu'il n'y a pas de choix effectuer
        self.choix_programme.choix_1.set(value='PREMIER CHOIX')
        # Appeler la méthode enregistrer_choix() de choix_programme
        # Vérifier que la valeur lbl_message est bien "Vous devez faire trois choix de programmes" 
        # changer pour que choix_programme.choix_1 ait une valeur valide

        # refaite la vérification de lbl_message
        pass

    def test_2_enregistrer_choix_pas_de_choix_2(self):
        # Effectuer le même test que le test précédent.
        # Cette fois-ci, vérifier que le message est le bon lorsque self.choix_programme.choix_2 a comme valeur 'DEUXIÈME CHOIX'

        pass

    def test_3_enregistrer_choix_pas_de_matricule(self):
        # Donner des bonnes valeurs aux menus à option choix_1, choix_2, et choix_3
        # puis appeler la méthode enregistrer_choix()
        # le lbl_message devrait contenir un texte "Vous devez entrer votre matricule"
        pass

    def test_4_enregistrer_choix_2_choix_pareils_cas1(self):
        # Donner la même valeur aux menus à option choix_1 et choix_2
        # donner une valeur différente au menu à option choix_3
        # donner une valeur au matricule
        # appeler la méthode enregistrer_choix()
        # le lbl_message devrait contenir un texte "Vous devez choisir trois programmes différents"
        # répété ces opérations
        pass

    def test_5_enregistrer_choix_2_choix_pareils_cas2(self):
        # effectuer le même test que le précédent, mais avec les menus choix_1 et choix_3 ayant les mêmes valeurs
        pass

    def test_6_enregistrer_choix_2_choix_pareils_cas3(self):
        # effectuer le même test que le précédent, mais avec les menus choix_2 et choix_3 ayant les mêmes valeurs
        pass
    
    def test_7_enregistrer_choix_message_OK(self):
        # Donner des valeurs valides à tous les choix et au matricule.
        # appeler la méthode enregirster_choix()
        # vérifier le message dans lbl_message.
        pass
    
    # Extra ! + 1% de la note finale du cours.
    #Vérifier l'ajout d'une ligne au fichier choix_programmes_étudiants.csv.
    # Vous devez aussi vérifié que la ligne ajoutée correspond à vos attentes
    def test_ecriture_des_choix(self):
        pass




if __name__ == '__main__':
    unittest.main()
    #unittest.main(verbosity=2)    # Utiliser cette instruction pour plus de détails dans les tests
