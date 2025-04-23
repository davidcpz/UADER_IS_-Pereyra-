# calculadora_impuestos.py

class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return base_imponible + iva + iibb + contribuciones

# Ejemplo de uso
if __name__ == "__main__":
    calculadora = CalculadoraImpuestos()
    print("Total con impuestos:", calculadora.calcular_total(1000))
