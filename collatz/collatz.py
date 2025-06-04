import matplotlib.pyplot as plt

def collatz_iterations(n):
    """Calcula el número de iteraciones para que n llegue a 1 siguiendo la conjetura de Collatz."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Calcular iteraciones para números del 1 al 10000
n_values = list(range(1, 10001))
iterations = [collatz_iterations(n) for n in n_values]

# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(iterations, n_values, s=1, color='blue', alpha=0.5)
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número Inicial")
plt.title("Iteraciones de la Conjetura de Collatz para n = 1 a 10000")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()