## Lines.py

The program expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.py`, or if the specified file does not exist, the program exits via `sys.exit`. It assumes that any line that starts with `#`, optionally preceded by whitespace, is a comment and that any line that only contains whitespace is blank.

