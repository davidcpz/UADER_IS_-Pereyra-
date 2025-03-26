#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    """Calcula el factorial de un número entero no negativo."""
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(inicio, fin):
    """Calcula y muestra los factoriales en un rango dado."""
    for i in range(inicio, fin + 1):
        print(f"Factorial {i}! es {factorial(i)}")

# Verificación de argumentos
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
    calcular_factoriales(inicio, fin)

