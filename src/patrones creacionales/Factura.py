# factura_factory.py
class Factura:
    def __init__(self, importe):
        self.importe = importe

    def mostrar(self):
        pass

class FacturaResponsable(Factura):
    def mostrar(self):
        print(f"Factura A - IVA Responsable - Total: {self.importe}")

class FacturaNoInscripto(Factura):
    def mostrar(self):
        print(f"Factura B - IVA No Inscripto - Total: {self.importe}")

class FacturaExento(Factura):
    def mostrar(self):
        print(f"Factura C - IVA Exento - Total: {self.importe}")

class FacturaFactory:
    @staticmethod
    def crear_factura(tipo, importe):
        if tipo == "responsable":
            return FacturaResponsable(importe)
        elif tipo == "no_inscripto":
            return FacturaNoInscripto(importe)
        elif tipo == "exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Condición impositiva no válida")

# Ejemplo
if __name__ == "__main__":
    f = FacturaFactory.crear_factura("responsable", 1500)
    f.mostrar()
