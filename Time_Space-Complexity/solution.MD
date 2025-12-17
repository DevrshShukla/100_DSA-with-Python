# ✅ Time & Space Complexity — Detailed Solutions (Non‑Recursive)

This file contains **detailed, step‑by‑step solutions** for all practice questions from **TC_SC_Practice_Questions_No_Recursion.md**.

Focus:

* Worst‑case **Time Complexity (TC)**
* Extra **Space Complexity (SC)**
* Interview‑style explanations

---

## 🟢 Section 1: Basic Practice — Solutions

### ✅ Q1

```python
x = 10
y = 20
print(x + y)
```

**Time:** O(1)
**Space:** O(1)

🔹 Only one arithmetic operation
🔹 No dependency on input size

---

### ✅ Q2

```python
for i in range(n):
    print(i)
```

**Time:** O(n)
**Space:** O(1)

🔹 Loop runs `n` times
🔹 No extra memory used

---

### ✅ Q3

```python
for i in range(10):
    print(i)
```

**Time:** O(1)
**Space:** O(1)

🔹 Loop runs constant times (10)
🔹 Constants ignored in Big‑O

---

### ✅ Q4

```python
arr = [1, 2, 3, 4, 5]
print(arr[0])
```

**Time:** O(1)
**Space:** O(1)

🔹 Direct index access

---

## 🟡 Section 2: Loop‑Based — Solutions

### ✅ Q5

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

**Time:** O(n²)
**Space:** O(1)

🔹 Nested loops → multiply

---

### ✅ Q6

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

**Time:** O(n²)
**Space:** O(1)

🔹 Total iterations ≈ n(n−1)/2
🔹 Drop constants

---

### ✅ Q7

```python
for i in range(n):
    for j in range(5):
        print(i, j)
```

**Time:** O(n)
**Space:** O(1)

🔹 Inner loop is constant

---

### ✅ Q8

```python
for i in range(n):
    pass
for j in range(n):
    pass
```

**Time:** O(n)
**Space:** O(1)

🔹 Sequential loops → add → 2n → n

---

## 🟠 Section 3: While Loop & Logarithmic — Solutions

### ✅ Q9

```python
i = 1
while i < n:
    i = i * 2
```

**Time:** O(log n)
**Space:** O(1)

🔹 Value doubles each iteration

---

### ✅ Q10

```python
i = n
while i > 1:
    i = i // 2
```

**Time:** O(log n)
**Space:** O(1)

🔹 Value halves each iteration

---

### ✅ Q11

```python
for i in range(n):
    j = 1
    while j <= n:
        j = j * 2
```

**Time:** O(n log n)
**Space:** O(1)

🔹 Outer loop → n
🔹 Inner loop → log n

---

## 🔵 Section 4: Arrays & Space — Solutions

### ✅ Q12

```python
arr = [0] * n
```

**Time:** O(n)
**Space:** O(n)

🔹 Array creation takes n operations

---

### ✅ Q13

```python
arr = []
for i in range(n):
    arr.append(i)
```

**Time:** O(n)
**Space:** O(n)

🔹 Appending n elements

---

### ✅ Q14

```python
arr = [1, 2, 3, 4, 5]
rev = arr[::-1]
```

**Time:** O(n)
**Space:** O(n)

🔹 Creates a new reversed array

---

### ✅ Q15

```python
for i in arr:
    print(i)
```

**Time:** O(n)
**Space:** O(1)

---

## 🔴 Section 5: Interview‑Level — Solutions

### ✅ Q16

```python
for i in range(n):
    for j in range(n):
        if i == j:
            break
```

**Time:** O(n²)
**Space:** O(1)

🔹 Worst case: break happens late

---

### ✅ Q17

```python
i = n
while i > 0:
    i -= 1
```

**Time:** O(n)
**Space:** O(1)

---

### ✅ Q18

```python
for i in range(n):
    if i % 2 == 0:
        print(i)
```

**Time:** O(n)
**Space:** O(1)

🔹 Condition does not reduce iterations

---

### ✅ Q19

```python
max_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
```

**Time:** O(n)
**Space:** O(1)

🔹 Single traversal

---

### ✅ Q20

```python
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print(arr[i], arr[j])
```

**Time:** O(n²)
**Space:** O(1)

🔹 Triangular nested loop

---

## 🎯 Final Interview Advice

✔ Always say **worst‑case**
✔ Separate TC & SC clearly
✔ Explain pattern before formula

You are now **strong in TC & SC analysis** 🚀
