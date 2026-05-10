# 05: Custom Functions (`def`)

## 1. Defining Functions
- We use the `def` keyword to invent our own functions to solve repetitive problems.
- Python uses **indentation** to determine what code belongs inside the function.
  ```python
  def hello(to="world"):
      print("hello,", to)
  ```

## 2. Parameters and Defaults
- Functions can accept **parameters** (like `to`).
- We can assign **default values** (`to="world"`) so the function doesn't crash if called without an argument.

## 3. Architecture: The `main()` Function
- Real-world Python scripts define a `main()` function to organize the primary logic, and put helper functions (like `hello()`) below it.
- **Scope:** Variables defined inside `main()` cannot be seen by `hello()`. You must explicitly pass them as arguments.

## 4. Side Effects
- A **Side Effect** is any observable outcome resulting from a function's execution that is *not* returning a value. 
- Example: `print()` displaying text on a screen, playing an audio file, or modifying a global variable.
- Functions that *only* have side effects and return nothing are often called "void" functions in other languages.

## 5. The `return` Keyword
- `return` explicitly hands back a computed data value to the caller. 
- **Difference:** While `print()` (a side effect) only shows data to the human eye, `return` hands data back to the computer's memory so the program can store it, manipulate it, or pass it to another function.