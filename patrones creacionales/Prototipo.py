# prototipo.py
import copy

class Prototipo:
    def __init__(self, nombre):
        self.nombre = nombre

    def clonar(self):
        return copy.deepcopy(self)

# Ejemplo de uso
if __name__ == "__main__":
    original = Prototipo("Objeto original")
    copia = original.clonar()
    copia2 = copia.clonar()
    print("Original:", original.nombre)
    print("Copia 1:", copia.nombre)
    print("Copia 2:", copia2.nombre)
