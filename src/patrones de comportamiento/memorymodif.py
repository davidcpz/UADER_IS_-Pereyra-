import os

#*--------------------------------------------------------------------
#* Design pattern memento con historial de versiones
#*-------------------------------------------------------------------

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self.history = []

    def save(self, writer):
        self.history.append(writer.save())

    def list_versions(self):
        print("\nHistorial de versiones:")
        for i, m in enumerate(self.history):
            print(f"[{i}] - {len(m.content)} caracteres guardados")

    def undo(self, writer, version_index):
        if 0 <= version_index < len(self.history):
            writer.undo(self.history[version_index])
        else:
            print("Versión no válida.")


# ---------------------- MAIN ----------------------

if __name__ == '__main__':
    os.system("clear")
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    while True:
        print("\n=== Editor de texto con historial (Memento) ===")
        print("1. Escribir texto")
        print("2. Guardar versión")
        print("3. Listar versiones")
        print("4. Volver a una versión anterior")
        print("5. Mostrar contenido actual")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            texto = input("Escribí el texto a agregar:\n> ")
            writer.write(texto + "\n")

        elif opcion == "2":
            caretaker.save(writer)
            print("Versión guardada.")

        elif opcion == "3":
            caretaker.list_versions()

        elif opcion == "4":
            caretaker.list_versions()
            try:
                idx = int(input("Ingrese el número de versión a la que desea volver: "))
                caretaker.undo(writer, idx)
                print("Se restauró la versión seleccionada.")
            except ValueError:
                print("Entrada no válida.")

        elif opcion == "5":
            print("\nContenido actual del archivo simulado:")
            print("---------------------------------------")
            print(writer.content)

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")
