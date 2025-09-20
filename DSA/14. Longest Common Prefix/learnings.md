


## 1. `None` vs Empty

- **None** → Special object in Python that means *no value* (absence of data).  
- **Empty** → A valid object, but it contains nothing inside it (like `[]`, `""`, `{}`).

### Example:
```python
# None
x = None
print(x is None)   # True
print(bool(x))     # False

# Empty list
y = []
print(y == [])     # True
print(bool(y))     # False, because it's empty

# Empty string
z = ""
print(z == "")     # True
print(bool(z))     # False
````

✅ **Key Point:**

* `None` = *nothing at all*
* Empty = *something exists, but it’s empty*

---

## 2. `if not strs:` in Python

```python
if not strs:
```

* Checks if `strs` is **falsy**.
* Falsy values in Python: `None`, `0`, `""`, `[]`, `{}`, `set()`, `False`.

So → `if not strs:` already covers:

* `None`
* Empty list `[]`

### Example:


strs = None
if not strs:
    print("No input")   # Prints

strs = []
if not strs:
    print("Empty list") # Prints
```

---

## 3. Why `len(strs) == 0` is sometimes used?

* In **Java/C++**:

  * `strs == null` → check if not initialized.
  * `strs.length == 0` → check if empty.
  * That’s why both are written together.

* In **Python**:

  * `if not strs:` already handles both `None` and empty.
  * Writing `len(strs) == 0` is **redundant**, but sometimes people include it for readability or habit.

✅ **Pythonic Way:**

```python
if not strs:
    return ""
```

---

## 4. `.find()` Method in Python

* `.find(substring)` → returns the index of the first occurrence of `substring`.
* If not found → returns `-1`.

### Examples:

```python
word = "Flower"

print(word.find("Flo"))   # 0  ("Flo" starts at index 0)
print(word.find("low"))   # 1  ("low" starts at index 1)
print(word.find("wer"))   # 3  ("wer" starts at index 3)
print(word.find("xyz"))   # -1 (not found)
```

---

## 5. Why `strs[i].find(prefix) != 0`?

* We want the **prefix to be at the start** of the string (index `0`).
* If `.find(prefix) != 0`:

  * The prefix exists but **not at the beginning**, OR
  * Prefix doesn’t exist at all (`-1`).
* In that case, shorten the prefix and re-check.

### Example:

```python
prefix = "Flow"
word = "Float"

print(word.find(prefix))   # -1, "Flow" not in "Float"

# Shorten prefix
prefix = "Flo"
print(word.find(prefix))   # 0, "Flo" starts at index 0 → valid prefix
```

---

## 6. Alternative Pythonic Way: `startswith()`

Instead of using `.find()`, Python has a clearer method:

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix
```

✅ Much cleaner and easier to understand.

---

## 🔑 Key Takeaways

* `None` = no value, Empty = valid but contains nothing.
* `if not strs:` covers both `None` and empty in Python.
* `.find()` helps locate substrings, but for prefixes `startswith()` is better.
* Always prefer **Pythonic ways** over Java-style checks.



<br>
<br>




# Python String Method: `startswith()`

The `startswith()` method in Python is used to check whether a string **starts with a specified prefix**. It returns **`True`** if the string starts with the given prefix, otherwise it returns **`False`**.

---

## Syntax

```python
str.startswith(prefix[, start[, end]])
````

### Parameters

* **prefix**: The substring or tuple of substrings to check for at the start of the string.
* **start** *(optional)*: The starting index from where the check begins. Default is `0`.
* **end** *(optional)*: The ending index where the check stops. Default is the end of the string.

---

## Return Value

* Returns `True` if the string starts with the specified prefix within the given range.
* Returns `False` otherwise.

---

## Example 1: Basic Usage

```python
text = "Hello, world!"
result = text.startswith("Hello")
print(result)  # Output: True

result = text.startswith("world")
print(result)  # Output: False
```

**Explanation:**

* The string `"Hello, world!"` **starts with** `"Hello"`, so the first check returns `True`.
* It does **not start with** `"world"`, so the second check returns `False`.

---

## Example 2: Using `start` and `end` Parameters

```python
text = "Hello, world!"
result = text.startswith("world", 7, 12)
print(result)  # Output: True
```

**Explanation:**

* Here, we are checking if the substring from index `7` to `12` starts with `"world"`.
* The substring `text[7:12]` is `"world"`, so the result is `True`.

---

## Example 3: Using a Tuple of Prefixes

```python
text = "Hello, world!"
result = text.startswith(("Hi", "Hello"))
print(result)  # Output: True
```

**Explanation:**

* We can provide a tuple of strings as prefixes.
* If the string starts with **any one** of them, `startswith()` returns `True`.
* `"Hello, world!"` starts with `"Hello"`, so the result is `True`.

---

## Summary

* `startswith()` is useful for checking the beginning of a string.
* Supports checking with **specific start and end positions**.
* Can check against **multiple prefixes** using a tuple.

---

```

If you want, I can also create a **shorter, visually neat version** suitable for **quick revision flashcards**. Do you want me to do that?
```

