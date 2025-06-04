# hamburguesa_factory.py

class Hamburguesa:
    def entregar(self):
        pass

class Mostrador(Hamburguesa):
    def entregar(self):
        print("Entregada en mostrador.")

class RetiroCliente(Hamburguesa):
    def entregar(self):
        print("Retirada por el cliente.")

class Delivery(Hamburguesa):
    def entregar(self):
        print("Enviada por delivery.")

class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa(tipo):
        if tipo == "mostrador":
            return Mostrador()
        elif tipo == "retiro":
            return RetiroCliente()
        elif tipo == "delivery":
            return Delivery()
        else:
            raise ValueError("Tipo de entrega no válido")

# Ejemplo de uso
if __name__ == "__main__":
    h = HamburguesaFactory.crear_hamburguesa("delivery")
    h.entregar()
