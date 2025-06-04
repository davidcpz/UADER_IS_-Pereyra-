# Clase Subject (el emisor)
class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit_id(self, id_code):
        print(f"\nEmitiendo ID: {id_code}")
        for obs in self.observers:
            obs.notify(id_code)


# Clase base para Observers
class Observer:
    def __init__(self, expected_id):
        self.expected_id = expected_id

    def notify(self, emitted_id):
        if emitted_id == self.expected_id:
            print(f"→ Coincidencia: {emitted_id} fue recibido por {self.__class__.__name__}")


# Observers con IDs específicos
class ObserverA(Observer):
    def __init__(self):
        super().__init__("AB12")

class ObserverB(Observer):
    def __init__(self):
        super().__init__("CD34")

class ObserverC(Observer):
    def __init__(self):
        super().__init__("EF56")

class ObserverD(Observer):
    def __init__(self):
        super().__init__("GH78")


# ---- Ejemplo de uso ----

subject = Subject()

# Se suscriben 4 observers
subject.subscribe(ObserverA())
subject.subscribe(ObserverB())
subject.subscribe(ObserverC())
subject.subscribe(ObserverD())

# Emitimos 8 IDs, al menos 4 deben coincidir
ids_to_emit = ["AB12", "ZZ99", "CD34", "XY22", "EF56", "AA00", "GH78", "WW11"]

for id_code in ids_to_emit:
    subject.emit_id(id_code)
