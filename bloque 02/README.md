
## o2: Recursion & Backtracking 🌀🔙

### o2.1 🔁 **Recursive Factorial** 🧮✨

---

#### ❓ Problem 🤔

Implement `factorial(n)` to compute the factorial of `n` using **recursion**, and return the result. 🔄🧮

---

#### 📜 Description 📖

* **Function**: `factorial(n: int) → int or None` 🛠️
* **Inputs**:

  * `n`: non-negative integer (≥ 0) 🎯
* **Outputs**:

  * **result**: `n!` as an integer 🔢
  * **invalid**: return `None` if input invalid ❌
* **Time Complexity**: **O(n)** 🔄
* **Edge cases**:

  * `n = 0` → returns `1` (0! = 1) ⚠️
  * Very large `n` may hit recursion limits 🌋
* **Constraints**:

  * Must use **recursion** (no loops) 🔙
* **Input validation**:

  * If `n` is not an integer or `n < 0`, return `None` ❌⚙️

---

#### 🧪 Tests to Pass ✅

1. **o2.1.1**: Base case

   * Input: `n = 0`
   * Expect: returns `1` ✅
2. **o2.1.2**: Small n

   * Input: `n = 5`
   * Expect: returns `120` ✅
3. **o2.1.3**: Larger n

   * Input: `n = 7`
   * Expect: returns `5040` ✅
4. **o2.1.4**: Type-check test

   * Input: `n = 3`
   * Verify: return type is `int` 🆗
5. **o2.1.5**: Error-handling test

   * Input: `n = -1` and `n = "a"`
   * Expect: returns `None` for both ❌

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def factorial(n):
    """🔁 Compute n! recursively; return None if input invalid."""
    # Your solution here 🛠️
    pass

def test_o2_1():
    # o2.1.1: n = 0 → result = 1
    record_test("o2.1.1 n=0 → 1", factorial(0) == 1)
    # o2.1.2: n = 5 → result = 120
    record_test("o2.1.2 n=5 → 120", factorial(5) == 120)
    # o2.1.3: n = 7 → result = 5040
    record_test("o2.1.3 n=7 → 5040", factorial(7) == 5040)
    # o2.1.4: type-check
    out = factorial(3)
    record_test("o2.1.4 returns int", isinstance(out, int))
    # o2.1.5: invalid input → None
    record_test("o2.1.5 invalid returns None",
        factorial(-1) is None and factorial("a") is None)

# 🚀 Run tests
test_o2_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* **Base case**: if `n == 0`, return `1` 🌱.
* **Recursive step**: return `n * factorial(n-1)` 🔄.
* Validate input **before** recursion to avoid errors ❌.
* Watch out for Python’s **recursion depth** on large `n` 🌋.

---

#### 🧠 Motivation 💭

* Core example of **divide-and-conquer** breaking problems into smaller subproblems 🌳.
* Foundation for **dynamic programming** and memoization techniques 💾.
* Reinforces understanding of the **call stack** and recursion mechanics 🧠.

---

### o2.2 🔤 **Generate Binary Strings of Length N** 0️⃣1️⃣🛤️

---

#### ❓ Problem 🤔

Implement `generate_binary_strings(n)` to return all binary strings of length `n` using **backtracking**. 🔄🔤

---

#### 📜 Description 📖

* **Function**: `generate_binary_strings(n: int) → list[str]` 🛠️
* **Inputs**:

  * `n`: non-negative integer (length) 🎯
* **Outputs**:

  * **result**: list of all `'0'`/`'1'` strings of length `n` 📋
  * **invalid**: return `[]` if input invalid ❌
* **Time Complexity**: **O(2ⁿ · n)** 🔍
* **Edge cases**:

  * `n = 0` → returns `['']` (one empty string) ⚠️
  * Exponential growth for large `n` 🌋
* **Constraints**:

  * Must use **backtracking** (recursive generation) 🔙
* **Input validation**:

  * If `n` is not an integer or `n < 0`, return `[]` ❌⚙️

---

#### 🧪 Tests to Pass ✅

1. **o2.2.1**: n = 2 → list of 4

   * Expect: `['00','01','10','11']` ✅
2. **o2.2.2**: n = 3 → length = 8

   * Expect: `len(...) == 8` ✅
3. **o2.2.3**: contains specific string

   * Expect: `'101' in generate_binary_strings(3)` ✅
4. **o2.2.4**: Type-check test

   * Input: `n = 1`
   * Verify: return is `list`, elements are `str` 🆗
5. **o2.2.5**: Error-handling test

   * Input: `n = -1` and `n = "a"`
   * Expect: returns `[]` ❌

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    # Your solution here 🛠️
    pass

def test_o2_2():
    # o2.2.1: n = 2 → ['00','01','10','11']
    record_test("o2.2.1 n=2 → 4 strings",
        generate_binary_strings(2) == ['00','01','10','11'])
    # o2.2.2: n = 3 → length = 8
    record_test("o2.2.2 n=3 → length=8",
        len(generate_binary_strings(3)) == 8)
    # o2.2.3: contains '101'
    record_test("o2.2.3 contains '101'",
        '101' in generate_binary_strings(3))
    # o2.2.4: type-check
    res = generate_binary_strings(1)
    record_test("o2.2.4 returns list[str]",
        isinstance(res, list) and all(isinstance(s, str) for s in res))
    # o2.2.5: invalid input → []
    record_test("o2.2.5 invalid returns []",
        generate_binary_strings(-1) == [] and generate_binary_strings("a") == [])

# 🚀 Run tests
test_o2_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Use a **helper** function `backtrack(prefix)` to build strings step-by-step 🔧.
* At each recursion, append `'0'` then `'1'` and recurse 🔄.
* When `len(prefix) == n`, add to result 🌳.
* Validate `n` first to avoid unnecessary recursion ❌.

---

#### 🧠 Motivation 💭

* Demonstrates **backtracking** exploring all combinatorial branches 🌲.
* Foundation for **combinatorial** and **constraint-satisfaction** problems 🎯.
* Reinforces mastery of **recursive patterns** and **pruning**.

