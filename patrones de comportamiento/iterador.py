# Clase que implementa el iterador en ambas direcciones
class StringIterable:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        # Iterador en orden directo
        return ForwardIterator(self.text)

    def reverse_iter(self):
        # Iterador en orden reverso
        return ReverseIterator(self.text)


# Iterador hacia adelante
class ForwardIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        return char


# Iterador hacia atrás
class ReverseIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.text[self.index]
        self.index -= 1
        return char


# --- Ejemplo de uso ---
cadena = StringIterable("ingenieria")

print("Recorrido normal:")
for ch in cadena:
    print(ch, end=" ")

print("\nRecorrido inverso:")
for ch in cadena.reverse_iter():
    print(ch, end=" ")
