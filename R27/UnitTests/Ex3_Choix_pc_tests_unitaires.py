import os ,sys
testdir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '../')))

import unittest
import customtkinter as ctk

import classes
from classes.constant import *
from classes import Ex3_Choix_pc as Cpc


class Test_estimer(unittest.TestCase):

    def test_estimer_sans_processeur(self):
        # Instanciez la classe appChoix

        # Testez que self.choix_processeur =  "Choisis ton processeur    "

        #           faites l'appel de la méthode estimer()

        # Vérifier que self.lbl_message.Text = "Tu dois choisir un processeur"

        self.fail("À faire")

    def test_estimer_sans_carte_graphique(self):
        self.fail("À faire")

    def test_estimer_sans_RAM(self):
        self.fail("À faire")

    def test_estimer_les_3_choix(self):
        # Instanciez la classe Choix

        # donner le choix de processeur "AMD Ryzen 9 5950X         "

        # donner le choix de carte graphique "GeForce RTX 3090Ti        "

        # donner le choix de barrette RAM  "G.SKILL Trident Z5        "

        #        appeler la méthode estimer()
        
        # Vérifier que self.lbl_message.Text = "Pour tes choix, l'estimé est de 3720.26$."
       
        self.fail("À faire")
        
if __name__ == '__main__':
    unittest.main()