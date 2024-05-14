import os, sys
testdir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '../')))

import unittest

import classes
from classes.constant import *
from classes import Ex2_Groupes_etudiants as Ge



class Test_ajouter_etudiant(unittest.TestCase):

    def test_ajouter_None(self):
       # Instanciez un etudiant
       # Instanciez un groupe avec cet etudiant
       # Testez l'ajout de None
       # Vérifiez que vous obtenez la bonne erreur
       self.fail("À faire")

    def test_ajouter_1_etudiant_ok(self):
        # Instanciez un etudiant
        # Instanciez un groupe avec cet etudiant
        # Instanciez un autre étudiant
        # Testez l'ajout de cet autre étudiant
        # Vérifiez que le dernier étudiant du groupe est celui que vous avez ajouté
        # Vérifiez que le nombre d'étudiants du groupe est maintenant de 2
       self.fail("À faire")

    def test_ajouter_1_etudiant_depasse_max(self):
        # Instanciez 3 étudiants
        # Instanciez un groupe avec une liste de 3 etudiants
        # Instanciez un autre étudiant
        # Testez l'ajout de cet autre étudiant
        # Vérifiez que vous obtenez la bonne erreur
       self.fail("À faire")


if __name__ == '__main__':
    unittest.main(verbosity=2)