from unittest import TestCase
from area import *

class TesteArea(TestCase):

    def test_calcular_area_quadrada(self):
        area = Area()
        area.lado1 = 5
        area.lado2 = 5
        self.assertEqual(25, area.quadrada())

    def test_calcular_area_cubica(self):
        area = Area()
        area.lado1 = 2
        area.lado2 = 3
        area.lado3 = 4
        self.assertEqual(24, area.cubica())
    