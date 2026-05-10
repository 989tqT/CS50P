# 04: Numbers and Math

## 1. Integers and Type Casting
- An **integer** (`int`) is a whole number.
- Math operators: `+`, `-`, `*`, `/`, `%` (modulo).
- Because `input()` returns a string, we must **cast** it to an integer using `int()` before doing math.
  ```python
  x = int(input("What's x? "))
  ```

## 2. Floats and The `round()` Function
- A **float** is a real number with a decimal point.
- The `round(number[, ndigits])` function rounds a number. If `ndigits` is omitted, it rounds to the nearest integer.
  ```python
  z = round(x / y, 2) # Round to 2 decimal places
  ```

## 3. Formatting Numbers
- We can format large numbers with comma separators or force decimal places using f-strings:
  ```python
  print(f"{z:,}")   # 1,000
  print(f"{z:.2f}") # 0.67
  ```

## 4. Interactive Mode
- Typing `python` in the terminal opens the REPL (Read-Eval-Print Loop) `>>>`. It's used for rapid testing of math or syntax without creating a file.
