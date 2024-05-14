import os
import sys
testdir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '../')))

import unittest
import classes
from classes.constant import *
from classes import Thermostat

class Test_initialisation(unittest.TestCase):

    def test_temperature_initial(self):
        nouveau_thermostat = Thermostat()
        self.assertEqual(nouveau_thermostat._temperature, TEMPERATURE_INITIALE)

    def test_initialisation_temperature_trop_elevee(self):
        with self.assertRaises(expected_exception=ValueError):
            nouveau_thermostat = Thermostat.from_temperature(MAX_TEMPERATURE+4)

    def test_initialisation_temperature_trop_basse(self):
        with self.assertRaises(expected_exception=ValueError):
            nouveau_thermostat = Thermostat.from_temperature(MIN_TEMPERATURE-2)

    def test_initialisation_bonne_temperature(self):
        nouveau_thermostat = Thermostat.from_temperature(22)
        self.assertEqual(22, nouveau_thermostat.temperature)

#@unittest.skip
class test_modification_de_temperature(unittest.TestCase):

    def test_changer_temperature_trop_elevee(self):
       self.fail("À faire")
    def test_changer_temperature_trop_basse(self):
       self.fail("À faire")
    def test_changer_temperature_valide(self):
       self.fail("À faire")
     
    def test_augmenter_1_degre(self):
       self.fail("À faire")
    def test_augmenter_100_degre(self):
       self.fail("À faire")
    
    def test_diminuer_1_degre(self):
       self.fail("À faire")
    def test_diminuer_100_degre(self):
       self.fail("À faire")



if __name__ == '__main__':
    unittest.main(verbosity=2)