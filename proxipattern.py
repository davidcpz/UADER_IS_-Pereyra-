### Punto 1: Proxy Pattern

class Ping:
    def execute(self, ip: str):
        if ip.startswith("192."):
            print(f"Ejecutando ping a {ip} (con control de IP):")
            for i in range(1, 11):
                print(f"Intento {i}: Haciendo ping a {ip}")
        else:
            print(f"ERROR: La IP {ip} no es válida. Solo se permiten IPs que comiencen con '192.'")

    def executefree(self, ip: str):
        print(f"Ejecutando ping a {ip} (sin control de IP):")
        for i in range(1, 11):
            print(f"Intento {i}: Haciendo ping a {ip}")


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print(f"Proxy detectó la IP especial {ip}, redirigiendo a www.google.com usando executefree")
            self.ping.executefree("www.google.com")
        else:
            print(f"Proxy reenvía la solicitud a {ip}")
            self.ping.execute(ip)

            
# Ejemplo de ejecución Punto 1
if __name__ == "__main__":
    print("--- Punto 1: Proxy Pattern ---")
    proxy = PingProxy()
    proxy.execute("192.168.1.1")  # Caso normal
    proxy.execute("192.168.0.254")  # Caso especial
    proxy.execute("10.0.0.1")  # Caso inválido