# 🔤 Solución: Generación de Cadenas Binarias con Backtracking

## 🎯 Objetivo
Implementar una función `generate_binary_strings(n)` que genere todas las cadenas binarias posibles de longitud n utilizando la técnica de backtracking.

## 📋 Casos de Prueba a Cumplir
- ✅ `generate_binary_strings(2)` debe retornar `['00','01','10','11']`
- ✅ `generate_binary_strings(3)` debe tener longitud `8` (2³ = 8)
- ✅ El resultado para n=3 debe contener `'101'`
- ✅ La función debe retornar una lista de strings
- ✅ Para entradas inválidas debe retornar lista vacía `[]`

## 🔍 Análisis Paso a Paso

### Paso 1: Entender el Problema
Para una longitud n, necesitamos generar todas las combinaciones binarias posibles:
- n = 1: `['0', '1']` → 2¹ = 2 cadenas
- n = 2: `['00', '01', '10', '11']` → 2² = 4 cadenas  
- n = 3: `['000', '001', '010', '011', '100', '101', '110', '111']` → 2³ = 8 cadenas

### Paso 2: Comprender Backtracking
El backtracking es una técnica que:
1. **Construye** la solución paso a paso
2. **Explora** todas las posibilidades en cada paso
3. **Retrocede** cuando completa una rama
4. **Continúa** con la siguiente posibilidad

### Paso 3: Diseño del Algoritmo
```
Para cada posición de 0 a n-1:
  ├── Agregar '0' → explorar resto
  └── Agregar '1' → explorar resto
```

## 💡 Solución Completa

```python
def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    # Validar entrada
    if not isinstance(n, int) or n < 0:
        return []
    
    # Caso base: longitud 0
    if n == 0:
        return ['']
    
    result = []
    
    def backtrack(current_string):
        # Caso base: hemos completado una cadena de longitud n
        if len(current_string) == n:
            result.append(current_string)
            return
        
        # Explorar ambas opciones: agregar '0' o '1'
        backtrack(current_string + '0')
        backtrack(current_string + '1')
    
    # Iniciar el backtracking con cadena vacía
    backtrack('')
    return result
```

## 🧪 Verificación de Casos

### Caso 1: `generate_binary_strings(2) == ['00','01','10','11']`
```
backtrack('')
├── backtrack('0')
│   ├── backtrack('00') → agrega '00' ✅
│   └── backtrack('01') → agrega '01' ✅
└── backtrack('1')
    ├── backtrack('10') → agrega '10' ✅
    └── backtrack('11') → agrega '11' ✅
```

### Caso 2: `len(generate_binary_strings(3)) == 8`
Para n=3, el árbol de recursión genera 2³ = 8 cadenas ✅

### Caso 3: `'101' in generate_binary_strings(3)`
El algoritmo genera todas las combinaciones, incluyendo '101' ✅

### Caso 4: Tipo de retorno
Retorna una lista de strings ✅

### Caso 5: Entradas inválidas
- `generate_binary_strings(-1)` → `[]`
- `generate_binary_strings("a")` → `[]`

## 🌳 Visualización del Backtracking (n=2)

```
                    ''
                   /  \
                  /    \
               '0'      '1'
              /  \      /  \
            '00' '01'  '10' '11'
             ✓    ✓     ✓    ✓
```

## 🚀 Código Completo para Probar

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    # Validar entrada
    if not isinstance(n, int) or n < 0:
        return []
    
    # Caso base: longitud 0
    if n == 0:
        return ['']
    
    result = []
    
    def backtrack(current_string):
        # Caso base: hemos completado una cadena de longitud n
        if len(current_string) == n:
            result.append(current_string)
            return
        
        # Explorar ambas opciones: agregar '0' o '1'
        backtrack(current_string + '0')
        backtrack(current_string + '1')
    
    # Iniciar el backtracking con cadena vacía
    backtrack('')
    return result

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

## 📊 Resultado Esperado
```
✅ o2.2.1 n=2 → 4 strings
✅ o2.2.2 n=3 → length=8
✅ o2.2.3 contains '101'
✅ o2.2.4 returns list[str]
✅ o2.2.5 invalid returns []
```

## 🔧 Implementación Alternativa (Más Concisa)

```python
def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    if not isinstance(n, int) or n < 0:
        return []
    
    if n == 0:
        return ['']
    
    # Obtener cadenas de longitud n-1 y agregar '0' y '1'
    smaller = generate_binary_strings(n - 1)
    return [s + '0' for s in smaller] + [s + '1' for s in smaller]
```

## 🔑 Puntos Clave del Backtracking

1. **Caso Base**: Cuando la cadena actual tiene longitud n, la agregamos al resultado
2. **Recursión**: Para cada posición, probamos tanto '0' como '1'
3. **Exploración Completa**: El algoritmo explora sistemáticamente todas las posibilidades
4. **Orden**: Las cadenas se generan en orden lexicográfico
5. **Complejidad**: O(2ⁿ) tiempo y espacio, ya que hay 2ⁿ cadenas binarias posibles

## 🎓 Conceptos Aprendidos
- **Backtracking**: Técnica fundamental para problemas de búsqueda exhaustiva
- **Recursión**: Dividir el problema en subproblemas más pequeños
- **Validación de entrada**: Manejar casos edge correctamente
- **Strings inmutables**: Crear nuevas cadenas en cada llamada recursiva