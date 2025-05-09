### Punto 4: Decorator Pattern

class NumeroBase:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(f"Valor actual: {self.valor}")


class NumeroDecorator:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        self.numero.imprimir()


class SumarDosDecorator(NumeroDecorator):
    def imprimir(self):
        nuevo_valor = self.numero.valor + 2
        print(f"Valor después de sumar 2: {nuevo_valor}")


class MultiplicarPorDosDecorator(NumeroDecorator):
    def imprimir(self):
        nuevo_valor = self.numero.valor * 2
        print(f"Valor después de multiplicar por 2: {nuevo_valor}")


class DividirPorTresDecorator(NumeroDecorator):
    def imprimir(self):
        nuevo_valor = self.numero.valor / 3
        print(f"Valor después de dividir por 3: {nuevo_valor}")

        
# Ejemplo de ejecución Punto 4
if __name__ == "__main__":
    print("\n--- Punto 4: Decorator Pattern ---")
    numero = NumeroBase(9)
    numero.imprimir()
    suma = SumarDosDecorator(numero)
    suma.imprimir()
    multiplicar = MultiplicarPorDosDecorator(numero)
    multiplicar.imprimir()
    dividir = DividirPorTresDecorator(numero)
    dividir.imprimir()