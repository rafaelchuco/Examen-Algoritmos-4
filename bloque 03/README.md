
## o3: Linked Lists 📎🔗

### o3.1 ➕ **Insert at Beginning, Insert at End & Length** 🏁👶➕📏

---

#### ❓ Problem 🤔

Implement `insert_at_beginning(data)`, `insert_at_end(data)`, and maintain a `length` property in your `LinkedList` class. 🐍✨

---

#### 📜 Description 📖

* **Classes**:

  * `Node(data)` with attributes `data` and `next` 🧩
  * `LinkedList()` with:

    * `head` (initially `None`) 🎯
    * `length` (initially `0`) 🔢
* **Methods to implement**:

  1. **`insert_at_beginning(data)`** – create a new node at the head, update `head`, increment `length`.
  2. **`insert_at_end(data)`** – append a new node at the tail (or beginning if empty), increment `length`.
* **Helper**:

  * `display()` returns `"val1 -> val2 -> ..."` or `"Empty list"` if no nodes 🌳

---

#### 🧪 Tests to Pass ✅

1. **o3.1.1**: Mixed single insert

   * Actions:

     ```python
     ll.insert_at_beginning(2)
     ll.insert_at_end(3)
     ```
   * Expect: `ll.display()` returns `'2 -> 3'` ✅
2. **o3.1.2**: Mixed multiple inserts

   * Continuing above:

     ```python
     ll.insert_at_beginning(1)
     ll.insert_at_end(4)
     ```
   * Expect: `ll.display()` returns `'1 -> 2 -> 3 -> 4'` ✅
3. **o3.1.3**: Length tracking

   * After four successful inserts: `ll.length == 4` 🔢✅
4. **o3.1.4**: Invalid input handling

   * Record `old = ll.length` then:

     ```python
     ll.insert_at_beginning(None)
     ll.insert_at_end("x")
     ```
   * Expect: `ll.length` remains `old` (invalid ignored) ⚠️
5. **o3.1.5**: Return-type verification

   * Verify:

     ```python
     isinstance(ll.length, int)  # True 🆗  
     isinstance(ll.display(), str)  # True 🆗
     ```

---

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

#### 💡 Tips ✨

* Validate `data` (e.g., skip if `data is None`) before inserting.
* Handle **empty list** case separately in `insert_at_end`.
* Update `length` only on valid insert operations.

---

#### 🧠 Motivation 💭

* Teaches both **prepend** (stack) and **append** (queue) operations 🔄.
* Reinforces pointer updates and size tracking 🔢.
* Lays groundwork for advanced structures like **deque** and **circular lists**.

---

### o3.2 🔍❌ **Search & Delete** 🕵️‍♂️🗑️

---

#### ❓ Problem 🤔

Implement `search(target)` to check if a value exists, and `delete(target)` to remove the first matching node—updating `length`. 🔎❌

---

#### 📜 Description 📖

* **Class**: same `LinkedList` with `head`, `length`, `insert_*`, `display()`.
* **Methods to implement**:

  1. **`search(target)`** – traverse nodes, return `True` on match else `False`.
  2. **`delete(target)`** – unlink the first matching node, decrement `length`.

---

#### 🧪 Tests to Pass ✅

1. **o3.2.1**: Search found

   * Preload list with `[1,2,3,4]`
   * Expect: `ll.search(3) is True` ✅
2. **o3.2.2**: Delete middle

   * `ll.delete(2)` → `ll.display() == '1 -> 3 -> 4'` ✅
3. **o3.2.3**: Delete ends

   * `ll.delete(1)` then `ll.delete(4)` → `ll.display() == '3'` ✅
4. **o3.2.4**: Invalid operations

   * Record `old = ll.length`

     ```python
     ll.search(None) is False
     ll.delete(999)
     ll.length == old
     ```
   * Expect: no change, invalid ignored ⚠️
5. **o3.2.5**: Return-type verification

   * Verify:

     ```python
     isinstance(ll.search(3), bool)  # True 🆗  
     isinstance(ll.length, int)      # True 🆗
     ```

---

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

#### 💡 Tips ✨

* **search(target)**: iterate `while curr:`, return early on match.
* **delete(target)**: handle head removal, then unlink using `prev` & `curr`.
* Only decrement `length` when deletion occurs.

---

#### 🧠 Motivation 💭

* Combines **lookup** and **removal**—key for dynamic collections 🔄.
* Emphasizes robust **edge-case** handling (head/tail/absent) 🎯.
* Prepares for advanced list manipulations like **filter** & **splice**.

