# o1: Desafíos de Complejidad Algorítmica 📈⏱️

Este documento presenta dos desafíos fundamentales para comprender y aplicar diferentes complejidades algorítmicas: **logarítmica O(log n)** y **constante O(1)**.

---

## o1.1 🧩 **Conteo de Duplicaciones para Exceder N** 🔢➕📈

### 🎯 Objetivo del Problema

Implementa la función `logarithmic_complexity(n)` que cuenta cuántas veces debes **duplicar** el número 1 para que supere el valor `n`. La función debe devolver tanto el conteo como el tiempo de ejecución.

### 📋 Especificaciones Técnicas

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

### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 1` → count = 1 (porque 1×2 = 2 > 1) ⚠️
- Valores muy grandes de `n` (hasta 10⁹) 🔧

**Restricciones obligatorias:**
- ✅ Debe usar un bucle que duplique un total acumulativo
- 🚫 **NO** usar funciones logarítmicas del módulo `math`

**Validación de entrada:**
- Si `n` no es un entero o `n < 1`, devolver un indicador de error (ej: `-1` para count) más el tiempo transcurrido ❌⚙️

### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o1.1.1** | `n = 1` | `(1, time)` | Caso base: 1×2 > 1 🌱 |
| **o1.1.2** | `n = 10` | `(4, time)` | Secuencia: 1→2→4→8→16 🌟 |
| **o1.1.3** | `n = 100` | `(7, time)` | Llega hasta 128 🔥 |
| **o1.1.4** | `n = 5` | `(int, float)` | Verificación de tipos 🧐 |
| **o1.1.5** | `n = "a"` o `n = -3` | `(-1, float)` | Manejo de errores ⚠️ |

### 💻 Base Code 🖥️

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

### 💡 Guía de Implementación

**Estructura del bucle recomendada:**
```python
value = 1
count = 0
while value <= n:
    value *= 2  # 🔼 duplicar valor
    count += 1  # ➕ incrementar contador
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

### 🧠 Importancia y Aplicaciones

- **Fundamentos teóricos:** Demuestra el crecimiento logarítmico, crucial en **búsqueda binaria** y **divide y vencerás** 🌳
- **Estrategias algorítmicas:** Ayuda a elegir entre enfoques iterativos vs. recursivos 🔄
- **Aplicaciones reales:** Patrones de duplicación en **redimensionamiento de datos** y **retroceso exponencial** 🔧
- **Análisis de complejidad:** Desarrolla confianza en el escalado algorítmico 📏💡

---

## o1.2 🧩 **Suma de los Primeros N Números Naturales** ➕📊⏱️

### 🎯 Objetivo del Problema

Implementa la función `constant_sum(n)` que calcula la suma de los primeros `n` números naturales en **tiempo constante**, devolviendo el resultado y el tiempo de ejecución.

### 📋 Especificaciones Técnicas

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

### 🔍 Casos Especiales y Restricciones

**Casos límite:**
- `n = 0` → sum = 0 ⚠️
- Valores muy grandes de `n` (hasta 10⁸) 🔧

**Restricciones obligatorias:**
- ✅ Debe usar la **fórmula matemática** `n*(n+1)//2`
- 🚫 **NO** usar bucles para sumar todos los números

**Validación de entrada:**
- Si `n` no es un entero o `n < 0`, devolver un indicador de error (ej: `-1` para sum) más el tiempo transcurrido ❌⏱️

### 🧪 Casos de Prueba Requeridos

| Test | Entrada | Resultado Esperado | Descripción |
|------|---------|-------------------|-------------|
| **o1.2.1** | `n = 0` | `(0, time)` | Caso base: suma vacía 🌱 |
| **o1.2.2** | `n = 1` | `(1, time)` | Un solo elemento 🌟 |
| **o1.2.3** | `n = 10` | `(55, time)` | Suma 1+2+...+10 🔥 |
| **o1.2.4** | `n = 5` | `(int, float)` | Verificación de tipos 🧐 |
| **o1.2.5** | `n = "a"` o `n = -3` | `(-1, float)` | Manejo de errores ⚠️ |

### 💻 Base Code 🖥️

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
    # Your solution here 🛠️
    end = time.time()
    elapsed = end - start
    return None, elapsed  # replace None with your sum or -1 on invalid

def test_o1_2():
    # o1.2.1: n = 0 → sum = 0
    s, _ = constant_sum(0)
    record_test("o1.2.1 n=0 → sum==0", s == 0)
    # o1.2.2: n = 1 → sum = 1
    s, _ = constant_sum(1)
    record_test("o1.2.2 n=1 → sum==1", s == 1)
    # o1.2.3: n = 10 → sum = 55
    s, _ = constant_sum(10)
    record_test("o1.2.3 n=10 → sum==55", s == 55)
    # o1.2.4: Type-check test
    out = constant_sum(5)
    record_test(
        "o1.2.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float)
    )
    # o1.2.5: Error-handling test
    s_err, _ = constant_sum("a")
    record_test("o1.2.5 invalid input returns -1", s_err == -1)

# 🚀 Run tests
test_o1_2()

# 📋 Summary
for r in test_results:
    print(r)
```

### 💡 Guía de Implementación

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

### 🧠 Importancia y Aplicaciones

- **Eficiencia computacional:** Los métodos de tiempo constante son la base de **cálculos directos** en estadística y física 📊🔬
- **Potencia matemática:** Demuestra el poder de la **intuición matemática** frente a la iteración por fuerza bruta 🧮
- **Aplicaciones reales:** Las fórmulas aceleran resúmenes de datos a gran escala en analítica 🍃
- **Fundamentos sólidos:** Refuerza la confianza en el análisis de algoritmos y validación de entrada ✅🔒

---

## 🎓 Resumen de Aprendizajes

Estos desafíos te ayudarán a:

1. **Dominar conceptos de complejidad**: Diferencias prácticas entre O(log n) y O(1)
2. **Desarrollar habilidades de análisis**: Identificar patrones de crecimiento algorítmico
3. **Aplicar buenas prácticas**: Validación de entrada y medición de rendimiento
4. **Construir intuición**: Para elegir el enfoque algorítmico más eficiente

¡Completa ambos desafíos para fortalecer tu comprensión de la complejidad algorítmica! 🚀