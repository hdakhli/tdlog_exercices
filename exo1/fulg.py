import unittest


class NoAmmunitionError(Exception):
    pass


class OutOfRangeError(Exception):
    pass


class Weapon:
    def _init_(self, ammunitions: int, range: int):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x: int, y: int, z: int):
        raise NotImplementedError("La méthode fire_at doit être implémentée dans les classes dérivées.")


class SurfaceMissileLauncher(Weapon):
    def _init_(self):
        super()._init_(50, 100)

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Le lance-missiles antisurface n'a plus de munitions.")

        if z != 0:
            raise OutOfRangeError("Le lance-missiles antisurface ne peut tirer qu'en surface (z=0).")

        # Code spécifique pour le tir avec un lance-missiles antisurface en surface (x, y, z=0)
        # Utilisez les coordonnées x, y pour déterminer la cible du tir
        # Vérifiez également si l'arme a suffisamment de munitions avant de tirer
        self.ammunitions -= 1
        print("Lance-missiles antisurface tire sur la cible ({}, {}, {})".format(x, y, z))


class AirMissileLauncher(Weapon):
    def _init_(self):
        super()._init_(40, 20)

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Le lance-missiles antiair n'a plus de munitions.")

        if z <= 0:
            raise OutOfRangeError("Le lance-missiles antiair ne peut tirer que dans les airs (z>0).")

        # Code spécifique pour le tir avec un lance-missiles antiair dans les airs (x, y, z>0)
        # Utilisez les coordonnées x, y, z pour déterminer la cible du tir
        # Vérifiez également si l'arme a suffisamment de munitions avant de tirer
        self.ammunitions -= 1
        print("Lance-missiles antiair tire sur la cible ({}, {}, {})".format(x, y, z))


class SubmarineTorpedoLauncher(Weapon):
    def _init_(self):
        super()._init_(24, 40)

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Le lance-torpilles sous-marin n'a plus de munitions.")

        if z > 0:
            raise OutOfRangeError("Le lance-torpilles sous-marin ne peut tirer que sous la surface (z<=0).")

        # Code spécifique pour le tir avec un lance-torpilles sous-marin (x, y, z<=0)
        # Utilisez les coordonnées x, y, z pour déterminer la cible du tir
        # Vérifiez également si l'arme a suffisamment de munitions avant de tirer
        self.ammunitions -= 1
        print("Lance-torpilles sous-marin tire sur la cible ({}, {}, {})".format(x, y, z))


class WeaponTestCase(unittest.TestCase):
    def setUp(self):
        # Créez une instance de chaque arme pour les tests
        self.surface_missile_launcher = SurfaceMissileLauncher()
        self.air_missile_launcher = AirMissileLauncher()
        self.submarine_torpedo_launcher = SubmarineTorpedoLauncher()

    def test_surface_missile_launcher_fire_at(self):
        self.surface_missile_launcher.ammunitions = 0
        with self.assertRaises(NoAmmunitionError):
            self.surface_missile_launcher.fire_at(10, 10, 0)

        with self.assertRaises(OutOfRangeError):
            self.surface_missile_launcher.fire_at(10, 10, 1)

        # Test réussi - munitions disponibles et coordonnées valides
        self.surface_missile_launcher.ammunitions = 10
        self.surface_missile_launcher.fire_at(10, 10, 0)

    def test_air_missile_launcher_fire_at(self):

        self.air_missile_launcher.ammunitions = 0
        with self.assertRaises(NoAmmunitionError):
            self.air_missile_launcher.fire_at(10, 10, 100)

        with self.assertRaises(OutOfRangeError):
            self.air_missile_launcher.fire_at(10, 10, 0)

        # Test réussi - munitions disponibles et coordonnées valides
        self.air_missile_launcher.ammunitions = 5
        self.air_missile_launcher.fire_at(10, 10, 100)

    def test_submarine_torpedo_launcher_fire_at(self):
        self.submarine_torpedo_launcher.ammunitions = 0
        with self.assertRaises(NoAmmunitionError):
            self.submarine_torpedo_launcher.fire_at(10, 10, -100)

        with self.assertRaises(OutOfRangeError):
            self.submarine_torpedo_launcher.fire_at(10, 10, 1)

        # Test réussi - munitions disponibles et coordonnées valides
        self.submarine_torpedo_launcher.ammunitions = 8
        self.submarine_torpedo_launcher.fire_at(10, 10, -10)


if __name__ == '__main__':
    unittest.main()