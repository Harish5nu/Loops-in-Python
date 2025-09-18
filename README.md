# Chapter 7 – Loops in Python

Loops in Python allow us to repeat a block of code multiple times.  
For example: printing numbers from **1 to 1000**.

---

## Types of Loops in Python
Python supports two main types of loops:

- **while loop**
- **for loop**

We will learn them one by one.

---

## While Loop

The `while` loop executes a block of code as long as a condition is `True`.

### Syntax
```python
while condition:
    # body of the loop
```

- The condition is checked first.  
- If it evaluates to `True`, the loop body runs.  
- This continues until the condition becomes `False`.  
- If the condition never becomes `False`, the loop runs infinitely.

### Example
```python
i = 0
while i < 5:   # runs 5 times
    print("Harry")
    i = i + 1
```

### Quick Quiz
- Print numbers from 1 to 50 using a `while` loop.  
- Print all the items of a list using a `while` loop.

---

## For Loop

The `for` loop is used to iterate over a sequence such as a list, tuple, or string.

### Syntax
```python
for item in sequence:
    # body of the loop
```

### Example
```python
l = [1, 7, 8]
for item in l:
    print(item)   # prints 1, 7, 8
```

---

## The `range()` Function

The `range()` function generates a sequence of numbers.  
It is commonly used with `for` loops.

```python
range(start, stop, step)
```

- `start`: starting value (default = 0)  
- `stop`: end value (exclusive)  
- `step`: increment (default = 1)

### Example
```python
for i in range(0, 7):
    print(i)   # prints 0 to 6
```

---

## For Loop with Else

A `for` loop can have an `else` block.  
The `else` runs after the loop finishes normally (not interrupted by `break`).

### Example
```python
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("done")
```

**Output:**
```
1
7
8
done
```

---

## Break Statement

The `break` statement is used to exit the loop immediately.

### Example
```python
for i in range(0, 80):
    print(i)
    if i == 3:
        break
```

**Output:**
```
0
1
2
3
```

---

## Continue Statement

The `continue` statement skips the current iteration and moves to the next one.

### Example
```python
for i in range(4):
    print("printing")
    if i == 2:
        continue
    print(i)
```

---

## Pass Statement

The `pass` statement does nothing.  
It is used as a placeholder when no code is needed.

### Example
```python
for item in [1, 7, 8]:
    pass
```

---

# Chapter 7 – Practice Set

1. Write a program to print the multiplication table of a number using a `for` loop.  
2. Greet all names in a list that start with **"S"**.  
   ```python
   l = ["Harry", "Soham", "Sachin", "Rahul"]
   ```
3. Attempt Problem 1 using a `while` loop.  
4. Check whether a number is prime or not.  
5. Find the sum of first `n` natural numbers using a `while` loop.  
6. Calculate the factorial of a number using a `for` loop.  
7. Print the following star pattern (`n = 3`):
   ```
     *
    ***
   *****
   ```
8. Print the following star pattern (`n = 3`):
   ```
   *
   **
   ***
   ```
9. Print the following star pattern (`n = 3`):
   ```
   * * *
   * *
   * * *
   ```
10. Print the multiplication table of `n` in reverse order using a `for` loop.

---

✅ These are the basics of **Loops in Python** with examples and exercises.
