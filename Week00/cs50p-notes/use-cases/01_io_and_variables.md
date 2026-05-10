# 01: I/O and Variables

## 1. Built-in Functions (`print`, `input`)
- **Functions** are actions the language already knows how to perform. The `print` function takes arguments (like `"hello, world"`) and outputs them to the terminal.
- **Input:** The `input()` function takes a prompt as an argument and pauses the program until the user types something and presses Enter.
  ```python
  input("What's your name? ")
  print("hello, world")
  ```

## 2. Variables
- A **variable** is a container for a value. The equal sign `=` is the assignment operator. It assigns the value on the right to the variable on the left.
  ```python
  name = input("What's your name? ")
  print("hello,")
  print(name)
  ```
- **Multiple Arguments:** We can pass multiple arguments to `print()` using a comma `,`. Python automatically inserts a space between them.
  ```python
  print("hello,", name)
  ```
  