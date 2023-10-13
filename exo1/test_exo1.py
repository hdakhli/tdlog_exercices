import unittest
from exo1 import Item

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = Item("Widget", 10.0)
        self.assertEqual(item.name, "Widget")
        self.assertEqual(item.price, 10.0)

if __name__ == '__main__':
    unittest.main()
