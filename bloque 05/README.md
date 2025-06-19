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