# What are Modules and Packages?

As your programs grow larger, keeping all code in a single file becomes difficult.

Python solves this problem using:

* **Modules** → A single Python file (`.py`) containing functions, variables, or classes.
* **Packages** → A folder containing multiple related modules.

Project
│
├── main.py
├── math_utils.py        ← Module
├── string_utils.py      ← Module
│
└── utilities/           ← Package
├── __init__.py
├── calculator.py
└── converter.py

# Module

A **module** is simply a Python file.

Example:

### math\_utils.py

<pre class="overflow-visible! px-0!" data-start="681" data-end="764"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼv">def</span><span> </span><span class="ͼ11">add</span><span>(</span><span class="ͼ11">a</span><span>, </span><span class="ͼ11">b</span><span>):
    </span><span class="ͼv">return</span><span> </span><span class="ͼ11">a</span><span> </span><span class="ͼv">+</span><span> </span><span class="ͼ11">b</span><span>

</span><span class="ͼv">def</span><span> </span><span class="ͼ11">subtract</span><span>(</span><span class="ͼ11">a</span><span>, </span><span class="ͼ11">b</span><span>):
    </span><span class="ͼv">return</span><span> </span><span class="ͼ11">a</span><span> </span><span class="ͼv">-</span><span> </span><span class="ͼ11">b</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

Another file:

### main.py

<pre class="overflow-visible! px-0!" data-start="794" data-end="891"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼv">import</span><span> </span><span class="ͼ11">math_utils</span><span>

</span><span class="ͼ11">print</span><span>(</span><span class="ͼ11">math_utils</span><span class="ͼv">.</span><span>add(</span><span class="ͼy">10</span><span>, </span><span class="ͼy">20</span><span>))
</span><span class="ͼ11">print</span><span>(</span><span class="ͼ11">math_utils</span><span class="ͼv">.</span><span>subtract(</span><span class="ͼy">30</span><span>, </span><span class="ͼy">10</span><span>))</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

# Why Use Modules?

Benefits:

* Reuse code
* Better organization
* Easier debugging
* Easy maintenance
* Avoid duplicate code

# Packages

A package is a folder containing related modules.

Example:

<pre class="overflow-visible! px-0!" data-start="4849" data-end="4963"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>project/

│
├── main.py
│
└── tools/
    ├── __init__.py
    ├── math_tools.py
    └── string_tools.py</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>



| Concept           | Description                           |
| ----------------- | ------------------------------------- |
| Module            | A single`.py`file                     |
| Package           | A folder containing modules           |
| `import`          | Import an entire module               |
| `from ... import` | Import specific objects               |
| `as`              | Create an alias                       |
| `__name__`        | Indicates how a module is executed    |
| `__main__`        | Entry point for a script              |
| `pip`             | Install external packages             |
| `venv`            | Create an isolated Python environment |
