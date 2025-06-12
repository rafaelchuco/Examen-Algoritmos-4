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
        if target is None:
            return False
        curr = self.head
        while curr:
            if curr.data == target:
                return True
            curr = curr.next
        return False

    def delete(self, target):
        """Delete first node with data == target and update length."""
        if target is None or self.head is None:
            return
        if self.head.data == target:
            self.head = self.head.next
            self.length -= 1
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == target:
                prev.next = curr.next
                self.length -= 1
                return
            prev = curr
            curr = curr.next

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
