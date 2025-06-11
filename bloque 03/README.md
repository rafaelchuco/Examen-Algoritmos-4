# o3: Listas Enlazadas 📎🔗

## o3.1 ➕ **Insertar al Inicio, Insertar al Final y Longitud** 🏁👶➕📏

---

### ❓ Problema 🤔

Implementa los métodos `insert_at_beginning(data)`, `insert_at_end(data)`, y mantén una propiedad `length` en tu clase `LinkedList`. 🐍✨

---

### 📜 Descripción 📖

Necesitas crear una estructura de datos de lista enlazada con las siguientes características:

* **Clases requeridas**:
  * `Node(data)` con atributos `data` (datos) y `next` (siguiente nodo) 🧩
  * `LinkedList()` con:
    * `head` (cabeza de la lista, inicialmente `None`) 🎯
    * `length` (longitud de la lista, inicialmente `0`) 🔢

* **Métodos a implementar**:
  1. **`insert_at_beginning(data)`** – Crea un nuevo nodo al inicio de la lista, actualiza `head` e incrementa `length`
  2. **`insert_at_end(data)`** – Agrega un nuevo nodo al final de la lista (o al inicio si está vacía), incrementa `length`

* **Método auxiliar ya implementado**:
  * `display()` retorna `"val1 -> val2 -> ..."` o `"Empty list"` si no hay nodos 🌳

---

### 🧪 Pruebas que Debes Pasar ✅

Tu implementación debe pasar todas estas pruebas:

1. **o3.1.1**: Inserción mixta simple
   * **Acciones**:
     ```python
     ll.insert_at_beginning(2)  # Insertar 2 al inicio
     ll.insert_at_end(3)        # Insertar 3 al final
     ```
   * **Resultado esperado**: `ll.display()` debe retornar `'2 -> 3'` ✅

2. **o3.1.2**: Múltiples inserciones mixtas
   * **Continuando con el caso anterior**:
     ```python
     ll.insert_at_beginning(1)  # Insertar 1 al inicio
     ll.insert_at_end(4)        # Insertar 4 al final
     ```
   * **Resultado esperado**: `ll.display()` debe retornar `'1 -> 2 -> 3 -> 4'` ✅

3. **o3.1.3**: Seguimiento de longitud
   * **Después de cuatro inserciones exitosas**: `ll.length == 4` 🔢✅

4. **o3.1.4**: Manejo de entrada inválida
   * **Guarda el valor actual**: `old = ll.length`
   * **Luego ejecuta**:
     ```python
     ll.insert_at_beginning(None)  # Entrada inválida
     ll.insert_at_end("x")         # Entrada inválida
     ```
   * **Resultado esperado**: `ll.length` debe permanecer igual a `old` (las entradas inválidas se ignoran) ⚠️

5. **o3.1.5**: Verificación de tipos de retorno
   * **Verifica que**:
     ```python
     isinstance(ll.length, int)    # Debe ser True 🆗  
     isinstance(ll.display(), str) # Debe ser True 🆗
     ```

---

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

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        """Insert new node at beginning and update length."""
        # Your solution here 🛠️
        pass

    def insert_at_end(self, data):
        """Insert new node at end and update length."""
        # Your solution here 🛠️
        pass

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

---

### 💡 Consejos Útiles ✨

* **Validación de datos**: Verifica que `data` sea válido (por ejemplo, omite la inserción si `data is None`) antes de insertar
* **Caso de lista vacía**: Maneja el caso especial de lista vacía por separado en `insert_at_end`
* **Actualización de longitud**: Solo actualiza `length` cuando la operación de inserción sea válida y exitosa
* **Gestión de punteros**: Asegúrate de actualizar correctamente los punteros `next` y `head`

---

### 🧠 Motivación y Aprendizaje 💭

Este ejercicio te enseña conceptos fundamentales:

* **Operaciones básicas**: Tanto operaciones de **prepend** (agregar al inicio, como en una pila) como **append** (agregar al final, como en una cola) 🔄
* **Gestión de memoria**: Refuerza la comprensión de actualizaciones de punteros y seguimiento de tamaño 🔢
* **Fundamentos sólidos**: Establece las bases para estructuras de datos más avanzadas como **deque** y **listas circulares**
* **Manejo de errores**: Practica la validación de entrada y el manejo robusto de casos especiales

---

## o3.2 🔍❌ **Búsqueda y Eliminación** 🕵️‍♂️🗑️

---

### ❓ Problema 🤔

Implementa `search(target)` para verificar si un valor existe en la lista, y `delete(target)` para eliminar el primer nodo que coincida con el valor objetivo, actualizando la `length`. 🔎❌

---

### 📜 Descripción 📖

Trabajarás con la misma clase `LinkedList` que ya tiene `head`, `length`, métodos `insert_*`, y `display()`.

* **Métodos a implementar**:
  1. **`search(target)`** – Recorre los nodos de la lista y retorna `True` si encuentra una coincidencia, `False` en caso contrario
  2. **`delete(target)`** – Desenlaza el primer nodo que coincida con el valor objetivo y decrementa `length`

---

### 🧪 Pruebas que Debes Pasar ✅

Tu implementación debe pasar todas estas pruebas:

1. **o3.2.1**: Búsqueda exitosa
   * **Preparación**: Precarga la lista con `[1,2,3,4]`
   * **Resultado esperado**: `ll.search(3) is True` ✅

2. **o3.2.2**: Eliminación en el medio
   * **Acción**: `ll.delete(2)`
   * **Resultado esperado**: `ll.display() == '1 -> 3 -> 4'` ✅

3. **o3.2.3**: Eliminación en los extremos
   * **Acciones**: `ll.delete(1)` luego `ll.delete(4)`
   * **Resultado esperado**: `ll.display() == '3'` ✅

4. **o3.2.4**: Operaciones inválidas
   * **Guarda el valor actual**: `old = ll.length`
   * **Ejecuta**:
     ```python
     ll.search(None) is False  # Búsqueda inválida
     ll.delete(999)            # Eliminación de valor inexistente
     ll.length == old          # La longitud no debe cambiar
     ```
   * **Resultado esperado**: Sin cambios, las operaciones inválidas se ignoran ⚠️

5. **o3.2.5**: Verificación de tipos de retorno
   * **Verifica que**:
     ```python
     isinstance(ll.search(3), bool)  # Debe ser True 🆗  
     isinstance(ll.length, int)      # Debe ser True 🆗
     ```

---

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
        # Your solution here 🛠️
        pass

    def delete(self, target):
        """Delete first node with data == target and update length."""
        # Your solution here 🛠️
        pass

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

---

### 💡 Consejos Útiles ✨

* **Método search(target)**: Itera usando `while curr:` y retorna `True` inmediatamente cuando encuentres una coincidencia
* **Método delete(target)**: 
  - Maneja por separado la eliminación del nodo cabeza (head)
  - Para otros nodos, usa variables `prev` (anterior) y `curr` (actual) para desenlazan correctamente
  - Recuerda actualizar los punteros antes de eliminar el nodo
* **Gestión de longitud**: Solo decrementa `length` cuando la eliminación realmente ocurra
* **Validación**: Verifica que el valor objetivo sea válido antes de proceder con las operaciones

---

### 🧠 Motivación y Aprendizaje 💭

Este ejercicio avanzado te enseña:

* **Operaciones de consulta**: Combina **búsqueda** y **eliminación**, operaciones clave para colecciones dinámicas 🔄
* **Manejo robusto de casos especiales**: Enfatiza el manejo de situaciones límite como eliminación de cabeza/cola/elemento ausente 🎯
* **Preparación para operaciones avanzadas**: Te prepara para manipulaciones más complejas de listas como **filtrado** y **empalme**
* **Gestión eficiente de memoria**: Aprende a liberar nodos correctamente y mantener la integridad de la estructura

### 🔑 Conceptos Clave

- **Búsqueda lineal**: Recorrido secuencial para encontrar elementos
- **Eliminación con preservación de enlaces**: Mantener la continuidad de la lista después de eliminar nodos
- **Casos especiales**: Lista vacía, eliminación del primer/último elemento
- **Validación robusta**: Manejo de entradas inválidas sin afectar la estructura