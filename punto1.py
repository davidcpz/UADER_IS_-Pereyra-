# getJason_refactor.py
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

import json
import sys

class JsonReader:
    _instance = None  # Atributo de clase para el Singleton

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JsonReader, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.json_key = 'token1'  # Clave por defecto que buscamos en el JSON

    def read_json_value(self, filepath):
        """
        Lee un archivo JSON y retorna el valor asociado a la clave json_key.
        Si hay un error, devuelve un mensaje de error controlado.
        """
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