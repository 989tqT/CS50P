# Functions

* An action or verb that executes a specific task within a program.
* Programming languages provide a predetermined set of built-in functions for fundamental operations.
* Programmers invoke these functions to direct the computer's behavior.


# Arguments

* An input provided to a function that influences its behavior.
* Passed within parentheses to determine specific actions, such as supplying a text string for the `print` function to output to the screen.


# Side Effects

* An observable outcome (such as visual or audio output) resulting from a function's execution.
* Displaying text on the screen is a common example of a visual side effect.


# Bugs

* A mistake or error within a program.
* An inevitable part of the programming process across all experience levels.
* Treated as problems to be solved using analytical and technical tools.


# Return Values

* Data handed back to the caller upon a function's completion.
* Enables the program to capture the result of an operation (such as gathering user input) for further use.
* Must be stored in memory (conceptually similar to a physical note, typically assigned to a variable) to be passed as an argument to subsequent functions.


# Variables

* A container located within a computer's memory used to store a value.
* Capable of holding various data types, including numbers, text, and media.
* Conceptually similar to mathematical variables (like x, y, and z), enabling a program to retain and reference data dynamically during execution.


# Comments

* Notes embedded directly within source code intended for the programmer, reviewers, or collaborators.
* Initiated by a specific character or sequence, such as the hash symbol (`#`) in Python.
* Completely ignored by the computer during execution, ensuring they do not affect the program's behavior.


# Pseudocode

* An informal method used to outline a program's logic before writing actual code.
* Written in plain human language rather than a formal programming syntax.
* Designed to structure technical thoughts succinctly, methodically, and algorithmically.


# Strings (`str`)

* A fundamental data type representing a sequence of text.
* Technically abbreviated as `str` within Python syntax, following the convention of succinct naming in programming languages.


# String Manipulation

* **User Input Unpredictability:** Human input is frequently inconsistent, often containing accidental spaces or incorrect capitalization.
* **Built-in Functionality:** The Python `str` data type includes built-in functions (methods) designed to automatically clean, reformat, and manipulate text.
* **Purpose:** Enables programmers to sanitize and standardize user input programmatically rather than relying on human accuracy.


# Documentation & Parameters

* **Parameters vs. Arguments:**
    * **Parameters:** The variables defined in a function's signature (the expected inputs).
    * **Arguments:** The actual values passed into the function during execution.
* **The `print()` Signature:** `print(*objects, sep=' ', end='\n')`
    * `*objects`: Indicates the function can accept any number of inputs (separated by commas).
    * `sep=' '`: The separator inserted between multiple objects. Defaults to a single blank space.
    * `end='\n'`: The string appended after the last object. Defaults to a newline character (`\n`), which moves the cursor to the next line.
* **Official Reference:** `docs.python.org` serves as the definitive source for Python function documentation.


# Parameter Types

*   **Positional Parameters**: Arguments assigned based on their order in the function call; the position determines which value corresponds to which parameter.
*   **Named Parameters**: Optional arguments identified by a specific name (e.g., `sep` or `end`), typically passed at the end of the function call.



# Corner Cases

*   Exceptional scenarios or "edge cases" that fall outside standard usage patterns, such as nesting quotation marks within a string.


# Integers (`int`)

* A fundamental data type representing whole numbers (e.g., -2, -1, 0, 1, 2) extending to both negative and positive infinity.
* Strictly contains no decimal points.
* Technically abbreviated as `int` within Python.

# Mathematical Operators

* Python supports standard mathematical operations alongside specialized programming operators:
    * `+` : Addition
    * `-` : Subtraction
    * `*` : Multiplication
    * `/` : Division
    * `%` : Modulo (calculates the remainder after dividing one number by another).


# Interactive Mode

* A Python feature that allows for the immediate, line-by-line execution of code.
* Ideal for rapid testing or running statements interactively without the need to save them to a dedicated script file.


# Floats (`float`)

* A fundamental data type representing a number with a decimal point (mathematically known as a real number).
* The term "floating-point" refers to the decimal point's ability to "float" between varying numbers of digits to the left or right.
* Essential for programs that require mathematical precision beyond whole numbers, enabling the processing of fractional values.


# The `round()` Function

* A built-in function used to round a numerical value.
* **Documentation Syntax (`[]`):** Square brackets in technical documentation indicate that a parameter is optional. 
* **Parameters:**
    * `number`: The required positional parameter representing the value to be rounded.
    * `ndigits`: An optional parameter specifying the exact number of decimal places to retain.
* **Behavior:**
    * If `ndigits` is omitted, the function defaults to rounding the `number` to the nearest integer.
    * If `ndigits` is specified (e.g., `1` or `2`), it rounds the `number` to that specific decimal place (tenths, hundredths, etc.).


# Custom Functions `def`

* The capability to invent and define your own functions beyond a language's built-in set.
* Designed to encapsulate specific actions to solve repetitive problems, allowing the code to be reused multiple times without duplication.


# Scope

* Refers to the specific context or region of code in which a variable exists and can be accessed.
* A variable defined within one function (e.g., `main`) is isolated and cannot be directly accessed by another function.
* To utilize a variable's value across different functions, it must be explicitly passed as an argument.

# The `return` Keyword

* An instruction used to explicitly hand back a computed value from a function to its caller.
* Differs from a side effect (like printing to a screen); returning a value allows the program to capture, store, and reuse the result for further operations (similar to the behavior of built-in functions like `input()` or `int()`).

