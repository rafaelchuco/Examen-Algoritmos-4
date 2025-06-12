# 🔍 Solución: Lista Enlazada con Búsqueda y Eliminación

## 🎯 Objetivo
Implementar los métodos `search()` y `delete()` en una lista enlazada que permitan buscar elementos y eliminar nodos manteniendo la integridad de la estructura y el contador de longitud.

## 📋 Casos de Prueba a Cumplir
- ✅ `search(3)` debe retornar `True` cuando el elemento existe
- ✅ `delete(2)` debe eliminar el nodo del medio → `'1 -> 3 -> 4'`
- ✅ Eliminar nodos de los extremos: `delete(1)` y `delete(4)` → `'3'`
- ✅ Manejo de operaciones inválidas: `search(None)` → `False`, `delete(999)` no cambia longitud
- ✅ Tipos correctos: `search()` retorna bool, `length` es int

## 🔍 Análisis Paso a Paso

### Paso 1: Entender la Estructura Actual
```python
# Lista inicial: [1, 2, 3, 4]
head -> [1|next] -> [2|next] -> [3|next] -> [4|None]
```

### Paso 2: Operación Search
- Recorrer la lista nodo por nodo
- Comparar `current.data` con `target`
- Retornar `True` si encuentra, `False` si llega al final

### Paso 3: Operación Delete
**Casos especiales:**
1. **Lista vacía**: No hacer nada
2. **Eliminar head**: Actualizar `self.head = head.next`
3. **Eliminar nodo intermedio**: Conectar nodo anterior con siguiente
4. **Elemento no existe**: No hacer nada

## 💡 Solución Completa

```python
def search(self, target):
    """Return True if target exists, else False."""
    # Manejar caso inválido
    if target is None:
        return False
    
    # Recorrer la lista
    current = self.head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    
    # No encontrado
    return False

def delete(self, target):
    """Delete first node with data == target and update length."""
    # Manejar casos inválidos o lista vacía
    if target is None or self.head is None:
        return
    
    # Caso especial: eliminar el primer nodo (head)
    if self.head.data == target:
        self.head = self.head.next
        self.length -= 1
        return
    
    # Buscar el nodo a eliminar
    current = self.head
    while current.next is not None:
        if current.next.data == target:
            # Encontrado: conectar nodo actual con el siguiente al objetivo
            current.next = current.next.next
            self.length -= 1
            return
        current = current.next
    
    # No encontrado: no hacer nada
```

## 🧪 Verificación de Casos

### Estado Inicial
```python
ll = LinkedList()
for v in [1,2,3,4]:
    ll.insert_at_end(v)
# Lista: head -> [1] -> [2] -> [3] -> [4] -> None
```

### Caso 1: Search Found
```python
ll.search(3)  # Recorre: 1 → 2 → 3 ✅ → True
```

### Caso 2: Delete Middle
```python
ll.delete(2)
# Antes: [1] -> [2] -> [3] -> [4]
# Después: [1] -> [3] -> [4]  (conecta 1 directamente con 3)
# Result: '1 -> 3 -> 4' ✅
```

### Caso 3: Delete Ends
```python
ll.delete(1)  # Elimina head
# head = head.next → [3] -> [4]

ll.delete(4)  # Elimina último
# [3] -> None
# Result: '3' ✅
```

### Caso 4: Invalid Operations
```python
ll.search(None)  # → False ✅
ll.delete(999)   # Elemento no existe, length no cambia ✅
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
        # Manejar caso inválido
        if target is None:
            return False
        
        # Recorrer la lista
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        
        # No encontrado
        return False

    def delete(self, target):
        """Delete first node with data == target and update length."""
        # Manejar casos inválidos o lista vacía
        if target is None or self.head is None:
            return
        
        # Caso especial: eliminar el primer nodo (head)
        if self.head.data == target:
            self.head = self.head.next
            self.length -= 1
            return
        
        # Buscar el nodo a eliminar
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                # Encontrado: conectar nodo actual con el siguiente al objetivo
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next
        
        # No encontrado: no hacer nada

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

## 📊 Resultado Esperado
```
✅ o3.2.1 search(3) True
✅ o3.2.2 display == '1 -> 3 -> 4'
✅ o3.2.3 display == '3'
✅ o3.2.4 invalid handled
✅ o3.2.5 types ok
```

## 🎯 Visualización de Operaciones Delete

### Delete Middle Node (2)
```
Antes:  [1] -> [2] -> [3] -> [4] -> None
               ↑
            target
            
Después: [1] -----> [3] -> [4] -> None
         ↑                  ↑
    current.next = current.next.next
```

### Delete Head Node (1)
```
Antes:  [1] -> [3] -> [4] -> None
        ↑
     head (target)
     
Después: head -> [3] -> [4] -> None
```

### Delete Last Node (4)
```
Antes:  [3] -> [4] -> None
        ↑      ↑
    current  target
    
Después: [3] -> None
         ↑
    current.next = None
```

## 🔑 Puntos Clave

### Search Method
1. **Validación**: Rechazar `None` inmediatamente
2. **Traversal**: Recorrer nodo por nodo
3. **Comparación**: `current.data == target`
4. **Return**: `True` si encuentra, `False` al final

### Delete Method
1. **Validaciones**: Manejar `None` y lista vacía
2. **Caso head**: `self.head = self.head.next`
3. **Caso general**: Mantener referencia al nodo anterior
4. **Conexión**: `current.next = current.next.next`
5. **Actualizar longitud**: `self.length -= 1` solo si elimina

## ⚡ Complejidad

| Operación | Mejor Caso | Peor Caso | Promedio |
|-----------|------------|-----------|----------|
| `search()` | O(1) | O(n) | O(n) |
| `delete()` | O(1) | O(n) | O(n) |

- **Mejor caso**: Elemento en la primera posición
- **Peor caso**: Elemento en la última posición o no existe

## 🛡️ Casos Edge Manejados

1. **Lista vacía**: `delete()` no hace nada
2. **Target None**: `search()` → `False`, `delete()` no hace nada
3. **Elemento no existe**: `delete()` no cambia la lista ni longitud
4. **Un solo elemento**: Correctamente actualiza head a `None`
5. **Eliminar head**: Actualiza head correctamente

## 🎓 Conceptos Aprendidos
- **Traversal**: Recorrido secuencial de listas enlazadas
- **Pointer manipulation**: Reconectar nodos para eliminar
- **Edge case handling**: Manejar casos especiales como head y lista vacía
- **State consistency**: Mantener `length` sincronizado con la estructura
- **Boolean returns**: Funciones que retornan valores de verdad claros