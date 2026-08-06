# What is File Handling?

**File handling** is the process of creating, reading, writing, updating, and deleting files using Python.

Instead of storing data only in memory, file handling allows you to save data permanently on your computer.

Examples:

* Saving user information
* Reading configuration files
* Writing logs
* Processing CSV files
* Reading text documents

# Types of Files

Python mainly works with two types of files:

### 1. Text Files

Human-readable files.

Examples:

<pre class="overflow-visible! px-0!" data-start="555" data-end="603"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>notes.txt
data.csv
config.ini</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

### 2. Binary Files

Store data in binary format.

Examples:

<pre class="overflow-visible! px-0!" data-start="672" data-end="733"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>image.jpg
video.mp4
music.mp3
document.pdf</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

# Opening a File

Use the `open()` function.

### Syntax

<pre class="overflow-visible! px-0!" data-start="798" data-end="846"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼ11">file</span><span> </span><span class="ͼv">=</span><span> </span><span class="ͼ11">open</span><span>(</span><span class="ͼ11">filename</span><span>, </span><span class="ͼ11">mode</span><span>)</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>


| Mode   | Meaning                          |
| ------ | -------------------------------- |
| `"r"`  | Read (default)                   |
| `"w"`  | Write (overwrite)                |
| `"a"`  | Append                           |
| `"x"`  | Create new file                  |
| `"t"`  | Text mode (default)              |
| `"b"`  | Binary mode                      |
| `"r+"` | Read and write                   |
| `"w+"` | Write and read (overwrites file) |
| `"a+"` | Append and read                  |



# Using `with` Statement (Recommended)

The `with` statement automatically closes the file, even if an error occurs.


# tell()

Returns the current position.



# seek()

Move the pointer.




| Function/Method | Purpose                  |
| --------------- | ------------------------ |
| `open()`        | Open a file              |
| `read()`        | Read entire file         |
| `read(size)`    | Read specific characters |
| `readline()`    | Read one line            |
| `readlines()`   | Read all lines as a list |
| `write()`       | Write text               |
| `writelines()`  | Write multiple lines     |
| `close()`       | Close the file           |
| `tell()`        | Current file position    |
| `seek()`        | Move file pointer        |
| `os.rename()`   | Rename a file            |
| `os.remove()`   | Delete a file            |
| `csv.reader()`  | Read CSV                 |
| `csv.writer()`  | Write CSV                |
| `json.load()`   | Read JSON                |
| `json.dump()`   | Write JSON               |
