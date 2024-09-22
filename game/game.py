import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level >= 0:
            generator = random.randint(0, level)
            while True:
                guess = int(input("Number Guess: "))

                if guess > generator:
                    print("Too large!")
                elif guess < generator:
                    print("Too small!")
                else:
                    print("Just right!")
                    sys.exit(0)

        else:
            continue
    except ValueError:
        pass
