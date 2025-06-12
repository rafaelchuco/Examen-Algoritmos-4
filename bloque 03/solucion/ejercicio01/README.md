# 🔗 Solución: Lista Enlazada con Inserción al Inicio y Final

## 🎯 Objetivo
Implementar los métodos `insert_at_beginning()` e `insert_at_end()` en una clase LinkedList que mantenga un contador de longitud y maneje entradas inválidas correctamente.

## 📋 Casos de Prueba a Cumplir
- ✅ Inserción mixta: `insert_at_beginning(2)` + `insert_at_end(3)` → `'2 -> 3'`
- ✅ Múltiples inserciones: después de más operaciones → `'1 -> 2 -> 3 -> 4'`
- ✅ Tracking de longitud: `ll.length == 4` después de 4 inserciones
- ✅ Manejo de entradas inválidas: `None` y strings deben ser ignorados
- ✅ Tipos correctos: `length` es int, `display()` retorna string

## 🔍 Análisis Paso a Paso

### Paso 1: Entender la Estructura
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    # Apunta al primer nodo
        self.length = 0     # Contador de elementos
```

### Paso 2: Inserción al Inicio
```
Lista vacía: head -> None
Insertar 2:  head -> [2|None]
Insertar 1:  head -> [1|next] -> [2|None]
```

### Paso 3: Inserción al Final
```
Lista vacía: head -> None
Insertar 2:  head -> [2|None]
Insertar 3:  head -> [2|next] -> [3|None]
```

### Paso 4: Validación de Entrada
Según las pruebas, debemos rechazar:
- `None` valores
- Strings (como `"x"`)
- Solo aceptar números enteros

## 💡 Solución Completa

```python
def insert_at_beginning(self, data):
    """Insert new node at beginning and update length."""
    # Validar entrada: solo aceptar enteros
    if not isinstance(data, int):
        return
    
    # Crear nuevo nodo
    new_node = Node(data)
    
    # El nuevo nodo apunta al actual head
    new_node.next = self.head
    
    # Actualizar head para apuntar al nuevo nodo
    self.head = new_node
    
    # Incrementar longitud
    self.length += 1

def insert_at_end(self, data):
    """Insert new node at end and update length."""
    # Validar entrada: solo aceptar enteros
    if not isinstance(data, int):
        return
    
    # Crear nuevo nodo
    new_node = Node(data)
    
    # Si la lista está vacía, el nuevo nodo es el head
    if self.head is None:
        self.head = new_node
    else:
        # Encontrar el último nodo
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Conectar el último nodo al nuevo nodo
        current.next = new_node
    
    # Incrementar longitud
    self.length += 1
```

## 🧪 Verificación de Casos

### Caso 1: Inserción Mixta
```python
ll = LinkedList()
ll.insert_at_beginning(2)  # head -> [2|None]
ll.insert_at_end(3)        # head -> [2|next] -> [3|None]
# Result: '2 -> 3' ✅
```

### Caso 2: Múltiples Inserciones
```python
ll.insert_at_beginning(1)  # head -> [1|next] -> [2|next] -> [3|None]
ll.insert_at_end(4)        # head -> [1|next] -> [2|next] -> [3|next] -> [4|None]
# Result: '1 -> 2 -> 3 -> 4' ✅
```

### Caso 3: Tracking de Longitud
- Cada inserción válida incrementa `self.length`
- Después de 4 inserciones: `ll.length == 4` ✅

### Caso 4: Entradas Inválidas
```python
ll.insert_at_beginning(None)  # Ignorado
ll.insert_at_end("x")         # Ignorado
# length permanece igual ✅
```

## 🚀 Código Completo para Probar

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
        # Validar entrada: solo aceptar enteros
        if not isinstance(data, int):
            return
        
        # Crear nuevo nodo
        new_node = Node(data)
        
        # El nuevo nodo apunta al actual head
        new_node.next = self.head
        
        # Actualizar head para apuntar al nuevo nodo
        self.head = new_node
        
        # Incrementar longitud
        self.length += 1

    def insert_at_end(self, data):
        """Insert new node at end and update length."""
        # Validar entrada: solo aceptar enteros
        if not isinstance(data, int):
            return
        
        # Crear nuevo nodo
        new_node = Node(data)
        
        # Si la lista está vacía, el nuevo nodo es el head
        if self.head is None:
            self.head = new_node
        else:
            # Encontrar el último nodo
            current = self.head
            while current.next is not None:
                current = current.next
            
            # Conectar el último nodo al nuevo nodo
            current.next = new_node
        
        # Incrementar longitud
        self.length += 1

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

## 📊 Resultado Esperado
```
✅ o3.1.1 ll.display() == '2 -> 3'
✅ o3.1.2 ll.display() == '1 -> 2 -> 3 -> 4'
✅ o3.1.3 ll.length == 4
✅ o3.1.4 invalid ignored
✅ o3.1.5 types ok
```

## 🎯 Visualización de Operaciones

### Estado Inicial
```
LinkedList: head -> None, length = 0
```

### Después de `insert_at_beginning(2)`
```
LinkedList: head -> [2|None], length = 1
```

### Después de `insert_at_end(3)`
```
LinkedList: head -> [2|next] -> [3|None], length = 2
```

### Después de `insert_at_beginning(1)`
```
LinkedList: head -> [1|next] -> [2|next] -> [3|None], length = 3
```

### Después de `insert_at_end(4)`
```
LinkedList: head -> [1|next] -> [2|next] -> [3|next] -> [4|None], length = 4
```

## 🔑 Puntos Clave

### Insert at Beginning
1. **Validar entrada** - Solo aceptar enteros
2. **Crear nuevo nodo** - Con el dato proporcionado
3. **Conectar** - `new_node.next = self.head`
4. **Actualizar head** - `self.head = new_node`
5. **Incrementar longitud** - `self.length += 1`

### Insert at End
1. **Validar entrada** - Solo aceptar enteros
2. **Crear nuevo nodo** - Con el dato proporcionado
3. **Caso especial** - Si lista vacía, nuevo nodo es head
4. **Encontrar último nodo** - Recorrer hasta `current.next is None`
5. **Conectar** - `current.next = new_node`
6. **Incrementar longitud** - `self.length += 1`

## ⚡ Complejidad

| Operación | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| `insert_at_beginning()` | O(1) | O(1) |
| `insert_at_end()` | O(n) | O(1) |
| `display()` | O(n) | O(n) |

## 🎓 Conceptos Aprendidos
- **Listas enlazadas**: Estructura dinámica con nodos conectados
- **Inserción eficiente**: Al inicio es O(1), al final es O(n)
- **Mantenimiento de estado**: Tracking de longitud
- **Validación de entrada**: Filtrar tipos de datos inválidos
- **Traversal**: Recorrido de nodos siguiendo punteros `next`