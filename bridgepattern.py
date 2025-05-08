class Laminador:
    def producir(self, lamina):
        raise NotImplementedError()


class TrenLaminador5Mts(Laminador):
    def producir(self, lamina):
        print(f"Produciendo lámina de {lamina.espesor} pulgadas de espesor y {lamina.ancho} metros de ancho en plancha de 5 metros de largo.")


class TrenLaminador10Mts(Laminador):
    def producir(self, lamina):
        print(f"Produciendo lámina de {lamina.espesor} pulgadas de espesor y {lamina.ancho} metros de ancho en plancha de 10 metros de largo.")


class Lamina:
    def __init__(self, espesor: float, ancho: float, laminador: Laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.laminador = laminador

    def producir(self):
        self.laminador.producir(self)


# Ejemplo de ejecución Punto 2
if __name__ == "__main__":
    print("\n--- Punto 2: Bridge Pattern ---")
    tren5 = TrenLaminador5Mts()
    tren10 = TrenLaminador10Mts()
    lamina1 = Lamina(0.5, 1.5, tren5)
    lamina2 = Lamina(0.5, 1.5, tren10)
    lamina1.producir()
    lamina2.producir()