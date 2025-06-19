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