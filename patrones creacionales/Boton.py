# abstract_factory.py

class Boton:
    def render(self):
        pass

class Ventana:
    def render(self):
        pass

# Botones y ventanas específicos
class BotonWindows(Boton):
    def render(self):
        print("Botón estilo Windows")

class VentanaWindows(Ventana):
    def render(self):
        print("Ventana estilo Windows")

class BotonLinux(Boton):
    def render(self):
        print("Botón estilo Linux")

class VentanaLinux(Ventana):
    def render(self):
        print("Ventana estilo Linux")

# Abstract Factory
class GUIFactory:
    def crear_boton(self): pass
    def crear_ventana(self): pass

class WindowsFactory(GUIFactory):
    def crear_boton(self):
        return BotonWindows()
    def crear_ventana(self):
        return VentanaWindows()

class LinuxFactory(GUIFactory):
    def crear_boton(self):
        return BotonLinux()
    def crear_ventana(self):
        return VentanaLinux()

# Ejemplo
if __name__ == "__main__":
    sistema = "windows"
    factory = WindowsFactory() if sistema == "windows" else LinuxFactory()

    boton = factory.crear_boton()
    ventana = factory.crear_ventana()
    boton.render()
    ventana.render()
