# 🔐 Hashing in Python – Complete DSA Guide (Beginner to Advanced)

Hashing is one of the **most important concepts in Data Structures & Algorithms (DSA)**.  
It helps us **store, search, and retrieve data very fast**.

This guide explains **hashing in Python** using **simple terms, real-world examples, and DSA perspective**.

---

## 📌 What is Hashing?

**Hashing** is a technique used to:
- Convert data (key) into a fixed-size value (index)
- Store data in such a way that **search, insert, and delete** operations are very fast

👉 Average Time Complexity: **O(1)**

---

## 🧠 Real-World Analogy

### 📱 Phone Contacts
- **Name** → Key  
- **Phone Number** → Value  

You don’t search contacts line by line.  
You directly type the name and get the number instantly.

➡ This instant access is possible because of **hashing**.

---

## 🧩 Components of Hashing

### 1️⃣ Key
- Input value (e.g., number, string)
- Example: `"apple"`, `101`

### 2️⃣ Hash Function
- Converts key → index
- Example idea:  
  `index = hash(key) % table_size`

### 3️⃣ Hash Table
- An array-like structure where data is stored using index

---

## 📦 Hashing in Python

Python provides **built-in hash tables**:

| Data Structure | Uses Hashing |
|---------------|-------------|
| `dict` | ✅ Yes |
| `set` | ✅ Yes |
| `list` | ❌ No |

---