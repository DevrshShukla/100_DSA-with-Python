# 📘 Recursion in Data Structures & Algorithms (DSA)

Recursion is one of the most important concepts in **DSA**.  
It helps solve problems by breaking them into **smaller versions of the same problem**.

---

## 🧠 What is Recursion?

**Recursion** is a technique where:
> A function **calls itself** to solve a problem.

The function keeps calling itself **until a stopping condition is met**.

---

## 🧱 Two Essential Parts of Recursion

Every recursive solution has **ONLY TWO things**:

### 1️⃣ Base Case
- The condition where recursion **stops**
- Prevents infinite calls

### 2️⃣ Recursive Case
- The part where the function **calls itself**
- Moves the problem closer to the base case

📌 **No base case = Stack Overflow**

---

## 🧠 Real-Life Examples (Very Important)

### 📦 Example 1: Boxes Inside Boxes
- Open a box
- Inside it, there is another box
- Keep opening until you find an empty box

👉 Empty box = **Base Case**  
👉 Opening next box = **Recursive Call**

---

### 🪜 Example 2: Climbing Stairs
- To reach step 10
- First reach step 9
- To reach step 9 → reach step 8
- Continue…

👉 Ground floor = **Base Case**

---

### 📂 Example 3: Folder Search
- Open a folder
- If file found → stop
- Else open sub-folder and repeat

👉 Searching folders uses **recursion**

---

## 🔁 How Recursion Works Internally

Recursion uses the **Call Stack**.

- Each recursive call is stored in memory
- Calls are removed only when base case is reached
- Follows **LIFO (Last In, First Out)**

📌 Too many calls → **Stack Overflow**

---

## 🧠 Step-by-Step Thinking Pattern

When solving recursion problems, always ask:

1️⃣ What is the **smallest version** of the problem?  
2️⃣ When should the function **stop**?  
3️⃣ How does each call reduce the problem size?

---

## 🔍 Types of Recursion (Basic Awareness)

### 1️⃣ Direct Recursion
A function calls itself directly.

---

### 2️⃣ Indirect Recursion
Function A calls Function B,  
Function B calls Function A.

---

### 3️⃣ Tail Recursion
Recursive call is the **last statement**.

📌 Easier to optimize.

---

## ⚠️ Common Mistakes in Recursion

❌ Missing base case  
❌ Base case never reached  
❌ Problem size not reducing  
❌ Too deep recursion  

These cause **Stack Overflow**

---

## 🔁 Recursion vs Iteration

| Feature | Recursion | Iteration |
|------|----------|----------|
| Uses | Call Stack | Loops |
| Memory | More | Less |
| Readability | High | Medium |
| Risk | Stack Overflow | Safe |

---

## 🧠 When to Use Recursion?

✅ Tree problems  
✅ Divide & conquer  
✅ Backtracking  
✅ Problems with repeated structure  

❌ Very large input sizes (prefer loops)

---

## 🎯 Interview Tip

If asked:
> *What is recursion?*

Answer:
> Recursion is a technique where a function solves a problem by calling itself with smaller inputs until a base case is reached.

---

## 🧠 One-Line Summary

**Recursion solves big problems by repeatedly solving smaller versions of the same problem until a base case stops the process.**

---

📌 **Next Topics to Learn**
- Stack Overflow
- Recursion Dry Run
- Backtracking
- Recursion vs DP
