
class Area():

    def quadrada(self):
        if self.lado1 > 0 and self.lado2 > 0:
            return self.lado1 * self.lado2
        else:
            raise ValueError("Nenhum dos lados pode ter valor negativo ou igual a 0")

    def cubica(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return self.lado1 * self.lado2 * self.lado3
        else:
            raise ValueError("Nenhum dos lados pode ter valor negativo ou igual a 0")
