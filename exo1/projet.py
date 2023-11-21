from main import Weapon
from main import Lance_missile_anti_surface
from main import Lance_missile_anti_air
from main import Lance_torpilles
from main import NoAmmunitionError
from main import OutOfRangeError
import unittest


class WeaponTestCase(unittest.TestCase):
    def setUp(self):
        # Créez une instance de chaque arme pour les tests
        self.surface_missile_launcher = Lance_missile_anti_surface()
        self.air_missile_launcher = Lance_missile_anti_air()
        self.submarine_torpedo_launcher = Lance_torpilles()

    def test_surface_missile_launcher_fire_at(self):
        self.Lance_missile_anti_surface.ammunition = 0
        with self.assertRaises(NoAmmunitionError):
            self.Lance_missile_anti_surface.fire_at(10, 10, 0)

        with self.assertRaises(OutOfRangeError):
            self.Lance_missile_anti_surface.fire_at(10, 10, 1)

        # Test réussi - munitions disponibles et coordonnées valides
        self.Lance_missile_anti_surface.ammunition = 10
        self.Lance_missile_anti_surface.fire_at(10, 10, 0)

    def test_air_missile_launcher_fire_at(self):

        self.air_missile_launcher.ammunition = 0
        with self.assertRaises(NoAmmunitionError):
            self.Lance_missile_anti_air.fire_at(10, 10, 100)

        with self.assertRaises(OutOfRangeError):
            self.Lance_missile_anti_air.fire_at(10, 10, 0)

        # Test réussi - munitions disponibles et coordonnées valides
        self.Lance_missile_anti_air.ammunition = 5
        self.Lance_missile_anti_air.fire_at(10, 10, 100)

    def test_submarine_torpedo_launcher_fire_at(self):
        self.Lance_torpilles.ammunition = 0
        with self.assertRaises(NoAmmunitionError):
            self.Lance_torpilles.fire_at(10, 10, -100)

        with self.assertRaises(OutOfRangeError):
            self.Lance_torpilles.fire_at(10, 10, 1)

        # Test réussi - munitions disponibles et coordonnées valides
        self.Lance_torpilles.ammunition = 8
        self.Lance_torpilles.fire_at(10, 10, -10)

if __name__ == 'main':
    unittest.main()