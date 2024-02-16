import sys
import colorama


class CLI:
    def __init__(self, num_lines=0):
        self.num_lines = num_lines
        self.lines = [""] * num_lines
        colorama.init()

    def update_line(self, line, text):
        if line < 1 or line > self.num_lines:
            raise ValueError("Invalid line number")

        self.lines[line - 1] = text
        self._print_output()

    def add_line(self, text):
        self.num_lines += 1
        self.lines.append(text)
        self._print_output()

    def insert_line(self, line_number, text, increase_num_lines=True):
        if line_number < 1 or line_number > self.num_lines:
            raise ValueError("Invalid line number")

        self.lines.insert(line_number - 1, text)

        if increase_num_lines:
            self.num_lines += 1

        if len(self.lines) > self.num_lines:
            self.lines = self.lines[:-1]
        
        self._print_output()

    def _print_output(self):
        sys.stdout.write("\033[F" * self.num_lines)

        for line in self.lines:
            sys.stdout.write("\033[K")
            sys.stdout.write(line + "\n")

        sys.stdout.write("\033[F" * (self.num_lines - len(self.lines)))
        sys.stdout.flush()

    def clear_all(self):
        self.lines = [""] * self.num_lines
        self._print_output()

    def __del__(self):
        colorama.deinit()

  
