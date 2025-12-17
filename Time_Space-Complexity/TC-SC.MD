# 📊 Time & Space Complexity (TC & SC) — Complete Guide

This document covers **all important concepts of Time Complexity (TC) and Space Complexity (SC)** required for **DSA, coding interviews, and placements**. It is beginner‑friendly and Python‑oriented.

---

## 📌 1. What is Time Complexity?

Time Complexity describes **how the running time of an algorithm grows with input size (n)**.

* It does **not** measure actual time in seconds
* It measures **number of operations**
* Expressed using **Big‑O notation**

### Example

```python
for i in range(n):
    print(i)
```

➡ Time Complexity = **O(n)**

---

## 📌 2. What is Space Complexity?

Space Complexity describes **how much extra memory an algorithm uses** as input size grows.

It includes:

* Variables
* Data structures
* Recursive call stack

---

## 📌 3. Big‑O Notation (Most Important)

| Notation   | Name         | Example                 |
| ---------- | ------------ | ----------------------- |
| O(1)       | Constant     | Accessing array element |
| O(log n)   | Logarithmic  | Binary Search           |
| O(n)       | Linear       | Single loop             |
| O(n log n) | Linearithmic | Merge Sort              |
| O(n²)      | Quadratic    | Nested loops            |
| O(2ⁿ)      | Exponential  | Fibonacci (recursive)   |
| O(n!)      | Factorial    | Permutations            |

---

## 📌 4. Common Time Complexity Patterns

### 🔹 O(1) — Constant Time

```python
x = arr[0]
```

### 🔹 O(n) — Linear Time

```python
for i in range(n):
    pass
```

### 🔹 O(n²) — Quadratic Time

```python
for i in range(n):
    for j in range(n):
        pass
```

### 🔹 O(log n) — Logarithmic Time

```python
while n > 1:
    n //= 2
```

---

## 📌 5. Common Space Complexity Patterns

### 🔹 O(1) Space

```python
a = 10
b = 20
```

### 🔹 O(n) Space

```python
arr = [0] * n
```

---

## 📌 6. How to Calculate Time Complexity (Tips)

### ✅ Tip 1: Ignore constants

```
O(5n + 10) → O(n)
```

### ✅ Tip 2: Nested loops → Multiply

```
for i in range(n):
    for j in range(n):
```

➡ O(n²)

### ✅ Tip 3: Sequential loops → Add

```
O(n) + O(n) = O(n)
```

### ✅ Tip 4: Divide or Multiply by 2 → Log n

```
i *= 2  or  i //= 2
```

---

## 📌 7. Interview Tips (Very Important)

✔ Always mention **Worst‑case complexity**
✔ State **both Time & Space**
✔ Explain in simple words before formula
✔ Compare brute force vs optimized

---

## 🧪 8. Practice Questions with Answers

### 🔹 Q1

```python
for i in range(n):
    print(i)
```

**Time:** O(n)
**Space:** O(1)

---

### 🔹 Q2

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

**Time:** O(n²)
**Space:** O(1)

---

### 🔹 Q3

```python
i = 1
while i < n:
    i *= 2
```

**Time:** O(log n)
**Space:** O(1)


---

### 🔹 Q4

```python
arr = [0] * n
```

**Time:** O(n)
**Space:** O(n)

---

## 📌 9. TC & SC Quick Cheat Sheet

| Code Pattern  | Time     | Space |
| ------------- | -------- | ----- |
| No loop       | O(1)     | O(1)  |
| Single loop   | O(n)     | O(1)  |
| Nested loop   | O(n²)    | O(1)  |
| Binary Search | O(log n) | O(1)  |

---

