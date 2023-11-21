import unittest


class NoAmmunitionError(Exception):
    pass


class OutOfRangeError(Exception):
    pass


class Weapon:
    def __init__(self, ammunition: int, range: int):
        self.ammunition = ammunition
        self.range = range

    def fire_at(self, x: int, y: int, z: int):
        raise NotImplementedError("La méthode fire_at doit être implémentée dans les classes dérivées.")


class Lance_missile_anti_surface(Weapon):
    def __init__(self):
        super().__init__(50, 100)

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            self.ammunition -= 1
            raise NoAmmunitionError("Le lance-missiles antisurface n'a plus de munitions.")

        if z != 0:
            self.ammunition -= 1
            raise OutOfRangeError("Le lance-missiles antisurface ne peut tirer qu'en surface (z=0).")
        print("Lance-missiles antisurface tire sur la cible ({}, {}, {})".format(x, y, z))

class Lance_missile_anti_air(Weapon):
    def __init__(self):
        super().__init__(40, 20)

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            self.ammunition -= 1
            raise NoAmmunitionError("Le lance-missiles antiair n'a plus de munitions.")

        if z <= 0:
            self.ammunition -= 1
            raise OutOfRangeError("Le lance-missiles antiair ne peut tirer que dans les airs (z>0).")
        


class Lance_torpilles(Weapon):
    def __init__(self):
        super().__init__(24, 40)

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            self.ammunition -= 1
            raise NoAmmunitionError("Le lance-torpilles sous-marin n'a plus de munitions.")

        if z > 0:
            self.ammunition -= 1
            raise OutOfRangeError("Le lance-torpilles sous-marin ne peut tirer que sous la surface (z<=0).")
          