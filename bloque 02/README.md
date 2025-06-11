# o2: Recursión y Backtracking 🌀🔙

Este documento presenta dos desafíos fundamentales para dominar las técnicas de **recursión** y **backtracking**: cálculo factorial recursivo y generación de cadenas binarias mediante exploración exhaustiva.

---

## o2.1 🔁 **Factorial Recursivo** 🧮✨

### 🎯 Objetivo del Problema

Implementa la función `factorial(n)` que calcule el factorial de `n` utilizando **recursión pura**, devolviendo el resultado matemático correcto o manejando entradas inválidas apropiadamente.

### 📋 Especificaciones Técnicas

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

### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 0` → devuelve `1` (por definición: 0! = 1) ⚠️
- Valores muy grandes de `n` pueden alcanzar el límite de recursión de Python 🌋

**Restricciones obligatorias:**
- ✅ Debe usar **recursión** exclusivamente (sin bucles)
- 🚫 No se permiten iteraciones o funciones matemáticas externas

**Validación de entrada:**
- Si `n` no es un entero o `n < 0`, devolver `None` ❌⚙️

### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o2.1.1** | `n = 0` | `1` | Caso base: 0! = 1 🌱 |
| **o2.1.2** | `n = 5` | `120` | Factorial medio: 5×4×3×2×1 🌟 |
| **o2.1.3** | `n = 7` | `5040` | Factorial mayor para verificar precisión 🔥 |
| **o2.1.4** | `n = 3` | `int` | Verificación de tipo de retorno 🧐 |
| **o2.1.5** | `n = -1`, `n = "a"` | `None` | Manejo de entradas inválidas ⚠️ |

### 💻 Base Code 🖥️

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

### 💡 Guía de Implementación

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

### 🧠 Importancia y Aplicaciones

- **Paradigma divide y vencerás:** Ejemplo fundamental de descomposición de problemas en subproblemas más pequeños 🌳
- **Fundamentos de programación dinámica:** Base para técnicas de memoización y optimización 💾
- **Comprensión del call stack:** Refuerza el entendimiento de la pila de llamadas y mecánicas de recursión 🧠
- **Matemáticas computacionales:** Aplicaciones en combinatoria, probabilidad y análisis numérico 📊

---

## o2.2 🔤 **Generación de Cadenas Binarias de Longitud N** 0️⃣1️⃣🛤️

### 🎯 Objetivo del Problema

Implementa la función `generate_binary_strings(n)` que genere todas las posibles cadenas binarias de longitud `n` utilizando la técnica de **backtracking**, explorando sistemáticamente todas las combinaciones posibles.

### 📋 Especificaciones Técnicas

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

### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 0` → devuelve `['']` (una cadena vacía) ⚠️
- Crecimiento exponencial: `n = 10` genera 1024 cadenas 🌋

**Restricciones obligatorias:**
- ✅ Debe usar **backtracking** (generación recursiva)
- ✅ Explorar sistemáticamente todas las ramas del árbol de decisión
- 🚫 No usar funciones de generación automática o bibliotecas externas

**Validación de entrada:**
- Si `n` no es un entero o `n < 0`, devolver `[]` ❌⚙️

### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o2.2.1** | `n = 2` | `['00','01','10','11']` | Todas las combinaciones de 2 bits 🌱 |
| **o2.2.2** | `n = 3` | `len(result) == 8` | Verificación de cantidad total 🌟 |
| **o2.2.3** | `n = 3` | `'101' in result` | Verificación de cadena específica 🔥 |
| **o2.2.4** | `n = 1` | `list[str]` | Verificación de tipos de retorno 🧐 |
| **o2.2.5** | `n = -1`, `n = "a"` | `[]` | Manejo de entradas inválidas ⚠️ |

### 💻 Base Code 🖥️

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

### 💡 Guía de Implementación

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

### 🧠 Importancia y Aplicaciones

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

## 🎓 Resumen de Aprendizajes

Estos desafíos te permitirán:

### 🔄 Dominio de Recursión
- **Casos base y recursivos:** Estructura fundamental de algoritmos recursivos
- **Gestión de la pila:** Comprensión profunda del call stack y memoria
- **Optimización:** Identificación de oportunidades de memoización

### 🌲 Maestría en Backtracking
- **Exploración sistemática:** Técnicas de búsqueda exhaustiva controlada
- **Poda de ramas:** Optimización mediante eliminación temprana
- **Espacios de solución:** Navegación eficiente en problemas combinatorios

### 🧠 Pensamiento Algorítmico
- **Descomposición de problemas:** División en subproblemas manejables
- **Patrones de diseño:** Reconocimiento de estructuras algorítmicas recurrentes
- **Análisis de complejidad:** Evaluación de eficiencia temporal y espacial

¡Completa ambos desafíos para consolidar tu dominio de las técnicas recursivas y de backtracking! 🚀💡