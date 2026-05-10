# 03: String Manipulation

## 1. Strings and Parameters (`end`, `sep`)
- A **string** (`str`) is a sequence of text.
- `print()` has default parameters. By default, it ends with a newline (`end='\n'`). We can override this to keep output on the same line.
  ```python
  print("hello,", end="")
  print(name)
  ```

## 2. Quotes and Escape Characters
- To include quotes inside strings, either use single quotes outside `print('hello, "friend"')` or use the escape character `\` (`print("hello, \"friend\"")`).

## 3. Formatting Strings (f-strings)
- **f-strings** are the most elegant way to inject variables into strings.
  ```python
  print(f"hello, {name}")
  ```

## 4. String Methods (`strip`, `title`)
- You must ensure user input is cleaned.
- `.strip()` removes leading/trailing whitespace.
- `.title()` capitalizes the first letter of each word.
- **Method Chaining:** You can combine them to be highly efficient.
  ```python
  name = input("What's your name? ").strip().title()
  ```

