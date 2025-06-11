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