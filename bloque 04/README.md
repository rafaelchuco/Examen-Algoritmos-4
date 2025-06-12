# o4: Pilas (Stacks) 📚🧱

## o4.1 🧩 **Pila basada en Array: `is_empty`, `push`, `pop`** 🔄📥📤

### ❓ Problema 🤔

Implementa una clase `Stack` utilizando una lista de Python con los siguientes métodos:

* `is_empty()` → verifica si la pila está vacía
* `push(data)` → agrega un elemento al tope de la pila
* `pop()` → remueve y retorna el elemento del tope (o `None` si está vacía) 🚀

### 📜 Descripción Detallada 📖

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

### 🧪 Casos de Prueba que Debes Pasar ✅

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

### 💻 Base Code 🖥️

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

### 💡 Consejos de Implementación ✨

* **Para `push`**: Usa `self.items.append(data)` para añadir al final 📥
* **Para `pop`**: Usa `self.items.pop()` dentro de un `if self.items:` para verificar que no esté vacía 🔄
* **Para `is_empty`**: Verifica con `not self.items` o `len(self.items) == 0` 🔍

### 🧠 ¿Por qué son importantes las Pilas? 💭

* Las pilas siguen el principio **LIFO**: Last In, First Out (Último en entrar, Primero en salir) 🔝
* Son fundamentales para implementar:
  - **Funciones deshacer/rehacer** en aplicaciones
  - **Pila de llamadas** en programación
  - **Búsqueda en profundidad (DFS)** en grafos y árboles 🌲

---

## o4.2 🧩 **Pila con Lista Enlazada: `push`, `pop`, `peek`, `size`** 🔗👀📏

### ❓ Problema 🤔

Implementa una `LinkedStack` usando nodos enlazados, con los métodos:

* `push(data)` → agregar al tope
* `pop()` → remover y retornar el tope (o `None`)
* `peek()` → ver el tope sin removerlo
* `size()` → obtener el número de elementos

### 📜 Descripción Detallada 📖

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

### 🧪 Casos de Prueba que Debes Pasar ✅

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

### 💻 Base Code 🖥️

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

### 💡 Consejos de Implementación ✨

* **Pila con Array**: Usa operaciones de lista al final para rendimiento O(1)
* **Pila Enlazada**: Inserta/remueve en la cabeza (head), mantén el contador `_size`
* **`peek`** nunca modifica la estructura; **`size`** simplemente retorna el contador
* Recuerda actualizar `_size` en cada `push` y `pop` exitoso

### 🧠 ¿Por qué dominar ambas implementaciones? 💭

* **Comprende las diferencias** entre almacenamiento **contiguo** (array) vs **enlazado** (nodos) 🔄
* **Trade-offs de memoria**: Arrays son más eficientes en espacio, listas enlazadas son más flexibles 🚧
* **Preparación para algoritmos avanzados**: DFS, sistemas de deshacer/rehacer, y simulación de call-stacks 🌲
* **Fundamentos sólidos** para estructuras de datos más complejas

---

## 🎯 Resumen de Objetivos de Aprendizaje

Al completar estos ejercicios habrás:

1. ✅ Implementado pilas con **dos enfoques diferentes** (array y lista enlazada)
2. ✅ Comprendido el principio **LIFO** y sus aplicaciones prácticas
3. ✅ Practicado manejo seguro de **casos extremos** (pilas vacías)
4. ✅ Desarrollado habilidades en **testing** y verificación de tipos
5. ✅ Sentado las bases para **algoritmos más avanzados** que usan pilas