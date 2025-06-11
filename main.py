import time
import os

# Lista global para almacenar los resultados de las pruebas
test_results = []

# Códigos de color ANSI para terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    GRAY = '\033[90m'

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, color=Colors.CYAN):
    """Imprime un encabezado decorado."""
    print(f"\n{color}{Colors.BOLD}{'='*70}")
    print(f"🎯 {title.upper()}")
    print(f"{'='*70}{Colors.END}")

def print_section(title, color=Colors.BLUE):
    """Imprime una sección decorada."""
    print(f"\n{color}{Colors.BOLD}{'─'*50}")
    print(f"📚 {title}")
    print(f"{'─'*50}{Colors.END}")

def record_test(test_name, condition):
    """Ejecuta una prueba y registra el resultado con emoji de estado y colores."""
    if condition:
        emoji = "✅"
        color = Colors.GREEN
        status = "PASS"
    else:
        emoji = "❌"
        color = Colors.RED
        status = "FAIL"
    
    formatted_result = f"{color}{emoji} {test_name} [{status}]{Colors.END}"
    test_results.append((formatted_result, condition))
    print(f"  {formatted_result}")

def print_performance_info(func_name, elapsed_time):
    """Muestra información de rendimiento."""
    print(f"  {Colors.GRAY}⏱️  Tiempo de ejecución: {elapsed_time:.6f}s{Colors.END}")


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
    print_section("🧮 ALGORITMOS DE COMPLEJIDAD", Colors.YELLOW)
    
    print(f"\n{Colors.BOLD}🔍 Probando Complejidad Logarítmica O(log n){Colors.END}")
    
    # Pruebas para complejidad logarítmica
    count, elapsed = logarithmic_complexity(1)
    record_test("n=1 → contador=1", count == 1)
    print_performance_info("logarithmic_complexity", elapsed)
    
    count, elapsed = logarithmic_complexity(10)
    record_test("n=10 → contador=4", count == 4)
    print_performance_info("logarithmic_complexity", elapsed)
    
    count, elapsed = logarithmic_complexity(100)
    record_test("n=100 → contador=7", count == 7)
    print_performance_info("logarithmic_complexity", elapsed)
    
    # Verificación de tipos
    output = logarithmic_complexity(5)
    record_test("Retorna tipos correctos (int, float)", 
                isinstance(output[0], int) and isinstance(output[1], float))
    
    # Manejo de errores
    count_error, _ = logarithmic_complexity("a")
    record_test("Manejo de entrada inválida", count_error == -1)
    
    print(f"\n{Colors.BOLD}⚡ Probando Suma Constante O(1){Colors.END}")
    
    # Pruebas para suma constante
    sum_result, elapsed = constant_sum(0)
    record_test("n=0 → suma=0", sum_result == 0)
    print_performance_info("constant_sum", elapsed)
    
    sum_result, elapsed = constant_sum(1)
    record_test("n=1 → suma=1", sum_result == 1)
    print_performance_info("constant_sum", elapsed)
    
    sum_result, elapsed = constant_sum(10)
    record_test("n=10 → suma=55", sum_result == 55)
    print_performance_info("constant_sum", elapsed)
    
    # Verificación de tipos
    output = constant_sum(5)
    record_test("Retorna tipos correctos (int, float)",
                isinstance(output[0], int) and isinstance(output[1], float))
    
    # Manejo de errores
    sum_error, _ = constant_sum("a")
    record_test("Manejo de entrada inválida", sum_error == -1)


def test_recursion_algorithms():
    """Pruebas para algoritmos recursivos."""
    print_section("🌀 RECURSIÓN Y BACKTRACKING", Colors.CYAN)
    
    print(f"\n{Colors.BOLD}🧮 Probando Factorial Recursivo{Colors.END}")
    
    # Pruebas de factorial
    record_test("factorial(0) = 1", factorial(0) == 1)
    record_test("factorial(5) = 120", factorial(5) == 120)
    record_test("factorial(7) = 5040", factorial(7) == 5040)
    record_test("Retorna tipo int", isinstance(factorial(3), int))
    record_test("Manejo de entrada inválida", 
                factorial(-1) is None and factorial("a") is None)
    
    print(f"\n{Colors.BOLD}🔢 Probando Generador de Cadenas Binarias{Colors.END}")
    
    # Pruebas de cadenas binarias
    binary_2 = generate_binary_strings(2)
    record_test("n=2 genera 4 cadenas correctas", 
                binary_2 == ["00", "01", "10", "11"])
    
    binary_3 = generate_binary_strings(3)
    record_test("n=3 genera 8 cadenas", len(binary_3) == 8)
    record_test("Contiene cadena '101'", "101" in binary_3)
    
    result = generate_binary_strings(1)
    record_test("Retorna list[str]",
                isinstance(result, list) and all(isinstance(s, str) for s in result))
    
    record_test("Manejo de entrada inválida",
                generate_binary_strings(-1) == [] and generate_binary_strings("a") == [])


def test_linked_list():
    """Pruebas para lista enlazada."""
    print_section("🔗 LISTAS ENLAZADAS", Colors.GREEN)
    
    print(f"\n{Colors.BOLD}➕ Probando Inserción y Longitud{Colors.END}")
    
    # Pruebas de inserción y longitud
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_end(3)
    record_test("Inserción mixta: '2 -> 3'", ll.display() == "2 -> 3")
    
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    record_test("Múltiples inserciones: '1 -> 2 -> 3 -> 4'", 
                ll.display() == "1 -> 2 -> 3 -> 4")
    
    record_test("Seguimiento de longitud = 4", ll.length == 4)
    
    # Manejo de entradas inválidas
    old_length = ll.length
    ll.insert_at_beginning(None)
    ll.insert_at_end("x")
    record_test("Entradas inválidas ignoradas", ll.length == old_length)
    
    # Verificación de tipos de retorno
    record_test("Tipos de retorno correctos",
                isinstance(ll.length, int) and isinstance(ll.display(), str))
    
    print(f"\n{Colors.BOLD}🔍 Probando Búsqueda y Eliminación{Colors.END}")
    
    # Pruebas de búsqueda y eliminación
    ll2 = LinkedList()
    for valor in [1, 2, 3, 4]:
        ll2.insert_at_end(valor)
    
    record_test("Búsqueda exitosa: search(3) = True", ll2.search(3) is True)
    
    ll2.delete(2)
    record_test("Eliminar elemento medio: '1 -> 3 -> 4'", 
                ll2.display() == "1 -> 3 -> 4")
    
    ll2.delete(1)
    ll2.delete(4)
    record_test("Eliminar extremos: '3'", ll2.display() == "3")
    
    # Operaciones inválidas
    old_length = ll2.length
    invalid_search = ll2.search(None) is False
    ll2.delete(999)
    invalid_operations_handled = invalid_search and (ll2.length == old_length)
    record_test("Operaciones inválidas manejadas", invalid_operations_handled)
    
    # Verificación de tipos
    record_test("Tipos de búsqueda correctos",
                isinstance(ll2.search(3), bool) and isinstance(ll2.length, int))


def print_progress_bar(progress, total, length=40):
    """Muestra una barra de progreso visual."""
    percent = (progress / total) * 100
    filled = int(length * progress // total)
    bar = '█' * filled + '░' * (length - filled)
    
    if percent >= 80:
        color = Colors.GREEN
    elif percent >= 60:
        color = Colors.YELLOW
    else:
        color = Colors.RED
    
    return f"{color}[{bar}] {percent:.1f}%{Colors.END}"

def run_all_tests():
    """Ejecuta todas las pruebas y muestra el resumen final."""
    clear_screen()
    
    # Banner principal
    print(f"{Colors.BOLD}{Colors.CYAN}")
    print("╔" + "═" * 68 + "╗")
    print("║" + "🚀 EXAMEN DE ESTRUCTURAS DE DATOS Y ALGORITMOS 🚀".center(68) + "║")
    print("╚" + "═" * 68 + "╝")
    print(f"{Colors.END}")
    
    print(f"{Colors.GRAY}Iniciando batería de pruebas...{Colors.END}")
    time.sleep(1)
    
    # Ejecutar pruebas
    start_time = time.time()
    test_complexity_algorithms()
    test_recursion_algorithms()
    test_linked_list()
    end_time = time.time()
    
    # Calcular estadísticas
    total_tests = len(test_results)
    passed_tests = sum(1 for _, passed in test_results if passed)
    failed_tests = total_tests - passed_tests
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    
    # Resumen final con estilo
    print_header("📊 RESUMEN FINAL DE RESULTADOS", Colors.BOLD)
    
    print(f"\n{Colors.BOLD}📈 ESTADÍSTICAS GENERALES:{Colors.END}")
    print(f"  🔢 Total de pruebas ejecutadas: {Colors.BOLD}{total_tests}{Colors.END}")
    print(f"  ✅ Pruebas aprobadas: {Colors.GREEN}{Colors.BOLD}{passed_tests}{Colors.END}")
    print(f"  ❌ Pruebas fallidas: {Colors.RED}{Colors.BOLD}{failed_tests}{Colors.END}")
    print(f"  ⏱️  Tiempo total de ejecución: {Colors.CYAN}{end_time - start_time:.4f}s{Colors.END}")
    
    print(f"\n{Colors.BOLD}📊 TASA DE ÉXITO:{Colors.END}")
    progress_bar = print_progress_bar(passed_tests, total_tests)
    print(f"  {progress_bar}")
    
    # Clasificación del rendimiento
    print(f"\n{Colors.BOLD}🏆 CALIFICACIÓN:{Colors.END}")
    if success_rate >= 90:
        grade = f"{Colors.GREEN}{Colors.BOLD}EXCELENTE 🌟{Colors.END}"
        emoji = "🏆"
    elif success_rate >= 80:
        grade = f"{Colors.CYAN}{Colors.BOLD}MUY BUENO 👍{Colors.END}"
        emoji = "🥈"
    elif success_rate >= 70:
        grade = f"{Colors.YELLOW}{Colors.BOLD}BUENO 👌{Colors.END}"
        emoji = "🥉"
    elif success_rate >= 60:
        grade = f"{Colors.YELLOW}{Colors.BOLD}REGULAR 😐{Colors.END}"
        emoji = "📚"
    else:
        grade = f"{Colors.RED}{Colors.BOLD}NECESITA MEJORAR 📖{Colors.END}"
        emoji = "💪"
    
    print(f"  {emoji} {grade} ({success_rate:.1f}%)")
    
    # Lista detallada de resultados solo si hay fallos
    if failed_tests > 0:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ PRUEBAS FALLIDAS:{Colors.END}")
        for result, passed in test_results:
            if not passed:
                print(f"  {result}")
    
    # Mensaje motivacional final
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'─' * 70}")
    if success_rate >= 80:
        print("🎉 ¡Felicitaciones! Excelente dominio de las estructuras de datos.")
    elif success_rate >= 60:
        print("👏 ¡Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("💪 ¡No te rindas! La práctica hace al maestro. ¡Sigue adelante!")
    print(f"{'─' * 70}{Colors.END}")


# Ejecutar todas las pruebas
if __name__ == "__main__":
    run_all_tests()