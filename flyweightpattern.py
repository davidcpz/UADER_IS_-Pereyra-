### Punto 5: Flyweight Pattern

class CaracterFlyweight:
    def __init__(self, caracter, fuente):
        self.caracter = caracter
        self.fuente = fuente

    def mostrar(self, posicion, color):
        print(f"Mostrando '{self.caracter}' en posición {posicion}, color {color}, fuente {self.fuente}.")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def obtener_flyweight(self, caracter, fuente):
        clave = (caracter, fuente)
        if clave not in self._flyweights:
            self._flyweights[clave] = CaracterFlyweight(caracter, fuente)
            print(f"Creando nuevo flyweight para '{caracter}' con fuente '{fuente}'.")
        return self._flyweights[clave]


# Ejemplo de ejecución Punto 5
if __name__ == "__main__":
    print("\n--- Punto 5: Flyweight Pattern ---")
    factory = FlyweightFactory()
    documento = [
        ("H", (0, 0), "negro"),
        ("o", (0, 1), "negro"),
        ("l", (0, 2), "negro"),
        ("a", (0, 3), "negro"),
        ("m", (0, 4), "azul"),
        ("u", (0, 5), "azul"),
        ("n", (0, 6), "azul"),
    ]
    fuente = "Arial"
    for caracter, posicion, color in documento:
        flyweight = factory.obtener_flyweight(caracter, fuente)
        flyweight.mostrar(posicion, color)