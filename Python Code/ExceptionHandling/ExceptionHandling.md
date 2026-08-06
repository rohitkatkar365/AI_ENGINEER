# What is Exception Handling?

An **exception** is an error that occurs while a program is running (runtime error).

If an exception is **not handled**, the program stops immediately.

Exception handling allows your program to **catch errors**, handle them gracefully, and continue running.

# Why Use Exception Handling?

Benefits:

* ✅ Prevents program crashes
* ✅ Provides meaningful error messages
* ✅ Improves user experience
* ✅ Makes programs more robust
* ✅ Helps in debugging


| Exception           | Cause                    |
| ------------------- | ------------------------ |
| `ZeroDivisionError` | Division by zero         |
| `ValueError`        | Invalid value            |
| `TypeError`         | Wrong data type          |
| `IndexError`        | Invalid list index       |
| `KeyError`          | Missing dictionary key   |
| `FileNotFoundError` | File doesn't exist       |
| `NameError`         | Undefined variable       |
| `AttributeError`    | Invalid object attribute |
| `ImportError`       | Import failed            |

try:

Risky code

except:

Handle error

try
│
├── Exception?
│      │
│      ├── Yes → except
│      │
│      └── No → else
│
└────────────→ finally




| Keyword   | Purpose                            |
| --------- | ---------------------------------- |
| `try`     | Wrap risky code                    |
| `except`  | Handle exceptions                  |
| `else`    | Runs if no exception occurs        |
| `finally` | Always executes                    |
| `raise`   | Manually raise an exception        |
| `assert`  | Verify conditions during debugging |
