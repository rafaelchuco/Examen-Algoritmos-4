# 🎓✨ Examen de Estructuras de Datos y Algoritmos 🌟📚

¡Bienvenido al examen definitivo basado en Python! 🚀 Cada semana contiene 2 desafíos emocionantes 🔥 enfocados en un tema específico. Los estudiantes implementarán funciones, validarán entradas y pasarán las pruebas dadas. ¡A continuación está la Semana 1 (o1) con sus dos desafíos dinámicos! 🎉🧩

---
## o1: Desafíos de Complejidad Algorítmica 📈⏱️

Este documento presenta dos desafíos fundamentales para comprender y aplicar diferentes complejidades algorítmicas: **logarítmica O(log n)** y **constante O(1)**.

---

### o1.1 🧩 **Conteo de Duplicaciones para Exceder N** 🔢➕📈

#### 🎯 Objetivo del Problema

Implementa la función `logarithmic_complexity(n)` que cuenta cuántas veces debes **duplicar** el número 1 para que supere el valor `n`. La función debe devolver tanto el conteo como el tiempo de ejecución.

#### 📋 Especificaciones Técnicas

**Firma de la función:**
```python
logarithmic_complexity(n: int) → (int, float)
```

**Parámetros de entrada:**
- `n`: número entero positivo (≥ 1) 🎯

**Valores de retorno:**
- **count**: número de duplicaciones necesarias para que `valor > n` 🔼
- **time**: tiempo transcurrido en segundos (tipo float) ⏱️

**Complejidad temporal esperada:** **O(log n)** 📊

#### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 1` → count = 1 (porque 1×2 = 2 > 1) ⚠️
- Valores muy grandes de `n` (hasta 10⁹) 🔧

**Restricciones obligatorias:**
- ✅ Debe usar un bucle que duplique un total acumulativo
- 🚫 **NO** usar funciones logarítmicas del módulo `math`

**Validación de entrada:**
- Si `n` no es un entero o `n < 1`, devolver un indicador de error (ej: `-1` para count) más el tiempo transcurrido ❌⚙️

#### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o1.1.1** | `n = 1` | `(1, time)` | Caso base: 1×2 > 1 🌱 |
| **o1.1.2** | `n = 10` | `(4, time)` | Secuencia: 1→2→4→8→16 🌟 |
| **o1.1.3** | `n = 100` | `(7, time)` | Llega hasta 128 🔥 |
| **o1.1.4** | `n = 5` | `(int, float)` | Verificación de tipos 🧐 |
| **o1.1.5** | `n = "a"` o `n = -3` | `(-1, float)` | Manejo de errores ⚠️ |

#### 💻 Base Code 🖥️

```python
import time

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def logarithmic_complexity(n):
    """🔢 Count doublings of 1 to exceed n; return (count, elapsed_time).
    If input invalid (not int or < 1), return (-1, elapsed_time)."""
    start = time.time()
    # Your solution here 🛠️
    end = time.time()
    elapsed = end - start
    return None, elapsed  # replace None with your count or -1 on invalid

def test_o1_1():
    # o1.1.1: n = 1 → count = 1
    cnt, _ = logarithmic_complexity(1)
    record_test("o1.1.1 n=1 → count==1", cnt == 1)
    # o1.1.2: n = 10 → count = 4
    cnt, _ = logarithmic_complexity(10)
    record_test("o1.1.2 n=10 → count==4", cnt == 4)
    # o1.1.3: n = 100 → count = 7
    cnt, _ = logarithmic_complexity(100)
    record_test("o1.1.3 n=100 → count==7", cnt == 7)
    # o1.1.4: Type-check test
    out = logarithmic_complexity(5)
    record_test(
        "o1.1.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float)
    )
    # o1.1.5: Error-handling test
    cnt_err, _ = logarithmic_complexity("a")
    record_test("o1.1.5 invalid input returns -1", cnt_err == -1)

# 🚀 Run tests
test_o1_1()

# 📋 Summary
for r in test_results:
    print(r)
```

#### 💡 Guía de Implementación

**Estructura del bucle recomendada:**
```python
value = 1
count = 0
while value <= n:
    value *= 2  ## 🔼 duplicar valor
    count += 1  ## ➕ incrementar contador
```

**Medición de tiempo:**
- Usar `time.time()` antes y después del algoritmo ⏱️

**¿Por qué es O(log n)?**
- Cada iteración duplica el valor, reduciendo exponencialmente el espacio de búsqueda 🔍

**Validación de entrada:**
```python
if not isinstance(n, int) or n < 1:
    return -1, elapsed
```

#### 🧠 Importancia y Aplicaciones

- **Fundamentos teóricos:** Demuestra el crecimiento logarítmico, crucial en **búsqueda binaria** y **divide y vencerás** 🌳
- **Estrategias algorítmicas:** Ayuda a elegir entre enfoques iterativos vs. recursivos 🔄
- **Aplicaciones reales:** Patrones de duplicación en **redimensionamiento de datos** y **retroceso exponencial** 🔧
- **Análisis de complejidad:** Desarrolla confianza en el escalado algorítmico 📏💡

---

### o1.2 🧩 **Suma de los Primeros N Números Naturales** ➕📊⏱️

#### 🎯 Objetivo del Problema

Implementa la función `constant_sum(n)` que calcula la suma de los primeros `n` números naturales en **tiempo constante**, devolviendo el resultado y el tiempo de ejecución.

#### 📋 Especificaciones Técnicas

**Firma de la función:**
```python
constant_sum(n: int) → (int, float)
```

**Parámetros de entrada:**
- `n`: número entero no negativo (≥ 0) 🎯

**Valores de retorno:**
- **sum**: resultado de `1 + 2 + … + n` ➕
- **time**: tiempo transcurrido en segundos (tipo float) ⏱️

**Complejidad temporal esperada:** **O(1)** 🛑

#### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 0` → sum = 0 ⚠️
- Valores muy grandes de `n` (hasta 10⁸) 🔧

**Restricciones obligatorias:**
- ✅ Debe usar la **fórmula matemática** `n*(n+1)//2`
- 🚫 **NO** usar bucles para sumar todos los números

**Validación de entrada:**
- Si `n` no es un entero o `n < 0`, devolver un indicador de error (ej: `-1` para sum) más el tiempo transcurrido ❌⏱️

#### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o1.2.1** | `n = 0` | `(0, time)` | Caso base: suma vacía 🌱 |
| **o1.2.2** | `n = 1` | `(1, time)` | Un solo elemento 🌟 |
| **o1.2.3** | `n = 10` | `(55, time)` | Suma 1+2+...+10 🔥 |
| **o1.2.4** | `n = 5` | `(int, float)` | Verificación de tipos 🧐 |
| **o1.2.5** | `n = "a"` o `n = -3` | `(-1, float)` | Manejo de errores ⚠️ |

#### 💻 Base Code 🖥️

```python
import time

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def constant_sum(n):
    """🔢 Compute sum of 1..n in O(1), return (sum, elapsed_time).
    If input invalid (not int or < 0), return (-1, elapsed_time)."""
    start = time.time()
    #Your solution here 🛠️
    end = time.time()
    elapsed = end - start
    return None, elapsed  #replace None with your sum or -1 on invalid

def test_o1_2():
    #o1.2.1: n = 0 → sum = 0
    s, _ = constant_sum(0)
    record_test("o1.2.1 n=0 → sum==0", s == 0)
    #o1.2.2: n = 1 → sum = 1
    s, _ = constant_sum(1)
    record_test("o1.2.2 n=1 → sum==1", s == 1)
    #o1.2.3: n = 10 → sum = 55
    s, _ = constant_sum(10)
    record_test("o1.2.3 n=10 → sum==55", s == 55)
    #o1.2.4: Type-check test
    out = constant_sum(5)
    record_test(
        "o1.2.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float)
    )
    #o1.2.5: Error-handling test
    s_err, _ = constant_sum("a")
    record_test("o1.2.5 invalid input returns -1", s_err == -1)

#🚀 Run tests
test_o1_2()

#📋 Summary
for r in test_results:
    print(r)
```

#### 💡 Guía de Implementación

**Fórmula matemática clave:**
```python
total = n * (n + 1) // 2
```

**¿Por qué es O(1)?**
- Sin bucles: una sola operación matemática garantiza tiempo constante 🔒

**Validación de entrada:**
```python
if not isinstance(n, int) or n < 0:
    return -1, elapsed
```

**Medición de tiempo:**
- Usar `time.time()` antes y después del cálculo ⏱️

#### 🧠 Importancia y Aplicaciones

- **Eficiencia computacional:** Los métodos de tiempo constante son la base de **cálculos directos** en estadística y física 📊🔬
- **Potencia matemática:** Demuestra el poder de la **intuición matemática** frente a la iteración por fuerza bruta 🧮
- **Aplicaciones reales:** Las fórmulas aceleran resúmenes de datos a gran escala en analítica 🍃
- **Fundamentos sólidos:** Refuerza la confianza en el análisis de algoritmos y validación de entrada ✅🔒

---

### 🎓 Resumen de Aprendizajes

Estos desafíos te ayudarán a:

1. **Dominar conceptos de complejidad**: Diferencias prácticas entre O(log n) y O(1)
2. **Desarrollar habilidades de análisis**: Identificar patrones de crecimiento algorítmico
3. **Aplicar buenas prácticas**: Validación de entrada y medición de rendimiento
4. **Construir intuición**: Para elegir el enfoque algorítmico más eficiente

¡Completa ambos desafíos para fortalecer tu comprensión de la complejidad algorítmica! 🚀
  
---
## o2: Recursión y Backtracking 🌀🔙

Este documento presenta dos desafíos fundamentales para dominar las técnicas de **recursión** y **backtracking**: cálculo factorial recursivo y generación de cadenas binarias mediante exploración exhaustiva.

---

### o2.1 🔁 **Factorial Recursivo** 🧮✨

#### 🎯 Objetivo del Problema

Implementa la función `factorial(n)` que calcule el factorial de `n` utilizando **recursión pura**, devolviendo el resultado matemático correcto o manejando entradas inválidas apropiadamente.

#### 📋 Especificaciones Técnicas

**Firma de la función:**
```python
factorial(n: int) → int or None
```

**Parámetros de entrada:**
- `n`: número entero no negativo (≥ 0) 🎯

**Valores de retorno:**
- **result**: `n!` como número entero 🔢
- **invalid**: `None` si la entrada es inválida ❌

**Complejidad temporal:** **O(n)** 🔄

#### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 0` → devuelve `1` (por definición: 0! = 1) ⚠️
- Valores muy grandes de `n` pueden alcanzar el límite de recursión de Python 🌋

**Restricciones obligatorias:**
- ✅ Debe usar **recursión** exclusivamente (sin bucles)
- 🚫 No se permiten iteraciones o funciones matemáticas externas

**Validación de entrada:**
- Si `n` no es un entero o `n < 0`, devolver `None` ❌⚙️

#### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o2.1.1** | `n = 0` | `1` | Caso base: 0! = 1 🌱 |
| **o2.1.2** | `n = 5` | `120` | Factorial medio: 5×4×3×2×1 🌟 |
| **o2.1.3** | `n = 7` | `5040` | Factorial mayor para verificar precisión 🔥 |
| **o2.1.4** | `n = 3` | `int` | Verificación de tipo de retorno 🧐 |
| **o2.1.5** | `n = -1`, `n = "a"` | `None` | Manejo de entradas inválidas ⚠️ |

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def factorial(n):
    """🔁 Compute n! recursively; return None if input invalid."""
    # Your solution here 🛠️
    pass

def test_o2_1():
    # o2.1.1: n = 0 → result = 1
    record_test("o2.1.1 n=0 → 1", factorial(0) == 1)
    # o2.1.2: n = 5 → result = 120
    record_test("o2.1.2 n=5 → 120", factorial(5) == 120)
    # o2.1.3: n = 7 → result = 5040
    record_test("o2.1.3 n=7 → 5040", factorial(7) == 5040)
    # o2.1.4: type-check
    out = factorial(3)
    record_test("o2.1.4 returns int", isinstance(out, int))
    # o2.1.5: invalid input → None
    record_test("o2.1.5 invalid returns None",
        factorial(-1) is None and factorial("a") is None)

# 🚀 Run tests
test_o2_1()

# 📋 Summary
for r in test_results:
    print(r)
```

#### 💡 Guía de Implementación

**Estructura recursiva recomendada:**

1. **Validación de entrada:**
   ```python
   if not isinstance(n, int) or n < 0:
       return None
   ```

2. **Caso base:**
   ```python
   if n == 0:
       return 1  # 🌱 Detiene la recursión
   ```

3. **Caso recursivo:**
   ```python
   return n * factorial(n - 1)  # 🔄 Llamada recursiva
   ```

**Consideraciones importantes:**
- Valida la entrada **antes** de iniciar la recursión para evitar errores ❌
- Ten cuidado con el **límite de profundidad de recursión** de Python en valores grandes 🌋
- El factorial crece muy rápidamente: 20! ya supera los 2 quintillones

#### 🧠 Importancia y Aplicaciones

- **Paradigma divide y vencerás:** Ejemplo fundamental de descomposición de problemas en subproblemas más pequeños 🌳
- **Fundamentos de programación dinámica:** Base para técnicas de memoización y optimización 💾
- **Comprensión del call stack:** Refuerza el entendimiento de la pila de llamadas y mecánicas de recursión 🧠
- **Matemáticas computacionales:** Aplicaciones en combinatoria, probabilidad y análisis numérico 📊

---

### o2.2 🔤 **Generación de Cadenas Binarias de Longitud N** 0️⃣1️⃣🛤️

#### 🎯 Objetivo del Problema

Implementa la función `generate_binary_strings(n)` que genere todas las posibles cadenas binarias de longitud `n` utilizando la técnica de **backtracking**, explorando sistemáticamente todas las combinaciones posibles.

#### 📋 Especificaciones Técnicas

**Firma de la función:**
```python
generate_binary_strings(n: int) → list[str]
```

**Parámetros de entrada:**
- `n`: número entero no negativo que representa la longitud deseada 🎯

**Valores de retorno:**
- **result**: lista de todas las cadenas binarias de longitud `n` 📋
- **invalid**: lista vacía `[]` si la entrada es inválida ❌

**Complejidad temporal:** **O(2ⁿ · n)** 🔍
- `2ⁿ` combinaciones posibles
- `n` operaciones por cadena generada

#### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 0` → devuelve `['']` (una cadena vacía) ⚠️
- Crecimiento exponencial: `n = 10` genera 1024 cadenas 🌋

**Restricciones obligatorias:**
- ✅ Debe usar **backtracking** (generación recursiva)
- ✅ Explorar sistemáticamente todas las ramas del árbol de decisión
- 🚫 No usar funciones de generación automática o bibliotecas externas

**Validación de entrada:**
- Si `n` no es un entero o `n < 0`, devolver `[]` ❌⚙️

#### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o2.2.1** | `n = 2` | `['00','01','10','11']` | Todas las combinaciones de 2 bits 🌱 |
| **o2.2.2** | `n = 3` | `len(result) == 8` | Verificación de cantidad total 🌟 |
| **o2.2.3** | `n = 3` | `'101' in result` | Verificación de cadena específica 🔥 |
| **o2.2.4** | `n = 1` | `list[str]` | Verificación de tipos de retorno 🧐 |
| **o2.2.5** | `n = -1`, `n = "a"` | `[]` | Manejo de entradas inválidas ⚠️ |

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    # Your solution here 🛠️
    pass

def test_o2_2():
    # o2.2.1: n = 2 → ['00','01','10','11']
    record_test("o2.2.1 n=2 → 4 strings",
        generate_binary_strings(2) == ['00','01','10','11'])
    # o2.2.2: n = 3 → length = 8
    record_test("o2.2.2 n=3 → length=8",
        len(generate_binary_strings(3)) == 8)
    # o2.2.3: contains '101'
    record_test("o2.2.3 contains '101'",
        '101' in generate_binary_strings(3))
    # o2.2.4: type-check
    res = generate_binary_strings(1)
    record_test("o2.2.4 returns list[str]",
        isinstance(res, list) and all(isinstance(s, str) for s in res))
    # o2.2.5: invalid input → []
    record_test("o2.2.5 invalid returns []",
        generate_binary_strings(-1) == [] and generate_binary_strings("a") == [])

# 🚀 Run tests
test_o2_2()

# 📋 Summary
for r in test_results:
    print(r)
```

#### 💡 Guía de Implementación

**Estructura de backtracking recomendada:**

1. **Validación de entrada:**
   ```python
   if not isinstance(n, int) or n < 0:
       return []
   ```

2. **Función auxiliar de backtracking:**
   ```python
   def backtrack(prefix):
       if len(prefix) == n:
           result.append(prefix)  # 🌳 Caso base
           return
       
       # Explorar ambas opciones
       backtrack(prefix + '0')  # 🔄 Rama izquierda
       backtrack(prefix + '1')  # 🔄 Rama derecha
   ```

3. **Inicialización:**
   ```python
   result = []
   backtrack('')  # Comenzar con cadena vacía
   return result
   ```

**Conceptos clave del backtracking:**
- **Exploración sistemática:** Cada posición puede ser '0' o '1'
- **Árbol de decisión:** Cada nivel representa una posición en la cadena
- **Caso base:** Cuando la cadena alcanza la longitud deseada
- **Retroceso implícito:** Python maneja automáticamente el retorno de llamadas

#### 🧠 Importancia y Aplicaciones

- **Algoritmos de backtracking:** Demuestra la exploración exhaustiva de todas las ramas combinatoriales 🌲
- **Problemas de satisfacción de restricciones:** Fundamento para resolver N-Queens, Sudoku, coloreado de grafos 🎯
- **Generación combinatoria:** Base para permutaciones, combinaciones y subconjuntos 🔄
- **Optimización computacional:** Técnicas de poda y optimización de búsqueda 🚀

**Aplicaciones del mundo real:**
- **Criptografía:** Generación de claves y análisis de seguridad
- **Inteligencia artificial:** Espacios de búsqueda y algoritmos de decisión
- **Bioinformática:** Análisis de secuencias genéticas
- **Redes de computadoras:** Protocolos de comunicación y enrutamiento

---

### 🎓 Resumen de Aprendizajes

Estos desafíos te permitirán:

#### 🔄 Dominio de Recursión
- **Casos base y recursivos:** Estructura fundamental de algoritmos recursivos
- **Gestión de la pila:** Comprensión profunda del call stack y memoria
- **Optimización:** Identificación de oportunidades de memoización

#### 🌲 Maestría en Backtracking
- **Exploración sistemática:** Técnicas de búsqueda exhaustiva controlada
- **Poda de ramas:** Optimización mediante eliminación temprana
- **Espacios de solución:** Navegación eficiente en problemas combinatorios

#### 🧠 Pensamiento Algorítmico
- **Descomposición de problemas:** División en subproblemas manejables
- **Patrones de diseño:** Reconocimiento de estructuras algorítmicas recurrentes
- **Análisis de complejidad:** Evaluación de eficiencia temporal y espacial

¡Completa ambos desafíos para consolidar tu dominio de las técnicas recursivas y de backtracking! 🚀💡

---
## o3: Listas Enlazadas 📎🔗

### o3.1 ➕ **Insertar al Inicio, Insertar al Final y Longitud** 🏁👶➕📏

---

#### ❓ Problema 🤔

Implementa los métodos `insert_at_beginning(data)`, `insert_at_end(data)`, y mantén una propiedad `length` en tu clase `LinkedList`. 🐍✨

---

#### 📜 Descripción 📖

Necesitas crear una estructura de datos de lista enlazada con las siguientes características:

* **Clases requeridas**:
  * `Node(data)` con atributos `data` (datos) y `next` (siguiente nodo) 🧩
  * `LinkedList()` con:
    * `head` (cabeza de la lista, inicialmente `None`) 🎯
    * `length` (longitud de la lista, inicialmente `0`) 🔢

* **Métodos a implementar**:
  1. **`insert_at_beginning(data)`** – Crea un nuevo nodo al inicio de la lista, actualiza `head` e incrementa `length`
  2. **`insert_at_end(data)`** – Agrega un nuevo nodo al final de la lista (o al inicio si está vacía), incrementa `length`

* **Método auxiliar ya implementado**:
  * `display()` retorna `"val1 -> val2 -> ..."` o `"Empty list"` si no hay nodos 🌳

---

#### 🧪 Pruebas que Debes Pasar ✅

Tu implementación debe pasar todas estas pruebas:

1. **o3.1.1**: Inserción mixta simple
   * **Acciones**:
     ```python
     ll.insert_at_beginning(2)  # Insertar 2 al inicio
     ll.insert_at_end(3)        # Insertar 3 al final
     ```
   * **Resultado esperado**: `ll.display()` debe retornar `'2 -> 3'` ✅

2. **o3.1.2**: Múltiples inserciones mixtas
   * **Continuando con el caso anterior**:
     ```python
     ll.insert_at_beginning(1)  # Insertar 1 al inicio
     ll.insert_at_end(4)        # Insertar 4 al final
     ```
   * **Resultado esperado**: `ll.display()` debe retornar `'1 -> 2 -> 3 -> 4'` ✅

3. **o3.1.3**: Seguimiento de longitud
   * **Después de cuatro inserciones exitosas**: `ll.length == 4` 🔢✅

4. **o3.1.4**: Manejo de entrada inválida
   * **Guarda el valor actual**: `old = ll.length`
   * **Luego ejecuta**:
     ```python
     ll.insert_at_beginning(None)  # Entrada inválida
     ll.insert_at_end("x")         # Entrada inválida
     ```
   * **Resultado esperado**: `ll.length` debe permanecer igual a `old` (las entradas inválidas se ignoran) ⚠️

5. **o3.1.5**: Verificación de tipos de retorno
   * **Verifica que**:
     ```python
     isinstance(ll.length, int)    # Debe ser True 🆗  
     isinstance(ll.display(), str) # Debe ser True 🆗
     ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        """Insert new node at beginning and update length."""
        # Your solution here 🛠️
        pass

    def insert_at_end(self, data):
        """Insert new node at end and update length."""
        # Your solution here 🛠️
        pass

    def display(self):
        """Return 'Empty list' or 'val1 -> val2 -> ...'."""
        current, vals = self.head, []
        while current:
            vals.append(str(current.data))
            current = current.next
        return " -> ".join(vals) if vals else "Empty list"

def test_o3_1():
    ll = LinkedList()
    # o3.1.1 Mixed single insert
    ll.insert_at_beginning(2)
    ll.insert_at_end(3)
    record_test("o3.1.1 ll.display() == '2 -> 3'", ll.display() == '2 -> 3')
    # o3.1.2 Mixed multiple inserts
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    record_test("o3.1.2 ll.display() == '1 -> 2 -> 3 -> 4'", ll.display() == '1 -> 2 -> 3 -> 4')
    # o3.1.3 Length tracking
    record_test("o3.1.3 ll.length == 4", ll.length == 4)
    # o3.1.4 Invalid input handling
    old_len = ll.length
    ll.insert_at_beginning(None)
    ll.insert_at_end("x")
    record_test("o3.1.4 invalid ignored", ll.length == old_len)
    # o3.1.5 Return-type verification
    record_test("o3.1.5 types ok", isinstance(ll.length, int) and isinstance(ll.display(), str))

# 🚀 Run tests
test_o3_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Consejos Útiles ✨

* **Validación de datos**: Verifica que `data` sea válido (por ejemplo, omite la inserción si `data is None`) antes de insertar
* **Caso de lista vacía**: Maneja el caso especial de lista vacía por separado en `insert_at_end`
* **Actualización de longitud**: Solo actualiza `length` cuando la operación de inserción sea válida y exitosa
* **Gestión de punteros**: Asegúrate de actualizar correctamente los punteros `next` y `head`

---

#### 🧠 Motivación y Aprendizaje 💭

Este ejercicio te enseña conceptos fundamentales:

* **Operaciones básicas**: Tanto operaciones de **prepend** (agregar al inicio, como en una pila) como **append** (agregar al final, como en una cola) 🔄
* **Gestión de memoria**: Refuerza la comprensión de actualizaciones de punteros y seguimiento de tamaño 🔢
* **Fundamentos sólidos**: Establece las bases para estructuras de datos más avanzadas como **deque** y **listas circulares**
* **Manejo de errores**: Practica la validación de entrada y el manejo robusto de casos especiales

---

### o3.2 🔍❌ **Búsqueda y Eliminación** 🕵️‍♂️🗑️

---

#### ❓ Problema 🤔

Implementa `search(target)` para verificar si un valor existe en la lista, y `delete(target)` para eliminar el primer nodo que coincida con el valor objetivo, actualizando la `length`. 🔎❌

---

#### 📜 Descripción 📖

Trabajarás con la misma clase `LinkedList` que ya tiene `head`, `length`, métodos `insert_*`, y `display()`.

* **Métodos a implementar**:
  1. **`search(target)`** – Recorre los nodos de la lista y retorna `True` si encuentra una coincidencia, `False` en caso contrario
  2. **`delete(target)`** – Desenlaza el primer nodo que coincida con el valor objetivo y decrementa `length`

---

#### 🧪 Pruebas que Debes Pasar ✅

Tu implementación debe pasar todas estas pruebas:

1. **o3.2.1**: Búsqueda exitosa
   * **Preparación**: Precarga la lista con `[1,2,3,4]`
   * **Resultado esperado**: `ll.search(3) is True` ✅

2. **o3.2.2**: Eliminación en el medio
   * **Acción**: `ll.delete(2)`
   * **Resultado esperado**: `ll.display() == '1 -> 3 -> 4'` ✅

3. **o3.2.3**: Eliminación en los extremos
   * **Acciones**: `ll.delete(1)` luego `ll.delete(4)`
   * **Resultado esperado**: `ll.display() == '3'` ✅

4. **o3.2.4**: Operaciones inválidas
   * **Guarda el valor actual**: `old = ll.length`
   * **Ejecuta**:
     ```python
     ll.search(None) is False  # Búsqueda inválida
     ll.delete(999)            # Eliminación de valor inexistente
     ll.length == old          # La longitud no debe cambiar
     ```
   * **Resultado esperado**: Sin cambios, las operaciones inválidas se ignoran ⚠️

5. **o3.2.5**: Verificación de tipos de retorno
   * **Verifica que**:
     ```python
     isinstance(ll.search(3), bool)  # Debe ser True 🆗  
     isinstance(ll.length, int)      # Debe ser True 🆗
     ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        if data is None: return
        new = Node(data)
        new.next = self.head
        self.head = new
        self.length += 1

    def insert_at_end(self, data):
        if data is None: return
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new
        self.length += 1

    def display(self):
        curr, vals = self.head, []
        while curr:
            vals.append(str(curr.data))
            curr = curr.next
        return " -> ".join(vals) if vals else "Empty list"

    def search(self, target):
        """Return True if target exists, else False."""
        # Your solution here 🛠️
        pass

    def delete(self, target):
        """Delete first node with data == target and update length."""
        # Your solution here 🛠️
        pass

def test_o3_2():
    ll = LinkedList()
    for v in [1,2,3,4]:
        ll.insert_at_end(v)
    # o3.2.1 Search found
    record_test("o3.2.1 search(3) True", ll.search(3) is True)
    # o3.2.2 Delete middle
    ll.delete(2)
    record_test("o3.2.2 display == '1 -> 3 -> 4'", ll.display() == '1 -> 3 -> 4')
    # o3.2.3 Delete ends
    ll.delete(1)
    ll.delete(4)
    record_test("o3.2.3 display == '3'", ll.display() == '3')
    # o3.2.4 Invalid operations
    old = ll.length
    cond = (ll.search(None) is False)
    ll.delete(999)
    cond = cond and (ll.length == old)
    record_test("o3.2.4 invalid handled", cond)
    # o3.2.5 Return-type
    record_test("o3.2.5 types ok", isinstance(ll.search(3), bool) and isinstance(ll.length, int))

# 🚀 Run tests
test_o3_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Consejos Útiles ✨

* **Método search(target)**: Itera usando `while curr:` y retorna `True` inmediatamente cuando encuentres una coincidencia
* **Método delete(target)**: 
  - Maneja por separado la eliminación del nodo cabeza (head)
  - Para otros nodos, usa variables `prev` (anterior) y `curr` (actual) para desenlazan correctamente
  - Recuerda actualizar los punteros antes de eliminar el nodo
* **Gestión de longitud**: Solo decrementa `length` cuando la eliminación realmente ocurra
* **Validación**: Verifica que el valor objetivo sea válido antes de proceder con las operaciones

---

#### 🧠 Motivación y Aprendizaje 💭

Este ejercicio avanzado te enseña:

* **Operaciones de consulta**: Combina **búsqueda** y **eliminación**, operaciones clave para colecciones dinámicas 🔄
* **Manejo robusto de casos especiales**: Enfatiza el manejo de situaciones límite como eliminación de cabeza/cola/elemento ausente 🎯
* **Preparación para operaciones avanzadas**: Te prepara para manipulaciones más complejas de listas como **filtrado** y **empalme**
* **Gestión eficiente de memoria**: Aprende a liberar nodos correctamente y mantener la integridad de la estructura

#### 🔑 Conceptos Clave

- **Búsqueda lineal**: Recorrido secuencial para encontrar elementos
- **Eliminación con preservación de enlaces**: Mantener la continuidad de la lista después de eliminar nodos
- **Casos especiales**: Lista vacía, eliminación del primer/último elemento
- **Validación robusta**: Manejo de entradas inválidas sin afectar la estructura

---
## o4: Pilas (Stacks) 📚🧱

### o4.1 🧩 **Pila basada en Array: `is_empty`, `push`, `pop`** 🔄📥📤

#### ❓ Problema 🤔

Implementa una clase `Stack` utilizando una lista de Python con los siguientes métodos:

* `is_empty()` → verifica si la pila está vacía
* `push(data)` → agrega un elemento al tope de la pila
* `pop()` → remueve y retorna el elemento del tope (o `None` si está vacía) 🚀

#### 📜 Descripción Detallada 📖

**Estructura de la clase:**
```python
class Stack:
    def __init__(self):
        self.items = []  # Lista que almacena los elementos
```

**Métodos que debes implementar:**

1. **`is_empty(self) → bool`** 
   - Retorna `True` si `self.items` está vacía, `False` en caso contrario
   
2. **`push(self, data) → None`** 
   - Agrega `data` al final de `self.items` (que representa el tope de la pila)
   
3. **`pop(self) → Any | None`** 
   - Si la pila no está vacía: remueve y retorna el último elemento
   - Si está vacía: retorna `None`

**Restricciones importantes:**
- Usa únicamente operaciones básicas de listas (`append`, `pop`)
- No generes errores en usos inválidos (manejo seguro)
- Usa valores por defecto seguros para que el código siempre ejecute

#### 🧪 Casos de Prueba que Debes Pasar ✅

1. **o4.1.1**: Operaciones básicas
   - Crear pila vacía → `s.is_empty()` debe ser `True`
   - Agregar elementos → `s.push(1); s.push(2)` → `s.items == [1,2]`
   - Quitar elementos → `s.pop() == 2` y luego `s.pop() == 1` ✅

2. **o4.1.2**: Pop en pila vacía
   - En una pila vacía → `s2.pop()` debe retornar `None` ✅

3. **o4.1.3**: Operaciones mixtas
   - Después de `push(0); push(99)` → `pop() == 99` y `is_empty() == False` ✅

4. **o4.1.4**: Tipos de datos diversos
   - La pila debe almacenar cualquier tipo: `None`, strings, números, etc. ✅

5. **o4.1.5**: Verificación de tipos de retorno
   - `is_empty()` debe retornar un `bool`
   - `pop()` debe retornar el tipo correcto o `None` ✅

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if stack is empty."""
        # Your solution here 🛠️
        return True   # safe default

    def push(self, data):
        """Push data onto the stack."""
        # Your solution here 🛠️
        return        # safe default

    def pop(self):
        """Pop and return top item or None if empty."""
        # Your solution here 🛠️
        return None   # safe default

def test_o4_1():
    # o4.1.1 Core operations
    s = Stack()
    cond1 = (
        s.is_empty() is True
        and s.push(1) is None and s.push(2) is None
        and s.items == [1,2]
        and s.pop() == 2 and s.pop() == 1
    )
    record_test("o4.1.1 core ops", cond1)

    # o4.1.2 Pop on empty
    s2 = Stack()
    record_test("o4.1.2 pop empty → None", s2.pop() is None)

    # o4.1.3 Mixed operations
    s3 = Stack(); s3.push(0); s3.push(99)
    cond3 = (s3.pop() == 99 and s3.is_empty() == False)
    record_test("o4.1.3 mixed ops", cond3)

    # o4.1.4 Input-agnostic
    s4 = Stack(); s4.push(None); s4.push("x")
    record_test("o4.1.4 store any", s4.items == [None,"x"])

    # o4.1.5 Return-type tests
    val = s.pop()
    cond5 = isinstance(s.is_empty(), bool) and isinstance(val, (int,str,type(None)))
    record_test("o4.1.5 return types", cond5)

# 🚀 Run tests
test_o4_1()

# 📋 Summary
for r in test_results:
    print(r)
```

#### 💡 Consejos de Implementación ✨

* **Para `push`**: Usa `self.items.append(data)` para añadir al final 📥
* **Para `pop`**: Usa `self.items.pop()` dentro de un `if self.items:` para verificar que no esté vacía 🔄
* **Para `is_empty`**: Verifica con `not self.items` o `len(self.items) == 0` 🔍

#### 🧠 ¿Por qué son importantes las Pilas? 💭

* Las pilas siguen el principio **LIFO**: Last In, First Out (Último en entrar, Primero en salir) 🔝
* Son fundamentales para implementar:
  - **Funciones deshacer/rehacer** en aplicaciones
  - **Pila de llamadas** en programación
  - **Búsqueda en profundidad (DFS)** en grafos y árboles 🌲

---

### o4.2 🧩 **Pila con Lista Enlazada: `push`, `pop`, `peek`, `size`** 🔗👀📏

#### ❓ Problema 🤔

Implementa una `LinkedStack` usando nodos enlazados, con los métodos:

* `push(data)` → agregar al tope
* `pop()` → remover y retornar el tope (o `None`)
* `peek()` → ver el tope sin removerlo
* `size()` → obtener el número de elementos

#### 📜 Descripción Detallada 📖

**Estructuras de las clases:**
```python
class Node:
    def __init__(self, data):
        self.data = data    # Dato almacenado en el nodo
        self.next = None    # Referencia al siguiente nodo

class LinkedStack:
    def __init__(self):
        self.top = None     # Nodo en el tope (o None si vacía)
        self._size = 0      # Contador de elementos
```

**Métodos que debes implementar:**

1. **`push(self, data)`** 
   - Crea un nuevo `Node(data)` y lo coloca en el tope
   - Incrementa `self._size` en 1

2. **`pop(self)`** 
   - Si `self.top` existe: desenlaza y retorna su `data`
   - Si está vacía: retorna `None`
   - Decrementa `self._size` cuando sea exitoso

3. **`peek(self)`** 
   - Retorna `self.top.data` si existe, sino `None`
   - **No modifica** la pila

4. **`size(self)`** 
   - Retorna el valor de `self._size`

**Características importantes:**
- Usa valores por defecto seguros para que el código base siempre ejecute
- Maneja correctamente casos de pila vacía sin generar errores

#### 🧪 Casos de Prueba que Debes Pasar ✅

1. **o4.2.1**: Comportamiento en pila vacía
   - En pila recién creada: `peek() is None`, `pop() is None`, `size() == 0` ✅

2. **o4.2.2**: Después de agregar elementos
   - Tras `push(5); push(7); push(9)` → `peek() == 9`, `size() == 3` ✅

3. **o4.2.3**: Después de quitar elemento
   - Tras un `pop()` → `peek() == 7`, `size() == 2` ✅

4. **o4.2.4**: Tipos de datos mixtos
   - Tras `push("a")` → `peek() == "a"`, `size() == 3` ✅

5. **o4.2.5**: Verificación de tipos de retorno
   - `peek()` retorna el tipo correcto o `None`
   - `size()` retorna un `int` ✅

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Push element using linked nodes."""
        # Your solution here 🛠️
        return    # safe default

    def pop(self):
        """Pop and return top data or None."""
        # Your solution here 🛠️
        return None  # safe default

    def peek(self):
        """Return top data without removing or None."""
        # Your solution here 🛠️
        return None  # safe default

    def size(self):
        """Return number of items."""
        # Your solution here 🛠️
        return 0     # safe default

def test_o4_2():
    s = LinkedStack()
    # o4.2.1 Empty behavior
    cond1 = (s.peek() is None and s.pop() is None and s.size() == 0)
    record_test("o4.2.1 empty behavior", cond1)
    # o4.2.2 After pushes
    s.push(5); s.push(7); s.push(9)
    cond2 = (s.peek() == 9 and s.size() == 3)
    record_test("o4.2.2 push/peek/size", cond2)
    # o4.2.3 After pop
    s.pop()
    cond3 = (s.peek() == 7 and s.size() == 2)
    record_test("o4.2.3 pop adjusts", cond3)
    # o4.2.4 Mixed types
    s.push("a")
    cond4 = (s.peek() == "a" and s.size() == 3)
    record_test("o4.2.4 mixed types", cond4)
    # o4.2.5 Return-type tests
    cond5 = isinstance(s.peek(), (int,str,type(None))) and isinstance(s.size(), int)
    record_test("o4.2.5 return types", cond5)

# 🚀 Run tests
test_o4_2()

# 📋 Summary
for r in test_results:
    print(r)
```

#### 💡 Consejos de Implementación ✨

* **Pila con Array**: Usa operaciones de lista al final para rendimiento O(1)
* **Pila Enlazada**: Inserta/remueve en la cabeza (head), mantén el contador `_size`
* **`peek`** nunca modifica la estructura; **`size`** simplemente retorna el contador
* Recuerda actualizar `_size` en cada `push` y `pop` exitoso

#### 🧠 ¿Por qué dominar ambas implementaciones? 💭

* **Comprende las diferencias** entre almacenamiento **contiguo** (array) vs **enlazado** (nodos) 🔄
* **Trade-offs de memoria**: Arrays son más eficientes en espacio, listas enlazadas son más flexibles 🚧
* **Preparación para algoritmos avanzados**: DFS, sistemas de deshacer/rehacer, y simulación de call-stacks 🌲
* **Fundamentos sólidos** para estructuras de datos más complejas

---

### 🎯 Resumen de Objetivos de Aprendizaje

Al completar estos ejercicios habrás:

1. ✅ Implementado pilas con **dos enfoques diferentes** (array y lista enlazada)
2. ✅ Comprendido el principio **LIFO** y sus aplicaciones prácticas
3. ✅ Practicado manejo seguro de **casos extremos** (pilas vacías)
4. ✅ Desarrollado habilidades en **testing** y verificación de tipos
5. ✅ Sentado las bases para **algoritmos más avanzados** que usan pilas
---
## o5: Colas 🚶‍♀️🚶

### o5.1 🧩 Cola Basada en Array: enqueue, dequeue, peek 📥📤👀

#### ❓ Problema 🤔

Implementa una clase `Queue` simple que funcione como FIFO (First In, First Out) usando una lista de Python con los siguientes métodos:

- `enqueue(item)` → agregar elemento al final de la cola
- `dequeue()` → remover y retornar el primer elemento (o `None` si está vacía)
- `peek()` → retornar el primer elemento sin removerlo (o `None` si está vacía)

#### 📜 Descripción Detallada 📖

**Estructura de la Clase:**
```python
class Queue:
    def __init__(self):
        self._items = []  # Lista interna para almacenar elementos
```

**Métodos a Implementar:**

1. **`enqueue(self, item)`** – Agrega `item` al final de `self._items` usando `append()`.
2. **`dequeue(self)`** – Si `self._items` no está vacía, remueve el primer elemento con `pop(0)` y lo retorna; de lo contrario, retorna `None` implícitamente.
3. **`peek(self)`** – Si `self._items` no está vacía, retorna `self._items[0]`; de lo contrario, retorna `None`.

**Restricciones:**
- Usa únicamente operaciones de lista estándar de Python
- Implementa stubs seguros (usando `pass`) para que el harness nunca genere errores
- Mantén el comportamiento FIFO estricto

#### 🧪 Casos de Prueba a Superar ✅

**o5.1.1** - Comportamiento de cola vacía:
```python
queue_array = Queue()
# Debe cumplir: queue_array.dequeue() is None and queue_array.peek() is None
```

**o5.1.2** - Orden FIFO en enqueue/dequeue:
```python
queue_array.enqueue(1); queue_array.enqueue(2); queue_array.enqueue(3)
# Debe cumplir: dequeue() == 1, luego == 2, luego == 3
```

**o5.1.3** - Peek sin remover:
```python
queue_array.enqueue("x")
# Debe cumplir: peek() == "x" y después dequeue() == "x"
```

**o5.1.4** - Soporte para tipos mixtos:
```python
queue_array.enqueue(None); queue_array.enqueue("y")
# Debe manejar correctamente valores None y otros tipos
```

**o5.1.5** - Verificación de tipos de retorno:
```python
# Los métodos deben retornar tipos apropiados (int, str, NoneType)
```

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        pass

    def dequeue(self):
        """Remove and return front item or None if empty."""
        # Your solution here 🛠️
        pass

    def peek(self):
        """Return front item without removing or None if empty."""
        # Your solution here 🛠️
        pass

def test_o5_1():
    queue_array = Queue()
    record_test("o5.1.1 empty behavior",
        queue_array.dequeue() is None and queue_array.peek() is None)

    queue_array.enqueue(1)
    queue_array.enqueue(2)
    queue_array.enqueue(3)
    record_test("o5.1.2 FIFO order",
        queue_array.dequeue() == 1 and
        queue_array.dequeue() == 2 and
        queue_array.dequeue() == 3)

    queue_array.enqueue("x")
    record_test("o5.1.3 peek preserves",
        queue_array.peek() == "x" and queue_array.dequeue() == "x")

    queue_array.enqueue(None)
    queue_array.enqueue("y")
    record_test("o5.1.4 mixed types",
        queue_array.peek() is None and queue_array.dequeue() is None)

    val_removed = queue_array.dequeue()
    val_peeked  = queue_array.peek()
    record_test("o5.1.5 return types",
        isinstance(val_removed, (int, str, type(None))) and
        isinstance(val_peeked,   (int, str, type(None))))

# 🚀 Run tests
test_o5_1()

# 📋 Summary
for result in test_results:
    print(result)
```

#### 💡 Consejos Estratégicos ✨

1. **Para enqueue**: Utiliza `self._items.append(item)` para agregar al final 📥
2. **Para dequeue**: Usa `self._items.pop(0)` para remover del inicio, pero siempre verifica que la lista no esté vacía primero 🔄
3. **Para peek**: Accede a `self._items[0]` solo después de verificar `if self._items:` 🔎
4. **Manejo de casos edge**: Siempre considera qué pasa cuando la cola está vacía

#### 🧠 Motivación y Aplicaciones 💭

Las colas son estructuras FIFO fundamentales: **First In, First Out** ⏳

**Aplicaciones del mundo real:**
- Sistemas de cola de tareas y scheduling de procesos
- Algoritmos BFS (Breadth-First Search) en grafos
- Modelos productor-consumidor
- Buffers de comunicación entre procesos
- Sistemas de manejo de requests en servidores web

---

### o5.2 🧩 Cola con Lista Enlazada: is_empty, enqueue, dequeue, size 🔗📏

#### ❓ Problema 🤔

Implementa una cola FIFO basada en lista enlazada llamada `LinkedQueue` con los métodos:

- `is_empty()` → retorna `True` si la cola no tiene elementos
- `enqueue(item)` → agrega un nuevo nodo al final de la cola
- `dequeue()` → remueve y retorna los datos del nodo frontal (o `None`)
- `size()` → retorna el número de elementos en la cola

#### 📜 Descripción Detallada 📖

**Clases Requeridas:**

```python
class Node:
    def __init__(self, data):
        self.data = data    # Almacena el valor del nodo
        self.next = None    # Puntero al siguiente nodo

class LinkedQueue:
    def __init__(self):
        self._front = None    # Nodo frontal (None si vacía)
        self._rear  = None    # Nodo trasero (None si vacía)
        self._count = 0       # Contador de elementos
```

**Métodos a Implementar:**

1. **`is_empty(self)`** – Retorna `True` si `_count == 0`
2. **`enqueue(self, item)`** – Crea `Node(item)`, lo enlaza en `_rear`, ajusta `_front` si es el primer elemento, incrementa `_count`
3. **`dequeue(self)`** – Si no está vacía, remueve `_front`, retorna sus datos, decrementa `_count`; de lo contrario retorna `None`
4. **`size(self)`** – Retorna `_count`

**Consideraciones Especiales:**
- Manejo cuidadoso de punteros `_front` y `_rear`
- Casos edge: cola vacía, un solo elemento, múltiples elementos
- Mantener consistencia del contador `_count`

#### 🧪 Casos de Prueba a Superar ✅

**o5.2.1** - Cola vacía inicial:
```python
queue_linked = LinkedQueue()
# Debe cumplir: is_empty() is True and size() == 0
```

**o5.2.2** - Operaciones enqueue/dequeue:
```python
queue_linked.enqueue("a"); queue_linked.enqueue("b")
# Debe cumplir: is_empty() is False, size() == 2, dequeue() == "a"
```

**o5.2.3** - Cola después de vaciarla:
```python
# Después de remover todos los elementos
# Debe cumplir: is_empty() is True, size() == 0
```

**o5.2.4** - Dequeue inválido en cola vacía:
```python
# dequeue() en cola vacía debe retornar None sin cambiar size()
```

**o5.2.5** - Verificación de tipos de retorno:
```python
# Verificar que los métodos retornan tipos correctos
```

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._rear  = None
        self._count = 0

    def is_empty(self):
        """Return True if queue is empty."""
        # Your solution here 🛠️
        pass

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        pass

    def dequeue(self):
        """Remove and return front item or None."""
        # Your solution here 🛠️
        pass

    def size(self):
        """Return number of elements."""
        # Your solution here 🛠️
        pass

def test_o5_2():
    queue_linked = LinkedQueue()
    record_test("o5.2.1 empty",
        queue_linked.is_empty() is True and queue_linked.size() == 0)

    queue_linked.enqueue("a")
    queue_linked.enqueue("b")
    record_test("o5.2.2 enqueue/dequeue",
        queue_linked.is_empty() is False and
        queue_linked.size() == 2 and
        queue_linked.dequeue() == "a")

    queue_linked.dequeue()
    record_test("o5.2.3 drained",
        queue_linked.is_empty() is True and queue_linked.size() == 0)

    previous_size = queue_linked.size()
    record_test("o5.2.4 invalid dequeue",
        queue_linked.dequeue() is None and queue_linked.size() == previous_size)

    record_test("o5.2.5 return types",
        isinstance(queue_linked.is_empty(), bool) and
        isinstance(queue_linked.size(), int) and
        isinstance(queue_linked.dequeue(), (int, str, type(None))))

# 🚀 Run tests
test_o5_2()

# 📋 Summary
for result in test_results:
    print(result)
```

#### 💡 Consejos Estratégicos Avanzados ✨

1. **`is_empty`** – Simplemente verifica `self._count == 0`
2. **`enqueue`** – Crear nuevo `Node`, enlazarlo en `self._rear`; si es el primer nodo, establecer tanto `self._front` como `self._rear`
3. **`dequeue`** – Desenlazar `self._front`; si la cola queda vacía, resetear `self._rear` a `None`
4. **`size`** – Retornar `self._count`

**Algoritmo detallado para enqueue:**
```python
# Pseudocódigo
new_node = Node(item)
if self._rear is None:  # Cola vacía
    self._front = self._rear = new_node
else:  # Cola no vacía
    self._rear.next = new_node
    self._rear = new_node
self._count += 1
```

**Algoritmo detallado para dequeue:**
```python
# Pseudocódigo
if self._front is None:  # Cola vacía
    return None
data = self._front.data
self._front = self._front.next
if self._front is None:  # Era el último elemento
    self._rear = None
self._count -= 1
return data
```

#### 🧠 Motivación y Ventajas 💭

**¿Por qué usar listas enlazadas para colas?**

Las colas soportan múltiples paradigmas fundamentales: BFS, buffering, y rate-limiting 🔄

**Ventajas de la implementación con lista enlazada:**
- **Eficiencia**: Evita el costo O(n) de desplazar elementos que tiene `list.pop(0)` en Python
- **Memoria dinámica**: Se adapta automáticamente al tamaño real de datos
- **Operaciones O(1)**: Tanto enqueue como dequeue son operaciones de tiempo constante
- **Escalabilidad**: Maneja eficientemente colas muy grandes

**Aplicaciones avanzadas:**
- Sistemas de colas distribuidas (Redis, RabbitMQ)
- Algoritmos de grafos (BFS, pathfinding)
- Sistemas operativos (scheduling de procesos)
- Redes de computadoras (packet queuing)
- Simulaciones de eventos discretos

Esta implementación refuerza conceptos fundamentales de manejo de memoria dinámica y manipulación de punteros 🧩