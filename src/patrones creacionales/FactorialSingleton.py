# factorial_singleton.py

class FactorialSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialSingleton, cls).__new__(cls)
        return cls._instance

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

# Ejemplo de uso
if __name__ == "__main__":
    f1 = FactorialSingleton()
    f2 = FactorialSingleton()
    print("¿Misma instancia?", f1 is f2)
    print("Factorial de 5:", f1.factorial(5))
