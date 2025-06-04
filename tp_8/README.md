# TP6 - Ingeniería Reversa, Re-factoría y Re-Ingeniería

## 📌 Descripción

Este trabajo práctico parte de un archivo compilado en Python (`getJason.pyc`) correspondiente a un sistema legado sin código fuente, que tenía como objetivo recuperar un token de acceso a microservicios bancarios almacenado en un archivo `sitedata.json`.

El objetivo fue aplicar los pasos de ingeniería reversa, realizar la decompilación, adaptar el código para permitir su reuso, y validar su funcionamiento mediante casos de prueba.

---

## 🔁 Cambios realizados

1. **Decompilación** del archivo `getJason.pyc` usando PyLingual.
2. **Refactorización** del código para:
   - Aceptar una clave (`key`) como argumento opcional.
   - Usar `"token1"` como valor por defecto.
   - Mostrar mensajes claros de error si la clave o el archivo no existen.
   - Mejorar la legibilidad y documentación del código.
3. **Validación** mediante pruebas funcionales.

---

## 🧪 Casos de prueba

Se usó el siguiente archivo `sitedata.json`:

```json
{
    "token1": "C598-ECF9-F0F7-881A",
    "token2": "C598-ECF9-F0F7-881B",
    "token3": "Boca Juniors"
}
