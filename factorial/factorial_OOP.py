class Factorial:
    """Clase para calcular factoriales."""
    def __init__(self, min_val=1, max_val=1):
        self.min_val = min_val
        self.max_val = max_val
    
    def calcular(self, num):
        """Calcula el factorial de un número."""
        if num < 0:
            raise ValueError("El factorial de un número negativo no existe.")
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact
    
    def run(self):
        """Calcula y muestra los factoriales en el rango especificado."""
        for i in range(self.min_val, self.max_val + 1):
            print(f"Factorial {i}! es {self.calcular(i)}")

# Entrada de usuario o argumento de línea de comandos
import sys
if len(sys.argv) < 2:
    num = input("Ingrese un número o rango (ej. 5, 3-7, -10, 4-): ")
else:
    num = sys.argv[1]

# Procesamiento de entrada
if "-" in num:
    partes = num.split("-")
    if partes[0] == "":  # Caso "-hasta"
        inicio, fin = 1, int(partes[1])
    elif partes[1] == "":  # Caso "desde-"
        inicio, fin = int(partes[0]), 60
    else:  # Caso "desde-hasta"
        inicio, fin = int(partes[0]), int(partes[1])
else:
    inicio = fin = int(num)

# Validación de rango
if inicio > fin or inicio < 0:
    print("Rango inválido. Asegúrese de que los valores sean correctos.")
else:
    Factorial(inicio, fin).run()
