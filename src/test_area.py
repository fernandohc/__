from unittest import TestCase
from area import *

class TesteArea(TestCase):

    def test_calcular_area_quadrada(self):
        area = Area()
        area.lado1 = 5
        area.lado2 = 5
        self.assertEqual(25, area.quadrada())

    def test_area_quadrada_deve_lancar_excecao_ao_possuir_lado_com_tamanho_zero_ou_negativo(self):
        area = Area()
        area.lado1 = 5
        area.lado2 = 0
        with self.assertRaises(ValueError):
            area.quadrada() 

    def test_calcular_area_cubica(self):
        area = Area()
        area.lado1 = 2
        area.lado2 = 3
        area.lado3 = 4
        self.assertEqual(24, area.cubica())

    def test_area_cubica_deve_lancar_excecao_ao_possuir_lado_com_tamanho_zero_ou_negativo(self):
        area = Area()
        area.lado1 = 2
        area.lado2 = 3
        area.lado3 = -1
        with self.assertRaises(ValueError):
            area.cubica()
            