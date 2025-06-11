import time

# Lista global para almacenar los resultados de las pruebas
test_results = []


def record_test(test_name, condition):
    """Ejecuta una prueba y registra el resultado con emoji de estado."""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# SECCIÓN 1: COMPLEJIDAD ALGORÍTMICA
# ====================================================================

def logarithmic_complexity(n):
    """
    Cuenta cuántas veces se debe doblar el valor 1 para exceder n.
    
    Args:
        n: Número entero positivo a superar
        
    Returns:
        tuple: (contador, tiempo_transcurrido) si es válido, (-1, tiempo) si no
    """
    start = time.time()
    
    # Validación de entrada
    if not isinstance(n, int) or n < 1:
        end = time.time()
        return -1, end - start

    # Bucle de duplicación
    value = 1
    count = 0
    while value <= n:
        value *= 2  # Duplicar valor
        count += 1  # Incrementar contador
        
    end = time.time()
    elapsed = end - start
    return count, elapsed


def constant_sum(n):
    """
    Calcula la suma de los primeros n números naturales en tiempo O(1).
    
    Args:
        n: Número entero no negativo
        
    Returns:
        tuple: (suma, tiempo_transcurrido) si es válido, (-1, tiempo) si no
    """
    start = time.time()
    
    # Validación de entrada
    if not isinstance(n, int) or n < 0:
        end = time.time()
        return -1, end - start

    # Fórmula matemática directa: n * (n + 1) / 2
    total = n * (n + 1) // 2
    end = time.time()
    elapsed = end - start
    return total, elapsed


# ====================================================================
# SECCIÓN 2: RECURSIÓN Y BACKTRACKING
# ====================================================================

def factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        int: El factorial de n, o None si la entrada es inválida
    """
    # Validación de entrada
    if not isinstance(n, int) or n < 0:
        return None
        
    # Caso base
    if n == 0:
        return 1
        
    # Caso recursivo
    return n * factorial(n - 1)


def generate_binary_strings(n):
    """
    Genera todas las cadenas binarias de longitud n usando backtracking.
    
    Args:
        n: Longitud de las cadenas binarias a generar
        
    Returns:
        list: Lista de todas las cadenas binarias posibles
    """
    # Validación de entrada
    if not isinstance(n, int) or n < 0:
        return []
        
    result = []

    def backtrack(prefix):
        """Función auxiliar recursiva para generar cadenas."""
        if len(prefix) == n:
            result.append(prefix)
            return
        # Agregar '0' y '1' recursivamente
        backtrack(prefix + "0")
        backtrack(prefix + "1")

    backtrack("")
    return result


# ====================================================================
# SECCIÓN 3: LISTAS ENLAZADAS
# ====================================================================

class Node:
    """Nodo individual de una lista enlazada."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Lista enlazada simple con operaciones básicas:
    inserción, visualización, búsqueda, eliminación y longitud.
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        if not isinstance(data, int):
            return
            
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        """Inserta un nuevo nodo al final de la lista."""
        if not isinstance(data, int):
            return
            
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
        self.length += 1

    def display(self):
        """Retorna una representación en cadena de la lista."""
        current = self.head
        values = []
        
        while current:
            values.append(str(current.data))
            current = current.next
            
        return " -> ".join(values) if values else "Lista vacía"

    def search(self, target):
        """Busca un valor en la lista y retorna True si lo encuentra."""
        if not isinstance(target, int):
            return False
            
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
            
        return False

    def delete(self, target):
        """Elimina el primer nodo que contenga el valor objetivo."""
        if not isinstance(target, int):
            return

        # Eliminar el primer nodo (head)
        if self.head and self.head.data == target:
            self.head = self.head.next
            self.length -= 1
            return

        # Buscar y eliminar en el resto de la lista
        previous = None
        current = self.head
        
        while current:
            if current.data == target:
                previous.next = current.next
                self.length -= 1
                return
            previous = current
            current = current.next


# ====================================================================
# PRUEBAS UNITARIAS
# ====================================================================

def test_complexity_algorithms():
    """Pruebas para algoritmos de complejidad."""
    print("\n=== Probando Complejidad Algorítmica ===")
    
    # Pruebas para complejidad logarítmica
    count, _ = logarithmic_complexity(1)
    record_test("Complejidad logarítmica: n=1 → contador=1", count == 1)
    
    count, _ = logarithmic_complexity(10)
    record_test("Complejidad logarítmica: n=10 → contador=4", count == 4)
    
    count, _ = logarithmic_complexity(100)
    record_test("Complejidad logarítmica: n=100 → contador=7", count == 7)
    
    # Verificación de tipos
    output = logarithmic_complexity(5)
    record_test("Complejidad logarítmica: retorna (int, float)", 
                isinstance(output[0], int) and isinstance(output[1], float))
    
    # Manejo de errores
    count_error, _ = logarithmic_complexity("a")
    record_test("Complejidad logarítmica: entrada inválida retorna -1", count_error == -1)
    
    # Pruebas para suma constante
    sum_result, _ = constant_sum(0)
    record_test("Suma constante: n=0 → suma=0", sum_result == 0)
    
    sum_result, _ = constant_sum(1)
    record_test("Suma constante: n=1 → suma=1", sum_result == 1)
    
    sum_result, _ = constant_sum(10)
    record_test("Suma constante: n=10 → suma=55", sum_result == 55)
    
    # Verificación de tipos
    output = constant_sum(5)
    record_test("Suma constante: retorna (int, float)",
                isinstance(output[0], int) and isinstance(output[1], float))
    
    # Manejo de errores
    sum_error, _ = constant_sum("a")
    record_test("Suma constante: entrada inválida retorna -1", sum_error == -1)


def test_recursion_algorithms():
    """Pruebas para algoritmos recursivos."""
    print("\n=== Probando Recursión y Backtracking ===")
    
    # Pruebas de factorial
    record_test("Factorial: n=0 → 1", factorial(0) == 1)
    record_test("Factorial: n=5 → 120", factorial(5) == 120)
    record_test("Factorial: n=7 → 5040", factorial(7) == 5040)
    record_test("Factorial: retorna int", isinstance(factorial(3), int))
    record_test("Factorial: entrada inválida retorna None", 
                factorial(-1) is None and factorial("a") is None)
    
    # Pruebas de cadenas binarias
    binary_2 = generate_binary_strings(2)
    record_test("Cadenas binarias: n=2 → ['00','01','10','11']", 
                binary_2 == ["00", "01", "10", "11"])
    
    binary_3 = generate_binary_strings(3)
    record_test("Cadenas binarias: n=3 → longitud=8", len(binary_3) == 8)
    record_test("Cadenas binarias: contiene '101'", "101" in binary_3)
    
    result = generate_binary_strings(1)
    record_test("Cadenas binarias: retorna list[str]",
                isinstance(result, list) and all(isinstance(s, str) for s in result))
    
    record_test("Cadenas binarias: entrada inválida retorna []",
                generate_binary_strings(-1) == [] and generate_binary_strings("a") == [])


def test_linked_list():
    """Pruebas para lista enlazada."""
    print("\n=== Probando Listas Enlazadas ===")
    
    # Pruebas de inserción y longitud
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_end(3)
    record_test("Lista enlazada: inserción mixta → '2 -> 3'", ll.display() == "2 -> 3")
    
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    record_test("Lista enlazada: múltiples inserciones → '1 -> 2 -> 3 -> 4'", 
                ll.display() == "1 -> 2 -> 3 -> 4")
    
    record_test("Lista enlazada: seguimiento de longitud = 4", ll.length == 4)
    
    # Manejo de entradas inválidas
    old_length = ll.length
    ll.insert_at_beginning(None)
    ll.insert_at_end("x")
    record_test("Lista enlazada: entradas inválidas ignoradas", ll.length == old_length)
    
    # Verificación de tipos de retorno
    record_test("Lista enlazada: tipos correctos",
                isinstance(ll.length, int) and isinstance(ll.display(), str))
    
    # Pruebas de búsqueda y eliminación
    ll2 = LinkedList()
    for valor in [1, 2, 3, 4]:
        ll2.insert_at_end(valor)
    
    record_test("Lista enlazada: búsqueda(3) = True", ll2.search(3) is True)
    
    ll2.delete(2)
    record_test("Lista enlazada: eliminar medio → '1 -> 3 -> 4'", 
                ll2.display() == "1 -> 3 -> 4")
    
    ll2.delete(1)
    ll2.delete(4)
    record_test("Lista enlazada: eliminar extremos → '3'", ll2.display() == "3")
    
    # Operaciones inválidas
    old_length = ll2.length
    invalid_search = ll2.search(None) is False
    ll2.delete(999)
    invalid_operations_handled = invalid_search and (ll2.length == old_length)
    record_test("Lista enlazada: operaciones inválidas manejadas", invalid_operations_handled)
    
    # Verificación de tipos
    record_test("Lista enlazada: tipos de búsqueda correctos",
                isinstance(ll2.search(3), bool) and isinstance(ll2.length, int))


def run_all_tests():
    """Ejecuta todas las pruebas y muestra el resumen final."""
    print("🚀 Iniciando Examen de Estructuras de Datos y Algoritmos")
    print("=" * 60)
    
    test_complexity_algorithms()
    test_recursion_algorithms()
    test_linked_list()
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📋 RESUMEN FINAL DE PRUEBAS")
    print("=" * 60)
    
    for result in test_results:
        print(result)
    
    approved = sum('✅' in result for result in test_results)
    failed = sum('❌' in result for result in test_results)
    
    print(f"\nTotal Aprobadas: {approved} ✅")
    print(f"Total Fallidas: {failed} ❌")
    print(f"Porcentaje de Éxito: {(approved / (approved + failed) * 100):.1f}%")


# Ejecutar todas las pruebas
if __name__ == "__main__":
    run_all_tests()