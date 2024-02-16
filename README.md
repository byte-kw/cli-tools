# cli-tools
cli-tools is a Python script that provides a convenient way to manage and update terminal output. It allows you to dynamically update and display multiple lines of text in the terminal, making it useful for progress tracking, logging, and interactive console applications.

### Introduction

The `CLI` class provides methods to add, update, and insert of text within a fixed number of lines. The output is automatically adjusted and scrolled to fit within the specified number of lines in the terminal. It utilizes the `colorama` library to apply ANSI escape sequences. It is also a better approach than using `end="\r"` for complex and multi-line output.

### Example: Dynamic Progress Output

```python
import time

terminal = CLI(num_lines=10)

for i in range(1, 11):
    progress = f"Progress: {i * 10}%"
    terminal.update_line(1, progress)
    time.sleep(1)

terminal.clear_all()
```

### Todo

- Colorize (using colorama)
- More formatting options
- Alignment
- Input Handling
