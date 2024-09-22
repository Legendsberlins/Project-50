import sys
# Check number of command line arguments
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    # Perform function when file ends with .py
    try:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                # Create a variable which increments the number of lines per loop
                line_count = 0
                # Loop through each line of the file
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line and not stripped_line.startswith("#"):
                        line_count = line_count + 1
                print(line_count)
    # If file does not end with .py or not found
        else:
            sys.exit("Not a Python file")
    except(FileNotFoundError):
        sys.exit("File not found")

