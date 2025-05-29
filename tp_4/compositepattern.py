### Punto 3: Composite Pattern

class Componente:
    def mostrar(self, indent=0):
        raise NotImplementedError()


class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, indent=0):
        print(" " * indent + f"Pieza: {self.nombre}")


class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, indent=0):
        print(" " * indent + f"SubConjunto: {self.nombre}")
        for comp in self.componentes:
            comp.mostrar(indent + 4)

# Ejemplo de ejecución Punto 3
if __name__ == "__main__":
    print("\n--- Punto 3: Composite Pattern ---")
    producto = SubConjunto("Producto Principal")
    for i in range(1, 4):
        subconjunto = SubConjunto(f"SubConjunto {i}")
        for j in range(1, 5):
            pieza = Pieza(f"Pieza {j} del SubConjunto {i}")
            subconjunto.agregar(pieza)
        producto.agregar(subconjunto)
    producto.mostrar()
    subconjunto_opcional = SubConjunto("SubConjunto Opcional")
    for j in range(1, 5):
        pieza = Pieza(f"Pieza {j} del SubConjunto Opcional")
        subconjunto_opcional.agregar(pieza)
    producto.agregar(subconjunto_opcional)
    print("\nEstructura con el sub-conjunto opcional:")
    producto.mostrar()