# getJason_refactor.py
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.



#getJason_refactor.py
#Trabajo Práctico 7 – Ingeniería Reversa, Re-factoría y Re-Ingeniería

#Este programa lee un archivo JSON desde línea de comandos y devuelve
#el valor de la clave 'token1'. Incluye manejo de errores controlado
#y puede ejecutarse con la opción '-v' para mostrar la versión.

#Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

# pylint: disable=R0903,C0114,C0115,C0116,W0718

import json
import sys

class JsonReader:
    #Clase Singleton que encapsula la lectura de un archivo JSON.
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JsonReader, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.json_key = 'token1'

    def read_json_value(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return str(data[self.json_key])
        except FileNotFoundError:
            return "Error: archivo no encontrado."
        except json.JSONDecodeError:
            return "Error: el archivo no es un JSON válido."
        except KeyError:
            return f"Error: clave '{self.json_key}' no encontrada en el archivo JSON."
        except Exception as e:
            return f"Error inesperado: {str(e)}"
        


def legacy_run(filepath):
    
   # Simula el comportamiento del script original (getJason.py),
    #pero redirige la lógica al nuevo sistema (JsonReader).
    reader = JsonReader()
    print(reader.read_json_value(filepath))


def main():
    # Función principal. Lee argumentos desde consola y ejecuta
    #el lector JSON o muestra la versión si se pasa el argumento '-v'.
    args = sys.argv[1:]  # Ignoramos el nombre del script

    if not args:
        print("Uso: python punto2.py <archivo.json> o -v para versión")
        sys.exit(1)

    if args[0] == "-v":
        print("Versión 1.1")
        sys.exit(0)

   # reader = JsonReader()
   # resultado = reader.read_json_value(args[0])
    #print(resultado)

    legacy_run(args[0])


if __name__ == "__main__":
    main()
