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

