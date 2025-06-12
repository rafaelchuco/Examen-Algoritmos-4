# 📚 Solución: Función Factorial Recursiva

## 🎯 Objetivo
Implementar una función `factorial(n)` que calcule el factorial de un número de forma recursiva y pase todos los casos de prueba.

## 📋 Casos de Prueba a Cumplir
- ✅ `factorial(0)` debe retornar `1`
- ✅ `factorial(5)` debe retornar `120`  
- ✅ `factorial(7)` debe retornar `5040`
- ✅ La función debe retornar un entero (`int`)
- ✅ Para entradas inválidas debe retornar `None`

## 🔍 Análisis Paso a Paso

### Paso 1: Entender el Factorial
El factorial de un número n (n!) se define como:
- `0! = 1` (caso base)
- `n! = n × (n-1)!` para n > 0

### Paso 2: Identificar Casos Especiales
- **Caso base**: `n = 0` retorna `1`
- **Casos inválidos**: números negativos y tipos no numéricos retornan `None`
- **Recursión**: para n > 0, llamar recursivamente

### Paso 3: Validación de Entrada
Necesitamos validar que:
- El input sea un número entero
- El número sea no negativo

## 💡 Solución Completa

```python
def factorial(n):
    """🔁 Compute n! recursively; return None if input invalid."""
    # Validar que n sea un entero
    if not isinstance(n, int):
        return None
    
    # Validar que n sea no negativo
    if n < 0:
        return None
    
    # Caso base: 0! = 1
    if n == 0:
        return 1
    
    # Caso recursivo: n! = n × (n-1)!
    return n * factorial(n - 1)
```

## 🧪 Verificación de Casos

### Caso 1: `factorial(0) == 1`
- Entra al caso base directamente
- Retorna `1` ✅

### Caso 2: `factorial(5) == 120`
- `factorial(5)` = `5 × factorial(4)`
- `factorial(4)` = `4 × factorial(3)`
- `factorial(3)` = `3 × factorial(2)`
- `factorial(2)` = `2 × factorial(1)`
- `factorial(1)` = `1 × factorial(0)`
- `factorial(0)` = `1`
- Resultado: `5 × 4 × 3 × 2 × 1 × 1 = 120` ✅

### Caso 3: `factorial(7) == 5040`
- Similar al anterior: `7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040` ✅

### Caso 4: Tipo de retorno
- La función retorna enteros para casos válidos ✅

### Caso 5: Entradas inválidas
- `factorial(-1)` → `None` (número negativo)
- `factorial("a")` → `None` (no es entero)

## 🚀 Código Completo para Probar

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def factorial(n):
    """🔁 Compute n! recursively; return None if input invalid."""
    # Validar que n sea un entero
    if not isinstance(n, int):
        return None
    
    # Validar que n sea no negativo
    if n < 0:
        return None
    
    # Caso base: 0! = 1
    if n == 0:
        return 1
    
    # Caso recursivo: n! = n × (n-1)!
    return n * factorial(n - 1)

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

## 📊 Resultado Esperado
```
✅ o2.1.1 n=0 → 1
✅ o2.1.2 n=5 → 120
✅ o2.1.3 n=7 → 5040
✅ o2.1.4 returns int
✅ o2.1.5 invalid returns None
```

## 🔑 Puntos Clave
1. **Validación de entrada**: Verificar tipo y valor antes de procesar
2. **Caso base**: `n = 0` retorna `1` para terminar la recursión
3. **Recursión**: Llamar a la función con `n-1` y multiplicar por `n`
4. **Manejo de errores**: Retornar `None` para entradas inválidas