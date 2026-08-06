> # What is a String?
>
> A **string** is a sequence of characters enclosed in **single quotes (`'`)**, **double quotes (`"`)**, or **triple quotes (`'''` or `"""`)**.

# Strings are Immutable

**A string **cannot be changed** after it is created.**

# 1. Indexing

Each character has a position called an **index**.

P  y  t  h  o  n
0  1  2  3  4  5

P  y  t  h  o  n
-6 -5 -4 -3 -2 -1

# 2. Slicing

string[start:stop:step]

# 3. Concatenation

Joining strings using `+`.

## Method 3: f-Strings (Recommended)


| Topic             | Description                              |
| ----------------- | ---------------------------------------- |
| Indexing          | Access individual characters             |
| Slicing           | Extract part of a string                 |
| Concatenation     | Join strings using`+`                    |
| Formatting        | Use`+`,`format()`, or`f""`               |
| Escape Characters | `\n`,`\t`,`\\`,`\"`,`\'`                 |
| Raw Strings       | Prefix with`r`to ignore escape sequences |
| `upper()`         | Convert to uppercase                     |
| `lower()`         | Convert to lowercase                     |
| `split()`         | Split into a list                        |
| `join()`          | Join list elements into a string         |
| `replace()`       | Replace part of a string                 |
| `find()`          | Find the first occurrence of a substring |
| `count()`         | Count occurrences                        |
| `strip()`         | Remove leading/trailing whitespace       |
| `startswith()`    | Check prefix                             |
| `endswith()`      | Check suffix                             |

> # What is a List?

A **list** is an **ordered**, **mutable (changeable)** collection that can store multiple items of **different data types**.


| Operation          | Method      |
| ------------------ | ----------- |
| Add one item       | `append()`  |
| Add multiple items | `extend()`  |
| Insert at index    | `insert()`  |
| Remove by value    | `remove()`  |
| Remove by index    | `pop()`     |
| Remove all items   | `clear()`   |
| Reverse list       | `reverse()` |
| Sort in place      | `sort()`    |
| Count items        | `count()`   |
| Find index         | `index()`   |
| Copy list          | `copy()`    |

# Key Takeaways

* A **list** is an ordered, mutable collection that can hold any data type.
* Use **indexing** and **slicing** to access elements or sublists.
* `append()` adds one element, while `extend()` adds multiple elements.
* `sort()` changes the original list; `sorted()` returns a new sorted list.
* List comprehensions provide a clean and efficient way to create or transform lists.
* Always be mindful of common pitfalls like shared references (`b = a`) and invalid indexes.

# What is a Tuple?

A **tuple** is an **ordered** collection of items that is **immutable** (cannot be changed after creation).

✔ Ordered

✔ Immutable

✔ Allows duplicate values

✔ Can store different data types

✔ Faster than lists for read-only data

# Packing

Packing means storing multiple values into one tuple.

# Unpacking

Unpacking means assigning tuple elements to variables.

# When to Use Tuples

Use tuples when:

* Data should not change.
* You want to return multiple values from a function.
* You need a fixed collection of values.
* You want slightly better performance than a list for read-only data.


| Feature     | List            | Tuple                   |
| ----------- | --------------- | ----------------------- |
| Syntax      | `[]`            | `()`                    |
| Mutable     | ✅ Yes          | ❌ No                   |
| Ordered     | ✅ Yes          | ✅ Yes                  |
| Duplicates  | ✅ Yes          | ✅ Yes                  |
| Methods     | Many            | Only`count()`,`index()` |
| Performance | Slightly slower | Slightly faster         |


| Topic     | Description                            |
| --------- | -------------------------------------- |
| Tuple     | Ordered, immutable collection          |
| Indexing  | Access elements by position            |
| Slicing   | Extract part of a tuple                |
| Packing   | Combine values into a tuple            |
| Unpacking | Assign tuple elements to variables     |
| `count()` | Count occurrences of a value           |
| `index()` | Find the first index of a value        |
| Immutable | Cannot modify, add, or remove elements |

# What is a Set?

A **set** is an **unordered**, **mutable** collection of **unique** elements.

# Characteristics of Sets

✔ Unordered

✔ Mutable (you can add/remove items)

✔ No duplicate values

✔ Can store different immutable data types

✔ Fast membership testing (`in`)


| Feature    | List       | Set            |
| ---------- | ---------- | -------------- |
| Ordered    | ✅ Yes     | ❌ No          |
| Duplicates | ✅ Allowed | ❌ Not allowed |
| Indexing   | ✅ Yes     | ❌ No          |
| Mutable    | ✅ Yes     | ✅ Yes         |
| Syntax     | `[]`       | `{}`           |


| Method                   | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| `add()`                  | Add one element                          |
| `update()`               | Add multiple elements                    |
| `remove()`               | Remove element (raises error if missing) |
| `discard()`              | Remove element (no error if missing)     |
| `pop()`                  | Remove and return an arbitrary element   |
| `clear()`                | Remove all elements                      |
| `union()`                | Combine two sets                         |
| `intersection()`         | Common elements                          |
| `difference()`           | Elements in first set only               |
| `symmetric_difference()` | Elements in either set, not both         |
| `issubset()`             | Check if one set is contained in another |
| `issuperset()`           | Check if one set contains another        |
| `copy()`                 | Create a shallow copy                    |



# What is a Dictionary?

A **dictionary** is a **mutable**, **unordered** collection of **key-value pairs**.

Each **key** is unique and is used to access its corresponding **value**.


# Characteristics of Dictionaries

✔ Store data as **key : value**

✔ Mutable (can add, update, delete)

✔ Keys must be unique

✔ Values can be duplicated

✔ Keys must be immutable (`int`, `str`, `tuple`, etc.)



| Method      | Purpose                                 |
| ----------- | --------------------------------------- |
| `get()`     | Get value safely                        |
| `keys()`    | Return all keys                         |
| `values()`  | Return all values                       |
| `items()`   | Return key-value pairs                  |
| `update()`  | Add/update multiple items               |
| `pop()`     | Remove a specific key                   |
| `popitem()` | Remove the last inserted key-value pair |
| `clear()`   | Remove all items                        |
| `copy()`    | Create a shallow copy                   |




| Feature    | List | Tuple | Set  | Dictionary         |
| ---------- | ---- | ----- | ---- | ------------------ |
| Ordered    | ✅   | ✅    | ❌   | ✅ (Python 3.7+)   |
| Mutable    | ✅   | ❌    | ✅   | ✅                 |
| Duplicates | ✅   | ✅    | ❌   | Keys ❌, Values ✅ |
| Indexing   | ✅   | ✅    | ❌   | By key             |
| Syntax     | `[]` | `()`  | `{}` | `{key: value}`     |
