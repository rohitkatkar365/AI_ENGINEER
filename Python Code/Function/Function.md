# What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, you can write it once inside a function and call it whenever needed.

### Advantages of Functions

* ✅ Code Reusability
* ✅ Reduces Code Duplication
* ✅ Easier Debugging
* ✅ Better Readability
* ✅ Modular Programming

def function_name(parameters):

Function body

return value

**greet**()

# Function with Parameters

Parameters are variables that receive values when the function is called.

# Return Statement

`return` sends a value back to the caller.

# Types Of   Argument

# Positional Arguments

Arguments are matched by position.

def student(name, age):
print(name, age)

student("John", 20)

# Keyword Arguments

Arguments are matched by parameter names.

def student(name, age):
print(name, age)

student(age=20, name="John")

# Default Parameters

# Variable-Length Arguments (`*args`)

Accepts multiple positional arguments.

def total(*numbers):
print(numbers)
print(sum(numbers))

total(10, 20, 30)

# Keyword Variable-Length Arguments (`**kwargs`)

Accepts multiple keyword arguments.

def student(**info):
print(info)

student(name="John", age=20, city="Pune")

# 1. `filter()`

### Purpose

`filter()`**keeps only the elements that satisfy a condition**.

### Syntax

<pre class="overflow-visible! px-0!" data-start="295" data-end="335"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼ11">filter</span><span>(</span><span class="ͼ11">function</span><span>, </span><span class="ͼ11">iterable</span><span>)</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

* `function` → Returns `True` or `False`
* `iterable` → List, tuple, set, etc.

# 2. `map()`

### Purpose

`map()`**transforms every element**.

### Syntax

<pre class="overflow-visible! px-0!" data-start="1138" data-end="1175"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼ11">map</span><span>(</span><span class="ͼ11">function</span><span>, </span><span class="ͼ11">iterable</span><span>)</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

### Example 1: Square Every Number

<pre class="overflow-visible! px-0!" data-start="1218" data-end="1316"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼ11">numbers</span><span> </span><span class="ͼv">=</span><span> [</span><span class="ͼy">1</span><span>, </span><span class="ͼy">2</span><span>, </span><span class="ͼy">3</span><span>, </span><span class="ͼy">4</span><span>]

</span><span class="ͼ11">square</span><span> </span><span class="ͼv">=</span><span> </span><span class="ͼ11">list</span><span>(</span><span class="ͼ11">map</span><span>(</span><span class="ͼv">lambda</span><span> </span><span class="ͼ11">x</span><span>: </span><span class="ͼ11">x</span><span> </span><span class="ͼv">**</span><span> </span><span class="ͼy">2</span><span>, </span><span class="ͼ11">numbers</span><span>))

</span><span class="ͼ11">print</span><span>(</span><span class="ͼ11">square</span><span>)</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

# 3. `reduce()`

### Purpose

`reduce()`**reduces all elements into a single value**.

It is available in the `functools` module.

<pre class="overflow-visible! px-0!" data-start="1798" data-end="1840"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼv">from</span><span> </span><span class="ͼ11">functools</span><span> </span><span class="ͼv">import</span><span> </span><span class="ͼ11">reduce</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

### Syntax

<pre class="overflow-visible! px-0!" data-start="1854" data-end="1894"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼ11">reduce</span><span>(</span><span class="ͼ11">function</span><span>, </span><span class="ͼ11">iterable</span><span>)</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

### Example 1: Sum of Numbers

<pre class="overflow-visible! px-0!" data-start="1932" data-end="2059"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼv">from</span><span> </span><span class="ͼ11">functools</span><span> </span><span class="ͼv">import</span><span> </span><span class="ͼ11">reduce</span><span>

</span><span class="ͼ11">numbers</span><span> </span><span class="ͼv">=</span><span> [</span><span class="ͼy">1</span><span>, </span><span class="ͼy">2</span><span>, </span><span class="ͼy">3</span><span>, </span><span class="ͼy">4</span><span>]

</span><span class="ͼ11">result</span><span> </span><span class="ͼv">=</span><span> </span><span class="ͼ11">reduce</span><span>(</span><span class="ͼv">lambda</span><span> </span><span class="ͼ11">x</span><span>, </span><span class="ͼ11">y</span><span>: </span><span class="ͼ11">x</span><span> </span><span class="ͼv">+</span><span> </span><span class="ͼ11">y</span><span>, </span><span class="ͼ11">numbers</span><span>)

</span><span class="ͼ11">print</span><span>(</span><span class="ͼ11">result</span><span>)</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>


| Function   | Purpose                              | Output Size                |
| ---------- | ------------------------------------ | -------------------------- |
| `filter()` | Keeps elements matching a condition  | Same or smaller than input |
| `map()`    | Transforms every element             | Same as input              |
| `reduce()` | Combines all elements into one value | Exactly one value          |

# Lambda Functions

Anonymous (nameless) functions.

lambda arguments: expression




| Concept         | Description                      |
| --------------- | -------------------------------- |
| `def`           | Define a function                |
| Parameters      | Variables in function definition |
| Arguments       | Values passed to a function      |
| `return`        | Send a value back                |
| `*args`         | Multiple positional arguments    |
| `**kwargs`      | Multiple keyword arguments       |
| Local Variable  | Exists only inside a function    |
| Global Variable | Exists throughout the program    |
| `lambda`        | Anonymous function               |
| Recursion       | Function calling itself          |
| Docstring       | Function documentation           |
