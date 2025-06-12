# 🔢 Ejercicio: Suma en Tiempo Constante O(1)

## 📋 Descripción del Problema

Necesitamos implementar una función `constant_sum(n)` que:
- Calcula la suma de números del 1 al n en **tiempo constante O(1)**
- Retorna una tupla `(sum, elapsed_time)`
- Si la entrada es inválida (no es entero o < 0), retorna `(-1, elapsed_time)`

## 🧮 Análisis Matemático

### ¿Qué es la suma de 1 a n?

```
sum(1..n) = 1 + 2 + 3 + ... + n
```

### Ejemplos:
- n = 0: suma = 0 (suma vacía)
- n = 1: suma = 1
- n = 3: suma = 1 + 2 + 3 = 6
- n = 10: suma = 1 + 2 + 3 + ... + 10 = 55

### 🎯 La Fórmula Mágica

En lugar de usar un bucle (que sería O(n)), usamos la **fórmula de Gauss**:

```
suma = n × (n + 1) / 2
```

### ¿Por qué funciona esta fórmula?

Imaginemos la suma de 1 a 5:
```
  1 + 2 + 3 + 4 + 5 = 15
+ 5 + 4 + 3 + 2 + 1 = 15
  -------------------
  6 + 6 + 6 + 6 + 6 = 30
```

Tenemos `n` pares que suman `(n+1)`, entonces:
- Total = `n × (n+1)` 
- Pero contamos todo dos veces, así que: `n × (n+1) / 2`

## 💡 Solución

```python
def constant_sum(n):
    """🔢 Compute sum of 1..n in O(1), return (sum, elapsed_time).
    If input invalid (not int or < 0), return (-1, elapsed_time)."""
    start = time.time()
    
    # Validación de entrada
    if not isinstance(n, int) or n < 0:
        end = time.time()
        elapsed = end - start
        return -1, elapsed
    
    # Fórmula de Gauss: n × (n + 1) / 2
    result = n * (n + 1) // 2
    
    end = time.time()
    elapsed = end - start
    return result, elapsed
```

## 🔍 Explicación Paso a Paso

### 1. **Validación de Entrada**
```python
if not isinstance(n, int) or n < 0:
    return -1, elapsed
```
- Verificamos que `n` sea un entero
- Verificamos que `n` sea mayor o igual a 0 (≥ 0, no ≥ 1 como el anterior)
- Si no cumple, retornamos `-1`

### 2. **Aplicar Fórmula de Gauss**
```python
result = n * (n + 1) // 2
```
- Usamos `//` (división entera) para obtener un entero
- **¡Una sola operación!** → O(1)

### 3. **Verificación de la Fórmula**

**n = 0:**
```
suma = 0 × (0 + 1) / 2 = 0 × 1 / 2 = 0 ✅
```

**n = 1:**
```
suma = 1 × (1 + 1) / 2 = 1 × 2 / 2 = 1 ✅
```

**n = 10:**
```
suma = 10 × (10 + 1) / 2 = 10 × 11 / 2 = 110 / 2 = 55 ✅
Verificación: 1+2+3+4+5+6+7+8+9+10 = 55 ✅
```

## 🧪 Casos de Prueba

| Test | Input | Expected Output | Fórmula |
|------|-------|----------------|---------|
| o1.2.1 | n=0 | sum=0 | 0×1/2 = 0 |
| o1.2.2 | n=1 | sum=1 | 1×2/2 = 1 |
| o1.2.3 | n=10 | sum=55 | 10×11/2 = 55 |
| o1.2.4 | n=5 | (int, float) | Verificar tipos de retorno |
| o1.2.5 | n="a" | sum=-1 | Manejo de entrada inválida |

## ⚡ Comparación de Complejidades

### ❌ Método O(n) - Bucle (LENTO)
```python
# NO hacer esto - es O(n)
total = 0
for i in range(1, n+1):
    total += i
return total
```

### ✅ Método O(1) - Fórmula (RÁPIDO)
```python
# SÍ hacer esto - es O(1)
return n * (n + 1) // 2
```

**¿Por qué O(1)?** Porque sin importar si n=10 o n=1,000,000, siempre hacemos la misma cantidad de operaciones: una multiplicación y una división.

## 🎯 Código Final Completo

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
    
    # Validación de entrada
    if not isinstance(n, int) or n < 0:
        end = time.time()
        elapsed = end - start
        return -1, elapsed
    
    # Fórmula de Gauss: n × (n + 1) / 2
    result = n * (n + 1) // 2
    
    end = time.time()
    elapsed = end - start
    return result, elapsed

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

## ✅ Resultado Esperado

```
✅ o1.2.1 n=0 → sum==0
✅ o1.2.2 n=1 → sum==1
✅ o1.2.3 n=10 → sum==55
✅ o1.2.4 returns (int, float)
✅ o1.2.5 invalid input returns -1
```

## 🧠 Datos Curiosos

1. **Carl Friedrich Gauss** (matemático alemán) descubrió esta fórmula cuando tenía solo 10 años
2. Su maestro le pidió sumar los números del 1 al 100 para mantenerlo ocupado
3. Gauss lo resolvió en segundos usando esta fórmula: `100 × 101 / 2 = 5050`

## 💭 Conclusión

La diferencia entre O(n) y O(1) es **enorme**:
- Para n=1,000,000: O(n) hace 1 millón de operaciones, O(1) hace solo 1
- **¡Una simple fórmula matemática nos ahorra millones de operaciones!** 🚀