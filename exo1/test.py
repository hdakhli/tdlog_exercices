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
        self.lance_missile_anti_surface = Lance_missile_anti_surface()
        self.lance_missile_anti_air = Lance_missile_anti_air()
        self.lance_torpilles = Lance_torpilles()

    def test_Lance_missile_anti_surface_fire_at(self):
        self.lance_missile_anti_surface.ammunition = 0
        with self.assertRaises(NoAmmunitionError):
            self.lance_missile_anti_surface.fire_at(10, 10, 0)

        with self.assertRaises(OutOfRangeError):
            self.lance_missile_anti_surface.fire_at(10, 10, 1)

        # Test réussi - munitions disponibles et coordonnées valides
        self.lance_missile_anti_surface.ammunition = 10
        self.lance_missile_anti_surface.fire_at(10, 10, 0)

    def test_Lance_missile_anti_air_fire_at(self):

        self.lance_missile_anti_air.ammunition = 0
        with self.assertRaises(NoAmmunitionError):
            self.lance_missile_anti_air.fire_at(10, 10, 100)

        with self.assertRaises(OutOfRangeError):
            self.lance_missile_anti_air.fire_at(10, 10, 0)

        # Test réussi - munitions disponibles et coordonnées valides
        self.lance_missile_anti_air.ammunition = 5
        self.lance_missile_anti_air.fire_at(10, 10, 100)

    def test_Lance_torpilles_fire_at(self):
        self.lance_torpilles.ammunition = 0
        with self.assertRaises(NoAmmunitionError):
            self.lance_torpilles.fire_at(10, 10, -100)

        with self.assertRaises(OutOfRangeError):
            self.lance_torpilles.fire_at(10, 10, 1)

        # Test réussi - munitions disponibles et coordonnées valides
        self.lance_torpilles.ammunition = 8
        self.lance_torpilles.fire_at(10, 10, -10)

if __name__ == '__main__':
    unittest.main()
    
    
