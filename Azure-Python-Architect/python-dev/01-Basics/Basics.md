Perfect! Since you're transitioning from Java/Node.js to Python, I’ll show **each basic Python concept** with **2–3 clear examples**, and explain how they compare or feel similar to what you're used to.

---

## ✅ 1. **Variables and Data Types**

Python is dynamically typed (no `int`, `String` declarations like Java).

```python
name = "Sri"
age = 40
pi = 3.14159
is_active = True
```

```python
# Type conversion
age_str = str(age)
print("My age is " + age_str)  # My age is 40
```

---

## ✅ 2. **Conditionals**

Indentation replaces `{}`

```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```

```python
# Ternary expression
status = "Active" if is_active else "Inactive"
```

---

## ✅ 3. **Loops**

### `for` loop

```python
for i in range(3):
    print(i)  # 0, 1, 2
```

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### `while` loop

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## ✅ 4. **Functions**

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Sri"))  # Hello, Sri
```

```python
# Default and keyword arguments
def add(a, b=10):
    return a + b

print(add(5))       # 15
print(add(5, 3))    # 8
```

---

## ✅ 5. **Lists and Tuples**

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
```

```python
# Tuple (immutable)
coords = (10, 20)
x, y = coords
print(x, y)  # 10 20
```

---

## ✅ 6. **Dictionaries**

```python
person = {"name": "Sri", "age": 40}
print(person["name"])  # Sri
```

```python
# Adding a key
person["city"] = "Dallas"
```

---

## ✅ 7. **List Comprehension**

```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

```python
# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
```

---

## ✅ 8. **String Formatting**

```python
name = "Sri"
print(f"Hello {name}")  # Hello Sri
```

```python
age = 40
print("Age: {}".format(age))  # Age: 40
```

---

## ✅ 9. **Exception Handling**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

```python
try:
    name = person["first"]
except KeyError:
    print("Key not found")
```

---

## ✅ 10. **Importing Modules**

```python
import math
print(math.sqrt(16))  # 4.0
```

```python
from datetime import datetime
print(datetime.now())
```

---

Would you like me to bundle this into a small Python file you can run or save as a cheat sheet PDF?

Or want to continue to **OOP (classes/objects)** next?
