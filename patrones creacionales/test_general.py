# test_general.py
from FactorialSingleton import FactorialSingleton
from CalculadoraImpuesto import CalculadoraImpuestos
from Hamburguesa import HamburguesaFactory
from Factura import FacturaFactory
from Avion import AvionBuilder
from Prototipo import Prototipo
from Boton import WindowsFactory, LinuxFactory

def test_all():
    print("== Factorial Singleton ==")
    f = FactorialSingleton()
    print(f.factorial(5))

    print("\n== Impuestos ==")
    c = CalculadoraImpuestos()
    print(c.calcular_total(1000))

    print("\n== Hamburguesa ==")
    h = HamburguesaFactory.crear_hamburguesa("delivery")
    h.entregar()

    print("\n== Factura ==")
    factura = FacturaFactory.crear_factura("exento", 1500)
    factura.mostrar()

    print("\n== Avión ==")
    builder = AvionBuilder()
    builder.construir_body()
    builder.construir_turbinas()
    builder.construir_alas()
    builder.construir_tren_aterrizaje()
    avion = builder.obtener_avion()
    avion.mostrar()

    print("\n== Prototipo ==")
    original = Prototipo("Original")
    copia = original.clonar()
    print(copia.nombre)

    print("\n== Abstract Factory (Windows) ==")
    factory = WindowsFactory()
    factory.crear_boton().render()
    factory.crear_ventana().render()

test_all()
