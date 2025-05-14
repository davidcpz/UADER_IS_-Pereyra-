import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo State con interfaz por consola
#*--------------------------------------------------------------------

# Clase base para los estados
class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

# Estado AM
class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

# Estado FM
class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

# Clase principal Radio
class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate  # Inicia en FM

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

# Programa principal con interfaz por consola
if __name__ == "__main__":
    os.system("clear")
    print("=== Radio interactiva (consola) ===")
    radio = Radio()

    while True:
        print("\n-------------------------")
        print("Estás en modo: {}".format(radio.state.name))
        print("1. Escanear estación (scan)")
        print("2. Cambiar AM/FM (toggle_amfm)")
        print("0. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            radio.scan()
        elif opcion == "2":
            radio.toggle_amfm()
        elif opcion == "0":
            print("Apagando la radio.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
