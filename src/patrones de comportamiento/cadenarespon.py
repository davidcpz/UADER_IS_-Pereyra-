# Clase base para los manejadores
class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Handler para números pares
class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} consumido por EvenHandler (par)")
        elif self.next_handler:
            self.next_handler.handle(number)

# Handler para números primos
class PrimeHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} consumido por PrimeHandler (primo)")
        elif self.next_handler:
            self.next_handler.handle(number)

# Handler para números no consumidos
class NullHandler(Handler):
    def handle(self, number):
        print(f"{number} NO CONSUMIDO por ninguna clase")

# Construcción de la cadena: Even → Prime → Null
handler_chain = EvenHandler(
    PrimeHandler(
        NullHandler()
    )
)

# Procesar los números del 1 al 100
for i in range(1, 101):
    handler_chain.handle(i)
