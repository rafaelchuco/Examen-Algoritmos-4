# 🔢 Ejercicio: Complejidad Logarítmica

## 📋 Descripción del Problema

Necesitamos implementar una función `logarithmic_complexity(n)` que:
- Cuenta cuántas veces necesitamos duplicar el número 1 para que exceda el valor `n`
- Retorna una tupla `(count, elapsed_time)`
- Si la entrada es inválida (no es entero o < 1), retorna `(-1, elapsed_time)`

## 🧮 Análisis Matemático

### ¿Qué significa "duplicar 1 hasta exceder n"?

Empezamos con 1 y vamos duplicando:
- Paso 0: `1`
- Paso 1: `1 × 2 = 2`
- Paso 2: `2 × 2 = 4` 
- Paso 3: `4 × 2 = 8`
- Paso k: `2^k`

Queremos encontrar el menor `k` tal que `2^k > n`

### Ejemplos de los casos de prueba:

**n = 1:**
- Paso 0: 1 (no excede 1)
- Paso 1: 2 (excede 1) ✅
- **Respuesta: 1 duplicación**

**n = 10:**
- Paso 0: 1, Paso 1: 2, Paso 2: 4, Paso 3: 8 (no excede 10)
- Paso 4: 16 (excede 10) ✅
- **Respuesta: 4 duplicaciones**

**n = 100:**
- 2^6 = 64 (no excede), 2^7 = 128 (excede) ✅
- **Respuesta: 7 duplicaciones**

## 💡 Solución

```python
def logarithmic_complexity(n):
    """🔢 Count doublings of 1 to exceed n; return (count, elapsed_time).
    If input invalid (not int or < 1), return (-1, elapsed_time)."""
    start = time.time()
    
    # Validación de entrada
    if not isinstance(n, int) or n < 1:
        end = time.time()
        elapsed = end - start
        return -1, elapsed
    
    # Contar duplicaciones
    count = 0
    current = 1
    
    while current <= n:
        current *= 2  # Duplicar
        count += 1    # Incrementar contador
    
    end = time.time()
    elapsed = end - start
    return count, elapsed
```

## 🔍 Explicación Paso a Paso

### 1. **Validación de Entrada**
```python
if not isinstance(n, int) or n < 1:
    return -1, elapsed
```
- Verificamos que `n` sea un entero
- Verificamos que `n` sea mayor o igual a 1
- Si no cumple, retornamos `-1`

### 2. **Algoritmo Principal**
```python
count = 0
current = 1

while current <= n:
    current *= 2  # Duplicar: 1→2→4→8→16...
    count += 1    # Contar cada duplicación
```

### 3. **Traza de Ejecución para n=10**
```
Inicio: current=1, count=0
Iteración 1: current=1≤10 → current=2, count=1
Iteración 2: current=2≤10 → current=4, count=2  
Iteración 3: current=4≤10 → current=8, count=3
Iteración 4: current=8≤10 → current=16, count=4
Iteración 5: current=16>10 → SALIR
Resultado: count=4
```

## 🧪 Casos de Prueba

| Test | Input | Expected Output | Explicación |
|------|-------|----------------|-------------|
| o1.1.1 | n=1 | count=1 | 1→2 (1 duplicación) |
| o1.1.2 | n=10 | count=4 | 1→2→4→8→16 (4 duplicaciones) |
| o1.1.3 | n=100 | count=7 | 2^7=128>100 (7 duplicaciones) |
| o1.1.4 | n=5 | (int, float) | Verificar tipos de retorno |
| o1.1.5 | n="a" | count=-1 | Manejo de entrada inválida |

## ⚡ Complejidad

- **Tiempo:** O(log n) - logarítmica
- **Espacio:** O(1) - constante

El número de iteraciones es aproximadamente `log₂(n)`, de ahí el nombre "complejidad logarítmica".

## 🎯 Código Final Completo

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
    
    # Validación de entrada
    if not isinstance(n, int) or n < 1:
        end = time.time()
        elapsed = end - start
        return -1, elapsed
    
    # Contar duplicaciones
    count = 0
    current = 1
    
    while current <= n:
        current *= 2
        count += 1
    
    end = time.time()
    elapsed = end - start
    return count, elapsed

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

## ✅ Resultado Esperado

```
✅ o1.1.1 n=1 → count==1
✅ o1.1.2 n=10 → count==4
✅ o1.1.3 n=100 → count==7
✅ o1.1.4 returns (int, float)
✅ o1.1.5 invalid input returns -1
```