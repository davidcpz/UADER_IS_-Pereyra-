# -*- coding: utf-8 -*-
# chatgpt_client.py
# Programa que permite consultar la API de ChatGPT desde la consola

import openai
import readline  # Permite usar flecha arriba para recuperar consultas anteriores
import os

# Configuración de la API Key (puede usarse directamente o desde variable de entorno)
openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # También se puede usar: openai.api_key = "sk-..."

# Mensaje de contexto para el asistente
context = "Sos un asistente útil que responde de forma clara y precisa."
model = "gpt-4o"  # Modelo a utilizar

# Función que solicita una consulta al usuario desde la terminal
def obtener_consulta():
    try:
        # Entrada del usuario
        consulta = input("Ingrese su consulta: ").strip()
        if not consulta:
            # Se lanza error si está vacía
            raise ValueError("La consulta está vacía.")
        print("You:", consulta)  # Muestra la entrada del usuario
        return consulta
    except Exception as e:
        # Manejo de errores en la entrada
        print("Error al ingresar la consulta:", e)
        return None

# Función que se conecta con la API de ChatGPT y muestra la respuesta
def invocar_chatgpt(consulta):
    try:
        # Llamada al API con parámetros básicos
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": consulta}
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Obtiene el contenido de la respuesta del asistente
        contenido = response['choices'][0]['message']['content']
        print("chatGPT:", contenido)
    except Exception as e:
        # Manejo de errores de red o API
        print("Error al invocar ChatGPT:", e)

# Función principal del programa
def main():
    while True:
        try:
            # Obtiene la consulta del usuario
            consulta = obtener_consulta()
            if consulta:
                # Llama al asistente si hay texto
                invocar_chatgpt(consulta)
        except KeyboardInterrupt:
            # Permite salir del programa con Ctrl+C
            print("\nSaliendo del programa.")
            break

# Punto de entrada del script
if __name__ == "__main__":
    main()