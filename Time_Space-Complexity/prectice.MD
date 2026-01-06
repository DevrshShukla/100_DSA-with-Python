# 🧠 Time & Space Complexity — Practice Questions (Non‑Recursive)

This file contains **practice questions ONLY** for **Time Complexity (TC) and Space Complexity (SC)**.

🚫 **No recursion questions included**
✅ Focused on **loops, arrays, conditions, and iterative logic**
🎯 Ideal for **beginners, placements, and interview preparation**

---

## 📌 Instructions

* Always calculate **Worst‑case Time Complexity**
* Ignore constants
* Analyze **Time and Space separately**

---

## 🟢 Section 1: Basic Practice

### Q1

```python
x = 10
y = 20
print(x + y)
```

👉 Find TC and SC

---

### Q2

```python
for i in range(n):
    print(i)
```

👉 Find TC and SC

---

### Q3

```python
for i in range(10):
    print(i)
```

👉 Find TC and SC

---

### Q4

```python
arr = [1, 2, 3, 4, 5]
print(arr[0])
```

👉 Find TC and SC

---

## 🟡 Section 2: Loop‑Based Questions

### Q5

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

👉 Find TC and SC

---

### Q6

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

👉 Find TC and SC

---

### Q7

```python
for i in range(n):
    for j in range(5):
        print(i, j)
```

👉 Find TC and SC

---

### Q8

```python
for i in range(n):
    pass
for j in range(n):
    pass
```

👉 Find TC and SC

---

## 🟠 Section 3: While Loop & Logarithmic

### Q9

```python
i = 1
while i < n:
    i = i * 2
```

👉 Find TC and SC

---

### Q10

```python
i = n
while i > 1:
    i = i // 2
```

👉 Find TC and SC

---

### Q11

```python
i = 1
while i <= n:
    j = 1
    while j <= n:
        j = j * 2
    i += 1
```

👉 Find TC and SC

---

## 🔵 Section 4: Arrays & Space Complexity

### Q12

```python
arr = [0] * n
```

👉 Find TC and SC

---

### Q13

```python
arr = []
for i in range(n):
    arr.append(i)
```

👉 Find TC and SC

---

### Q14

```python
arr = [1, 2, 3, 4, 5]
rev = arr[::-1]
```

👉 Find TC and SC

---

### Q15

```python
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)
```

👉 Find TC and SC

---

## 🔴 Section 5: Interview‑Level Tricky Questions

### Q16

```python
for i in range(n):
    for j in range(n):
        if i == j:
            break
```

👉 Find TC and SC

---

### Q17

```python
i = n
while i > 0:
    i -= 1
```

👉 Find TC and SC

---

### Q18

```python
for i in range(n):
    if i % 2 == 0:
        print(i)
```

👉 Find TC and SC

---

### Q19

```python
arr = [1, 2, 3, 4, 5]
max_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
```

👉 Find TC and SC

---

### Q20

```python
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print(arr[i], arr[j])
```

👉 Find TC and SC

---

## 🎯 Goal

If you can **correctly analyze all questions in this file**, you are **strong in TC & SC fundamentals**.

👉 Next step: Apply these skills while solving **Arrays, Strings, and Searching problems**.

Happy Practice 🚀
