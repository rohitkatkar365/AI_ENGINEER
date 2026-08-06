> Python is a **high-level, interpreted, general-purpose programming language** that is designed to be easy to read and write. It was created by **Guido van Rossum** and first released in **1991**.

> ### Why is Python popular?

Python is widely used because it is:

* **Easy to learn** – Its syntax is simple and resembles English.
* **Versatile** – It can be used for many types of applications.
* **Cross-platform** – It runs on Windows, macOS, Linux, and more.
* **Open source** – Anyone can use and contribute to it.
* **Rich ecosystem** – Thousands of libraries are available for different tasks.

> ### What can you do with Python?

Python is used in many fields, including:

* 🌐 Web development (e.g., Django, Flask, FastAPI)
* 📊 Data analysis (e.g., Pandas, NumPy)
* 🤖 Artificial Intelligence and Machine Learning (e.g., TensorFlow, PyTorch)
* 🔬 Scientific computing
* 🎮 Game development
* 🤖 Automation and scripting
* 🛡️ Cybersecurity
* ☁️ Cloud and DevOps
* 📱 Desktop applications

> ### Variables in Python

Variable nothing but name of memory location.

For Example :

name = "Alice"
age = 25
salary = 50000

> ### What is a Data Type?

A **data type** tells Python what kind of value a variable stores.


| Data Type | Example            | Description                          |
| --------- | ------------------ | ------------------------------------ |
| `int`     | `10`               | Whole numbers                        |
| `float`   | `3.14`             | Decimal numbers                      |
| `str`     | `"Hello"`          | Text                                 |
| `bool`    | `True`             | True/False values                    |
| `list`    | `[1, 2, 3]`        | Ordered, mutable collection          |
| `tuple`   | `(1, 2, 3)`        | Ordered, immutable collection        |
| `set`     | `{1, 2, 3}`        | Unordered collection of unique items |
| `dict`    | `{"name": "John"}` | Key-value pairs                      |

> ### Python Operators

Operators are **symbols** that perform operations on variables and values.

> # 1. Arithmetic Operators
>
> These operators perform mathematical calculations.


| Operator | Meaning             | Example   |
| -------- | ------------------- | --------- |
| `+`      | Addition            | `10 + 5`  |
| `-`      | Subtraction         | `10 - 5`  |
| `*`      | Multiplication      | `10 * 5`  |
| `/`      | Division            | `10 / 5`  |
| `%`      | Modulus (Remainder) | `10 % 3`  |
| `**`     | Exponent (Power)    | `2 ** 3`  |
| `//`     | Floor Division      | `10 // 3` |

> # 2. Assignment Operators
>
> Used to assign values to variables.


| Operator | Example   | Same As      |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | Assign value |
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 3`  | `x = x - 3`  |
| `*=`     | `x *= 3`  | `x = x * 3`  |
| `/=`     | `x /= 3`  | `x = x / 3`  |
| `%=`     | `x %= 3`  | `x = x % 3`  |
| `//=`    | `x //= 3` | `x = x // 3` |
| `**=`    | `x **= 3` | `x = x ** 3` |

> # 3. Comparison (Relational) Operators
>
> These compare two values and return `True` or `False`.


| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not Equal             |
| `>`      | Greater Than          |
| `<`      | Less Than             |
| `>=`     | Greater Than or Equal |
| `<=`     | Less Than or Equal    |

> # 4. Logical Operators
>
> Used to combine conditions.


| Operator | Meaning                        |
| -------- | ------------------------------ |
| `and`    | Both conditions must be True   |
| `or`     | At least one condition is True |
| `not`    | Reverses the result            |

> # 5. Identity Operators
>
> Used to check whether two variables refer to the **same object** in memory.


| Operator | Meaning           |
| -------- | ----------------- |
| `is`     | Same object       |
| `is not` | Different objects |

> # 6. Membership Operators
>
> Used to test whether a value exists in a sequence.


| Operator | Meaning     |
| -------- | ----------- |
| `in`     | Present     |
| `not in` | Not present |

> # 7. Bitwise Operators (Introduction)
>
> These work on the binary (bit) representation of integers.


| Operator | Meaning     |
| -------- | ----------- |
| `&`      | AND         |
| \`       | \`          |
| `^`      | XOR         |
| `~`      | NOT         |
| `<<`     | Left Shift  |
| `>>`     | Right Shift |

> # Control Flow in Python
>
> ## What is Control Flow?
>
> **Control Flow** determines the order in which Python executes your code.
>
> By default, Python executes code **from top to bottom**.
>
> # Types of Control Flow
>
> Python provides three main control flow structures:
>
> 1. **Decision Making** (`if`, `elif`, `else`)
> 2. **Loops** (`for`, `while`)
> 3. **Loop Control Statements** (`break`, `continue`, `pass`
>
>
> | Topic      | Purpose                            |
> | ---------- | ---------------------------------- |
> | `if`       | Run code if a condition is true    |
> | `else`     | Run code if the condition is false |
> | `elif`     | Check additional conditions        |
> | `for`      | Repeat over a sequence             |
> | `while`    | Repeat while a condition is true   |
> | `break`    | Exit a loop immediately            |
> | `continue` | Skip the current iteration         |
> | `pass`     | Placeholder for future code        |
> | `range()`  | Generate a sequence of numbers     |
