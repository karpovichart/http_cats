from unittest import TestCase
from src.cats import Cats


class Testcats(TestCase):
    def test_choose_code(self):
        cat = Cats()
       # self.assertEqual(100, cat.choose_code(100))
        self.assertEqual(0, cat.choose_code(1))
