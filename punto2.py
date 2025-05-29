# getJason_refactor.py
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

import json
import sys

class JsonReader:
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

def main():
    args = sys.argv[1:]  # Ignoramos el nombre del script

    if not args:
        print("Uso: python getJason_refactor.py <archivo.json> o -v para versión")
        sys.exit(1)

    if args[0] == "-v":
        print("Versión 1.1")
        sys.exit(0)

    reader = JsonReader()
    resultado = reader.read_json_value(args[0])
    print(resultado)

if __name__ == "__main__":
    main()



