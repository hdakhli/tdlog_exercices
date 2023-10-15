import unittest

from exo



class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        item = Item(10, 20)

        self.assertEqual(20, item.weight)
