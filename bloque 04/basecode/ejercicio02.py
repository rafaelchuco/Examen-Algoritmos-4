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