# 📘 Python Lists – Complete Guide for DSA

A **list** in Python is a built-in data structure used to store an ordered collection of elements. Lists are one of the most important structures in **Data Structures & Algorithms (DSA)** because they form the base for arrays, stacks, queues, and more.

---

## 🧱 What is a List?

```python
my_list = [1, 2, 3, 4]
```
## ✅ Properties
    Ordered

    Mutable (changeable)

    Allows duplicates

    Supports mixed data types

    Dynamic size

## 🛠 Creating Lists
python
```python
a = [1, 2, 3]
b = list((4, 5, 6))
c = []  # empty list
```
## 🔍 Accessing Elements
```python
arr = [10, 20, 30, 40]

print(arr[0])    # 10
print(arr[-1])   # 40 (last element)
```
## ✂️ Slicing Lists
```python
nums = [1, 2, 3, 4, 5]

print(nums[1:4])   # [2, 3, 4]
print(nums[:3])    # [1, 2, 3]
print(nums[::2])   # [1, 3, 5]
```
## ✏️ Modifying Elements
```python
arr = [1, 2, 3]
arr[1] = 20
print(arr)  # [1, 20, 3]
```
## ➕ Adding Elements <br>
**append()** <br>
Adds element at the end.
```python
arr = [1, 2]
arr.append(3)
```
**insert()** <br>
Adds element at a specific index.
```python
arr.insert(1, 10)  # [1, 10, 2, 3]
```
**extend()** <br>
Adds multiple elements.
```python
arr.extend([4, 5])
```
## ➖ Removing Elements
**remove()** <br>
Removes first occurrence of value.
```python
arr.remove(10)
```
**pop()** <br>
Removes element by index (default: last).
```python
arr.pop()      # last
arr.pop(1)     # index 1
```
**clear()** <br>
Removes all elements.
```python
arr.clear()
```

**del** <br>
Deletes element or whole list.
```python
del arr[0]
```

## 🔄 Traversing a List
```python
arr = [1, 2, 3]

for x in arr:
    print(x)
```
**With index:**
```python
for i in range(len(arr)):
    print(i, arr[i])
```

## 🔢 Useful Built-in Functions
```python
nums = [4, 1, 3, 2]

len(nums)     # 4
max(nums)     # 4
min(nums)     # 1
sum(nums)     # 10
```
## 🧮 List Methods
**append(x)** <br> Add element at end <br><br>
**insert(i,x)** <br>	Insert at index <br><br>
**extend(iterable)**Add multiple elements <br><br>
**remove(x)** <br> Remove first occurrence <br><br>
**pop(i)** <br>	Remove & return element <br><br>
**clear()** <br>	Remove all elements <br><br>
**index(x)** <br>	Return index of x <br><br>
**count(x)** <br>	Count occurrences <br><br>
**sort()** <br>	Sort list <br><br>
**reverse()** <br>	Reverse list <br><br>
**copy()** <br>	Shallow copy <br><br>

Example:

python
Copy code
nums = [3, 1, 2]
nums.sort()
nums.reverse()

## 🔁 Sorting Lists
``` python
nums = [4, 2, 1, 3]

nums.sort()               # ascending
nums.sort(reverse=True)  # descending

sorted_nums = sorted(nums)  # returns new list
```
## 🪞 Copying Lists
``` python
a = [1, 2, 3]

b = a.copy()
c = a[:]        # slicing copy
d = list(a)     # constructor copy
```
## ⚠️ Avoid:
``` python
b = a  # both point to same list
```
## 🧠 List Comprehension
Compact way to create lists.
```python
squares = [x*x for x in range(1, 6)]
```
**With condition:**
```python
evens = [x for x in range(10) if x % 2 == 0]
```

## 🔍 Searching in List
```python
arr = [10, 20, 30]

if 20 in arr:
    print("Found")
```
**Index:**
```python
arr.index(20)
```

📌 Summary
✔ Ordered & mutable
✔ Supports all CRUD operations
✔ Rich set of methods
✔ Backbone of Python DSA

Mastering lists = Strong DSA foundation 💪