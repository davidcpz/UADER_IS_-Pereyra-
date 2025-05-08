# Trabajo Práctico: Patrones Estructurales (README)

## Descripción

Este proyecto contiene la implementación de distintos patrones estructurales en Python, correspondientes a un trabajo práctico para Ingeniería en Sistemas.

## Contenido

### Punto 1: Proxy Pattern
Implementa un `PingProxy` que actúa como intermediario para realizar pings. Si la IP es `192.168.0.254`, redirige el ping a `www.google.com`; de lo contrario, verifica si la IP comienza con `192.` antes de hacer ping.

**Ejecución:**
Se prueban tres casos: IP válida, IP especial, e IP inválida.

---

### Punto 2: Bridge Pattern
Modela la producción de láminas de acero usando dos trenes laminadores: uno de 5 metros y otro de 10 metros. La clase `Lamina` abstrae la lámina y delega la producción al laminador correspondiente.

**Ejecución:**
Se crean dos láminas y se producen con ambos trenes laminadores.

---

### Punto 3: Composite Pattern
Representa una estructura jerárquica con un producto principal formado por sub-conjuntos, cada uno con varias piezas. Permite mostrar toda la estructura anidada.

**Ejecución:**
Se construye la estructura inicial (3 sub-conjuntos de 4 piezas cada uno) y luego se añade un sub-conjunto opcional.

---

### Punto 4: Decorator Pattern
Permite decorar un número para modificar su impresión aplicando operaciones como sumar 2, multiplicar por 2 y dividir por 3.

**Ejecución:**
Se muestra el número original y luego con cada decorador aplicado.

---

### Punto 5: Flyweight Pattern

Un ejemplo clásico donde el patrón Flyweight sería útil es en un procesador de texto. Este tipo de aplicaciones manejan documentos que pueden contener millones de caracteres. Si cada carácter (como 'a', 'b', 'c', etc.) fuera representado por un objeto independiente, el consumo de memoria sería muy alto, especialmente considerando que muchos de esos caracteres son iguales (por ejemplo, la letra 'e' puede aparecer miles de veces en un solo documento).

## codigo del patron

Simula un editor de texto donde los caracteres son flyweights compartidos para optimizar el uso de memoria. Cada carácter es mostrado con su posición y color.

**Ejecución:**
Se simula la impresión de un pequeño texto, creando flyweights solo una vez por carácter.

---